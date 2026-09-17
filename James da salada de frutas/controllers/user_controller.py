from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models.user_model import UserModel

class UserController:

    @staticmethod
    def register_user(data):
        if not data:
            return {"error": "Dados não fornecidos"}, 400

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Nome de usuário e senha são obrigatórios"}, 400

        hashed_password = generate_password_hash(password)
        if UserModel.create_user(username, hashed_password):
            return {"message": "Usuário registrado com sucesso"}, 201

        return {"error": "Nome de usuário já existe"}, 400

    @staticmethod
    def login_user(data):
        if not data:
            return {"error": "Dados não fornecidos"}, 400

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Nome de usuário e senha são obrigatórios"}, 400

        user = UserModel.find_by_username(username)
        if user and check_password_hash(user['password'], password):
            access_token = create_access_token(identity=str(user['id']))
            return {"access_token": access_token}, 200

        return {"error": "Credenciais inválidas"}, 401

    @staticmethod
    def get_user(user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "Usuário não encontrado"}, 404

        return {
            "id": user['id'],
            "username": user['username']
        }, 200

    @staticmethod
    def update_user(user_id, data):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "Usuário não encontrado"}, 404

        if not data:
            return {"error": "Nenhum dado informado para atualização"}, 400

        username = data.get('username')
        password = data.get('password')

        hashed_password = generate_password_hash(password) if password else None

        if UserModel.update_user(user_id, username=username, password=hashed_password):
            return {"message": "Usuário atualizado com sucesso"}, 200

        return {"error": "Erro ao atualizar usuário"}, 400

    @staticmethod
    def delete_user(user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "Usuário não encontrado"}, 404

        if UserModel.delete_user(user_id):
            return {"message": "Usuário excluído com sucesso"}, 200

        return {"error": "Erro ao excluir usuário"}, 500