import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
limiter = Limiter(key_func=get_remote_address)

# Logging configuracao
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger('pink_urban')


def create_app():
    app = Flask(__name__)

    # Config
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(64).hex())
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///pink_urban.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SESSION_COOKIE_SECURE'] = os.getenv('SESSION_COOKIE_SECURE', 'false').lower() == 'true'
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
    app.config['REMEMBER_COOKIE_SECURE'] = os.getenv('SESSION_COOKIE_SECURE', 'false').lower() == 'true'
    app.config['REMEMBER_COOKIE_HTTPONLY'] = True

    # Init extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Faca login para acessar essa pagina.'
    login_manager.login_message_category = 'warning'
    rate_storage = os.getenv('RATELIMIT_STORAGE_URL', 'memory://')
    app.config.setdefault('RATELIMIT_STORAGE_URL', rate_storage)
    limiter.init_app(app)

    # Security headers (Talisman) — so ativa se FORCED ou nao for debug
    force_https = os.getenv('FORCE_HTTPS', 'false').lower() == 'true'
    if not app.debug or force_https:
        Talisman(app,
                 force_https=force_https,
                 force_https_permanent=True,
                 content_security_policy={
                     'default-src': "'self'",
                     'style-src': "'self' 'unsafe-inline' https://fonts.googleapis.com",
                     'font-src': "'self' https://fonts.gstatic.com",
                     'script-src': "'self' 'unsafe-inline'",
                     'img-src': "'self' data:"
                 })

    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        return db.session.get(User, int(user_id))

    # Register blueprints
    from main import main_bp
    from auth import auth_bp
    from admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # Create tables
    with app.app_context():
        from models import User
        db.create_all()
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            import secrets
            default_pass = secrets.token_urlsafe(12)
            admin = User(
                username='admin',
                email='admin@pinkurban.com',
                role='admin',
                is_approved=True
            )
            admin.set_password(default_pass)
            db.session.add(admin)
            db.session.commit()
            logger.warning(f'Admin criado. Senha: {default_pass} — ALTERE NO PRIMEIRO ACESSO!')

    return app
