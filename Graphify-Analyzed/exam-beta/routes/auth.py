from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from models import db, User

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
bcrypt = Bcrypt()


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        return jsonify({'type': 'error', 'title': 'Bad Request', 'status': 400, 'detail': 'リクエストボディが必要です'}), 400

    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '')
    display_name = data.get('display_name', '').strip()
    language = data.get('language', 'ja')

    errors = {}
    if not username:
        errors['username'] = 'ユーザー名は必須です'
    if User.query.filter_by(username=username).first():
        errors['username'] = 'このユーザー名は既に使用されています'
    if not email:
        errors['email'] = 'メールアドレスは必須です'
    if User.query.filter_by(email=email).first():
        errors['email'] = 'このメールアドレスは既に使用されています'
    if len(password) < 6:
        errors['password'] = 'パスワードは6文字以上必要です'
    if errors:
        return jsonify({
            'type': 'https://example.com/errors/validation-error',
            'title': 'Validation Error',
            'status': 400,
            'detail': '入力内容に誤りがあります',
            'instance': '/api/auth/register',
            'errors': errors
        }), 400

    user = User(
        username=username,
        email=email,
        password_hash=bcrypt.generate_password_hash(password).decode('utf-8'),
        display_name=display_name or username,
        language=language
    )
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({'type': 'error', 'title': 'Bad Request', 'status': 400, 'detail': 'リクエストボディが必要です'}), 400

    username = data.get('username', '')
    password = data.get('password', '')

    user = User.query.filter_by(username=username).first()
    if not user or not bcrypt.check_password_hash(user.password_hash, password):
        return jsonify({
            'type': 'https://example.com/errors/authentication-error',
            'title': 'Authentication Error',
            'status': 401,
            'detail': 'ユーザー名またはパスワードが正しくありません',
            'instance': '/api/auth/login'
        }), 401

    login_user(user)
    return jsonify({'message': 'ログインしました', 'user': user.to_dict()}), 200


@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'ログアウトしました'}), 200


@auth_bp.route('/me', methods=['GET'])
@login_required
def get_me():
    return jsonify(current_user.to_dict()), 200


@auth_bp.route('/profile', methods=['PUT'])
@login_required
def update_profile():
    data = request.get_json()
    if not data:
        return jsonify({'type': 'error', 'title': 'Bad Request', 'status': 400, 'detail': 'リクエストボディが必要です'}), 400

    if 'display_name' in data:
        current_user.display_name = data['display_name']
    if 'language' in data:
        current_user.language = data['language']
    if 'email' in data:
        current_user.email = data['email']

    db.session.commit()
    return jsonify({'message': 'プロフィールを更新しました', 'user': current_user.to_dict()}), 200
