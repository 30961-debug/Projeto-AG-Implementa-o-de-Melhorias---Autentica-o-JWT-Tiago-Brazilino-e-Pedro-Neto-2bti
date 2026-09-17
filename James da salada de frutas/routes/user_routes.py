from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.user_controller import UserController

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    response, status = UserController.register_user(request.get_json())
    return jsonify(response), status

@user_bp.route('/login', methods=['POST'])
def login():
    response, status = UserController.login_user(request.get_json())
    return jsonify(response), status

@user_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_user(id):
    response, status = UserController.get_user(id)
    return jsonify(response), status

@user_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    response, status = UserController.update_user(id, request.get_json())
    return jsonify(response), status

@user_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    response, status = UserController.delete_user(id)
    return jsonify(response), status