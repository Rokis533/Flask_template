from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import User
from app.utils.decorators import json_required

bp = Blueprint('api', __name__)


@bp.route('/users/<int:user_id>')
@login_required
def get_user(user_id):
    """Get user information"""
    user = User.query.get_or_404(user_id)
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'full_name': user.full_name,
        'created_at': user.created_at.isoformat()
    })


@bp.route('/profile', methods=['PUT'])
@login_required
@json_required
def update_profile():
    """Update user profile via API"""
    data = request.get_json()
    
    if 'first_name' in data:
        current_user.first_name = data['first_name']
    if 'last_name' in data:
        current_user.last_name = data['last_name']
    
    from app.extensions import db
    db.session.commit()
    
    return jsonify({
        'message': 'Profile updated successfully',
        'user': {
            'id': current_user.id,
            'full_name': current_user.full_name
        }
    })