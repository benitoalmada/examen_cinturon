from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


class Like:
    db = "esquema_cinturon"
    #def __init__(self, data):
    #    self.id = data['id']
    #    self.posteo_id = data['posteo_id']
    #    self.user_id = data['usuario_id']
    #    self.created_at = data['created_at']
    #    self.updated_at = data['updated_at']

  #  @classmethod
  #  def save(cls, data):
  #      query = "INSERT INTO likes (posteo_id, usuario_id) VALUES (%(posteo_id)s,%(user_id)s);"
  #      return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def traer_todo(cls, data):
        query = "SELECT posteo_id, count(posteo_id) as cant_gusta from likes JOIN posteos ON posteos.id = likes.posteo_id GROUP BY posteo_id ORDER BY cant_gusta DESC;"
        todo_like = []
        results = connectToMySQL(cls.db).query_db(query, data)
        for row in results:
            todo_like.append(cls(row))
        return todo_like

 #   @classmethod
 #   def get_all(cls):
 #       query = "SELECT * FROM likes;"
 #       results = connectToMySQL(cls.db_name).query_db(query)
 #       all_like = []
 #       for row in results:
 #           all_like.append(cls(row))
 #       return all_like


    @classmethod
    def eliminar(cls, data):

        query = "DELETE FROM likes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO likes (posteo_id, usuario_id) VALUES (%(posteo)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)