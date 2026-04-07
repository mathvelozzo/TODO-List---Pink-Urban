from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from functools import wraps
from app import db, logger
from models import User, TodoList
import secrets

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/reset-admin-pass')
def reset_admin_password():
    """Temporary endpoint to reset admin password. Requires URL token."""
    token = request.args.get('token', '')
    expected = secrets.compare_digest(token, 'pink-admin-reset-2026') if token else False
    if not expected:
        return jsonify({'error': 'Acesso negado'}), 403

    admin = User.query.filter_by(username='admin').first()
    if not admin:
        return jsonify({'error': 'Admin nao encontrado'}), 404

    new_pass = secrets.token_urlsafe(12)
    admin.set_password(new_pass)
    admin.is_approved = True
    db.session.commit()

    logger.info(f'Admin password reset via endpoint: {new_pass}')

    return jsonify({
        'message': 'Senha do admin resetada!',
        'user': 'admin',
        'senha': new_pass
    })

admin_bp = Blueprint('admin', __name__)

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            if request.is_json:
                return jsonify({'error': 'Acesso negado. Requer permissao de administrador.'}), 403
            flash('Acesso negado.', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated

@admin_bp.route('/')
@login_required
@admin_required
def dashboard():
    pending_users = User.query.filter_by(is_approved=False).all()
    total_users = User.query.count()
    total_lists = TodoList.query.count()
    return render_template('admin/dashboard.html',
                         pending_users=pending_users,
                         total_users=total_users,
                         total_lists=total_lists)

@admin_bp.route('/approve-user/<int:user_id>', methods=['POST'])
@login_required
@admin_required
def approve_user(user_id):
    user = User.query.get_or_404(user_id)
    user.is_approved = True
    db.session.commit()
    if request.is_json:
        return jsonify({'message': f'Usuario {user.username} aprovado com sucesso!'})
    flash(f'Usuario {user.username} aprovado!', 'success')
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/reject-user/<int:user_id>', methods=['POST'])
@login_required
@admin_required
def reject_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    if request.is_json:
        return jsonify({'message': f'Usuario {user.username} removido.'})
    flash(f'Usuario {user.username} removido.', 'info')
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/users')
@login_required
@admin_required
def all_users():
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@admin_bp.route('/api/users')
@login_required
@admin_required
def api_users():
    users = User.query.all()
    return jsonify([{
        'id': u.id,
        'username': u.username,
        'email': u.email,
        'role': u.role,
        'is_approved': u.is_approved,
        'created_at': u.created_at.strftime('%d/%m/%Y %H:%M') if u.created_at else ''
    } for u in users])

@admin_bp.route('/api/toggle-role/<int:user_id>', methods=['POST'])
@login_required
@admin_required
def toggle_role(user_id):
    user = User.query.get_or_404(user_id)
    if user.id == current_user.id:
        return jsonify({'error': 'Voce nao pode alterar seu proprio papel.'}), 400
    user.role = 'admin' if user.role != 'admin' else 'user'
    db.session.commit()
    return jsonify({'id': user.id, 'role': user.role})

@admin_bp.route('/api/lists')
@login_required
@admin_required
def api_all_lists():
    lists = TodoList.query.order_by(TodoList.created_at.desc()).all()
    return jsonify([{
        'id': l.id,
        'title': l.title,
        'slug': l.slug,
        'is_public': l.is_public,
        'created_by': l.owner.username,
        'created_at': l.created_at.strftime('%d/%m/%Y %H:%M') if l.created_at else ''
    } for l in lists])
