from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.formulario_controller import FormularioController

formulario_bp = Blueprint('formularios', __name__)

@formulario_bp.route('/', methods=['POST'])
@jwt_required()
def create_formulario():
    user_id = get_jwt_identity()
    response, status = FormularioController.create_formulario(user_id, request.get_json())
    return jsonify(response), status

@formulario_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_formulario(id):
    response, status = FormularioController.get_formulario(id)
    return jsonify(response), status

@formulario_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_formulario(id):
    response, status = FormularioController.update_formulario(id, request.get_json())
    return jsonify(response), status

@formulario_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_formulario(id):
    response, status = FormularioController.delete_formulario(id)
    return jsonify(response), status