import sqlite3
from database.db import get_db_connection

class FormularioModel:

    @staticmethod
    def create_formulario(user_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO formulario (user_id, nome, email, data_nascimento, cpf, genero)
                              VALUES (?, ?, ?, ?, ?, ?)''',
                           (user_id, nome, email, data_nascimento, cpf, genero))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()

    @staticmethod
    def find_by_id(formulario_id):
        conn = get_db_connection()
        formulario = conn.execute('SELECT * FROM formulario WHERE id = ?', (formulario_id,)).fetchone()
        conn.close()
        return formulario

    @staticmethod
    def update_formulario(formulario_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()
        try:
            conn.execute('''UPDATE formulario 
                            SET nome = ?, email = ?, data_nascimento = ?, cpf = ?, genero = ?
                            WHERE id = ?''',
                         (nome, email, data_nascimento, cpf, genero, formulario_id))
            conn.commit()
            return True
        except Exception:
            return False
        finally:
            conn.close()

    @staticmethod
    def delete_formulario(formulario_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM formulario WHERE id = ?', (formulario_id,))
        conn.commit()
        rows_affected = cursor.rowcount
        conn.close()
        return rows_affected > 0