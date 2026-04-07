from wsgi import application, db, logger
from models import User
import secrets

app = application
with app.app_context():
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        logger.error('Admin not found!')
        exit(1)

    new_pass = secrets.token_urlsafe(12)
    admin.set_password(new_pass)
    admin.is_approved = True
    db.session.commit()

    logger.info(f'Admin password reset!')
    logger.info(f'User: admin')
    logger.info(f'Senha: {new_pass}')
    print('========================================')
    print(f'ADMIN PASSWORD RESET')
    print(f'User: admin')
    print(f'Senha: {new_pass}')
    print('========================================')
