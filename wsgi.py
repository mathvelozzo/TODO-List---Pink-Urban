"""WSGI entry point for production deployment."""
import os
from app import create_app, db, logger
from models import User
import secrets

application = create_app()

# Ensure admin exists (runs once per worker start)
with application.app_context():
    db.create_all()
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        default_pass = secrets.token_urlsafe(12)
        admin = User(
            username='admin',
            email='admin@pinkurban.com',
            role='admin',
            is_approved=True
        )
        admin.set_password(default_pass)
        db.session.add(admin)
        try:
            db.session.commit()
            logger.warning(f'Admin criado! Usuario: admin | Senha: {default_pass}')
        except Exception:
            db.session.rollback()
            # Pode ser que outro worker ja criou
            admin = User.query.filter_by(username='admin').first()
            if admin:
                logger.info('Admin ja existe (criado por outro worker).')
