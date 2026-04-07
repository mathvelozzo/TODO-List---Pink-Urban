from app import create_app, db
from models import User

app = create_app()
with app.app_context():
    admin = User.query.filter_by(username='admin').first()
    if admin:
        admin.set_password('admin123')
        db.session.commit()
        print('Senha do admin resetada para: admin123')
    else:
        print('Usuario admin nao encontrado.')
