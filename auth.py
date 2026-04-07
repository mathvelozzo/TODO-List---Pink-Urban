from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from models import User
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        username = data.get('username', '').strip()
        password = data.get('password', '')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            if not user.is_approved:
                if request.is_json:
                    return jsonify({'error': 'Sua conta ainda nao foi aprovada pelo administrador.'}), 403
                flash('Sua conta ainda nao foi aprovada pelo administrador.', 'warning')
                return render_template('login.html')

            login_user(user)
            if request.is_json:
                return jsonify({'message': 'Login realizado com sucesso!'})
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('main.index'))
        else:
            if request.is_json:
                return jsonify({'error': 'Usuario ou senha invalidos.'}), 401
            flash('Usuario ou senha invalidos.', 'danger')

    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        username = data.get('username', '').strip()
        email = data.get('email', '').strip()
        password = data.get('password', '')
        confirm = data.get('confirm_password', '')

        errors = []

        if not username or len(username) < 3:
            errors.append('Usuario deve ter pelo menos 3 caracteres.')
        if not email or '@' not in email:
            errors.append('Email invalido.')
        if not password or len(password) < 6:
            errors.append('Senha deve ter pelo menos 6 caracteres.')
        if password != confirm:
            errors.append('As senhas nao coincidem.')

        if User.query.filter_by(username=username).first():
            errors.append('Usuario ja existe.')
        if User.query.filter_by(email=email).first():
            errors.append('Email ja cadastrado.')

        if errors:
            if request.is_json:
                return jsonify({'errors': errors}), 400
            for e in errors:
                flash(e, 'danger')
            return render_template('register.html')

        user = User(username=username, email=email, is_approved=False, role='user')
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        if request.is_json:
            return jsonify({'message': 'Cadastro realizado! Aguarde aprovacao do administrador.'}), 201
        flash('Cadastro realizado! Aguarde aprovacao do administrador.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Voce saiu da sua conta.', 'info')
    return redirect(url_for('main.index'))

@auth_bp.route('/check-approval')
@login_required
def check_approval():
    return jsonify({'is_approved': current_user.is_approved})
