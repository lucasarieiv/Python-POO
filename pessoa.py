from random import randint
from connection import Connection
import json

conManager = Connection()
cnx = conManager.cnx


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def save(self):
        with cnx:
            with cnx.cursor() as cursor:
                sql = f"SELECT nome FROM pessoa WHERE nome = '{self.nome}'"
                cursor.execute(sql)
                result = cursor.fetchall()
                _msg = f'Error on register name: {self.nome} already registered'
                if result:
                    return {
                        'statusCode': 200,
                        'body': json.dumps({'message': _msg})
                    }

                sql = f"INSERT INTO pessoa (nome, idade) VALUES ('{self.nome}',{self.idade})"
                cursor.execute(sql)
                cnx.commit()

    @staticmethod
    def get_all():
        with cnx:
            with cnx.cursor() as cursor:
                sql = f"SELECT * FROM pessoa"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)

    @staticmethod
    def get_id(id):
        with cnx:
            with cnx.cursor() as cursor:
                sql = f"SELECT * FROM pessoa WHERE id = {id}"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)

    @staticmethod
    def update(id, nome, idade):
        with cnx:
            with cnx.cursor() as cursor:
                sql = f"UPDATE pessoa SET nome='{nome}', idade={idade} WHERE id = {id}"
                cursor.execute(sql)
                result = cursor.fetchall()
                cnx.commit()

    @staticmethod
    def delete(id):
        with cnx:
            with cnx.cursor() as cursor:
                sql = f"DELETE FROM pessoa WHERE id = {id}"
                cursor.execute(sql)
                result = cursor.fetchall()
                cnx.commit()
