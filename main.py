from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash
from flask_login import current_user, login_required
from app import db
from models import TodoList, ListItem
import uuid

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/list/<slug>')
def view_list(slug):
    todo_list = TodoList.query.filter_by(slug=slug).first_or_404()
    is_owner = current_user.is_authenticated and current_user.id == todo_list.created_by
    return render_template('view_list.html', todo_list=todo_list, is_owner=is_owner)

@main_bp.route('/create-list', methods=['POST'])
@login_required
def create_list():
    data = request.get_json()
    title = data.get('title', '').strip()
    if not title:
        return jsonify({'error': 'Titulo e obrigatorio'}), 400

    slug = str(uuid.uuid4())[:8]
    new_list = TodoList(title=title, slug=slug, created_by=current_user.id)
    db.session.add(new_list)
    db.session.commit()

    return jsonify({'slug': new_list.slug, 'message': 'Lista criada com sucesso!'}), 201

@main_bp.route('/api/lists')
@login_required
def get_my_lists():
    lists = TodoList.query.filter_by(created_by=current_user.id).order_by(TodoList.created_at.desc()).all()
    return jsonify([{
        'id': l.id,
        'title': l.title,
        'slug': l.slug,
        'is_public': l.is_public,
        'created_at': l.created_at.strftime('%d/%m/%Y %H:%M') if l.created_at else ''
    } for l in lists])

@main_bp.route('/api/list/<int:list_id>/items', methods=['GET'])
@login_required
def get_items(list_id):
    todo_list = TodoList.query.get_or_404(list_id)
    if todo_list.created_by != current_user.id:
        return jsonify({'error': 'Acesso negado'}), 403
    items = [{'id': i.id, 'text': i.text, 'done': i.done} for i in todo_list.items]
    return jsonify(items)

@main_bp.route('/api/list/<int:list_id>/add', methods=['POST'])
@login_required
def add_item(list_id):
    todo_list = TodoList.query.get_or_404(list_id)
    if todo_list.created_by != current_user.id:
        return jsonify({'error': 'Acesso negado'}), 403

    data = request.get_json()
    text = data.get('text', '').strip()
    if not text:
        return jsonify({'error': 'Texto e obrigatorio'}), 400

    item = ListItem(text=text, list_id=list_id)
    db.session.add(item)
    db.session.commit()

    return jsonify({'id': item.id, 'text': item.text, 'done': item.done}), 201

@main_bp.route('/api/item/<int:item_id>/toggle', methods=['POST'])
@login_required
def toggle_item(item_id):
    item = ListItem.query.get_or_404(item_id)
    if item.parent_list.created_by != current_user.id:
        return jsonify({'error': 'Acesso negado'}), 403

    item.done = not item.done
    db.session.commit()

    return jsonify({'id': item.id, 'done': item.done})

@main_bp.route('/api/item/<int:item_id>', methods=['DELETE'])
@login_required
def delete_item(item_id):
    item = ListItem.query.get_or_404(item_id)
    if item.parent_list.created_by != current_user.id:
        return jsonify({'error': 'Acesso negado'}), 403

    db.session.delete(item)
    db.session.commit()

    return jsonify({'message': 'Item removido'}), 200

@main_bp.route('/api/list/<int:list_id>/title', methods=['PUT'])
@login_required
def update_list_title(list_id):
    todo_list = TodoList.query.get_or_404(list_id)
    if todo_list.created_by != current_user.id:
        return jsonify({'error': 'Acesso negado'}), 403

    data = request.get_json()
    title = data.get('title', '').strip()
    if not title:
        return jsonify({'error': 'Titulo e obrigatorio'}), 400

    todo_list.title = title
    db.session.commit()

    return jsonify({'message': 'Titulo atualizado'})

@main_bp.route('/api/list/<int:list_id>/delete', methods=['DELETE'])
@login_required
def delete_list(list_id):
    todo_list = TodoList.query.get_or_404(list_id)
    if todo_list.created_by != current_user.id:
        return jsonify({'error': 'Acesso negado'}), 403

    db.session.delete(todo_list)
    db.session.commit()

    return jsonify({'message': 'Lista removida'}), 200
