import psycopg2
from pool_cursors import Cursors
from person import Person


class Proprietario_DAO:
    def insert(self, person: Person):
        sql = "insert into proprietario (cpf, nome, telefone, data_cadastro) values (%s, %s, %s, %s)"
        values = (person.get_cpf(), person.get_nome(), person.get_telefone(), person.get_data_cadastro())

        try:
            with Cursors.create_cursor() as cursor:
                cursor.execute(sql, values)
            print(f"{person.get_nome()} adicionado(a).")
        except psycopg2.Error as erro:
            print(erro)

        Cursors.close_cursor()

    def delete(self, cpf):
        try:
            with Cursors.create_cursor() as cursor:
                cursor.execute("delete from proprietario where cpf = %s", (cpf,))
            print("Todos os registros relacionados a esse proprietário foram apagados.")
        except psycopg2.Error as erro:
            print(erro)

        Cursors.close_cursor()

    def select(self, cpf):
        try:
            with Cursors.create_cursor() as cursor:
                cursor.execute("select * from proprietario where cpf = %s", (cpf,))
                res = cursor.fetchall()
            print("Select realizado.")
        except psycopg2.Error as erro:
            print(erro)

        Cursors.close_cursor()
        return res
