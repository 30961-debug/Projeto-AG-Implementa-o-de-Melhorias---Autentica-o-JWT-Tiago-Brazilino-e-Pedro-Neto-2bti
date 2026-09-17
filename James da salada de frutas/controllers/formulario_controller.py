from models.formulario_model import FormularioModel

class FormularioController:

    @staticmethod
    def create_formulario(user_id, data):
        if not data:
            return {"error": "Dados não fornecidos"}, 400

        nome = data.get('nome')
        email = data.get('email')
        data_nascimento = data.get('data_nascimento')
        cpf = data.get('cpf')
        genero = data.get('genero')

        if not nome or not email or not data_nascimento or not cpf or not genero:
            return {"error": "Todos os campos são obrigatórios"}, 400

        formulario_id = FormularioModel.create_formulario(
            user_id, nome, email, data_nascimento, cpf, genero
        )
        if formulario_id:
            return {"message": "Formulário criado com sucesso", "id": formulario_id}, 201

        return {"error": "Erro ao criar formulário"}, 500

    @staticmethod
    def get_formulario(formulario_id):
        formulario = FormularioModel.find_by_id(formulario_id)
        if not formulario:
            return {"message": "Formulário não encontrado"}, 404

        return {
            "id": formulario['id'],
            "user_id": formulario['user_id'],
            "nome": formulario['nome'],
            "email": formulario['email'],
            "data_nascimento": formulario['data_nascimento'],
            "cpf": formulario['cpf'],
            "genero": formulario['genero']
        }, 200

    @staticmethod
    def update_formulario(formulario_id, data):
        formulario = FormularioModel.find_by_id(formulario_id)
        if not formulario:
            return {"message": "Formulário não encontrado"}, 404

        if not data:
            return {"error": "Nenhum dado informado para atualização"}, 400

        nome = data.get('nome', formulario['nome'])
        email = data.get('email', formulario['email'])
        data_nascimento = data.get('data_nascimento', formulario['data_nascimento'])
        cpf = data.get('cpf', formulario['cpf'])
        genero = data.get('genero', formulario['genero'])

        if FormularioModel.update_formulario(formulario_id, nome, email, data_nascimento, cpf, genero):
            return {"message": "Formulário atualizado com sucesso"}, 200

        return {"error": "Erro ao atualizar formulário"}, 500

    @staticmethod
    def delete_formulario(formulario_id):
        formulario = FormularioModel.find_by_id(formulario_id)
        if not formulario:
            return {"message": "Formulário não encontrado"}, 404

        if FormularioModel.delete_formulario(formulario_id):
            return {"message": "Formulário excluído com sucesso"}, 200

        return {"error": "Erro ao excluir formulário"}, 500