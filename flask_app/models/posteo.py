from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Posteo:
    db_name = 'esquema_cinturon'

    def __init__(self, data):
        self.id = data['id']
        self.posteo = data['posteo']
        self.user_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posteos (posteo, usuario_id) VALUES (%(posteo)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def traer_todo(cls,data):
        query = "SELECT * FROM posteos LEFT JOIN usuarios  on usuarios.id = posteos.usuario_id;"
        todo_posteo = []
        results = connectToMySQL(cls.db_name).query_db(query,data)
        for row in results:
            todo_posteo.append(cls(row))
        return todo_posteo

    @classmethod
    def todo(cls, data):
        query = "SELECT * FROM posteos WHERE usuario_id = %(id)s;"
        todo = []
        results = connectToMySQL(cls.db_name).query_db(query, data)
        for row in results:
            todo.append(cls(row))
        return todo
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posteos;"
        results = connectToMySQL(cls.db_name).query_db(query)
        all_recipes = []
        for row in results:
            all_recipes.append(cls(row))
        return all_recipes

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM posteos WHERE usuario_id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE posteos SET post=%(post)s, like=%(like)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def eliminar(cls, data):
        query = "DELETE FROM posteos WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validar_posteo(posteo):
        is_valid = True
        if len(posteo['posteo']) < 5:
            is_valid = False
            flash("El posteo debe tener por lo menos 5 caracteres")
        return is_valid


