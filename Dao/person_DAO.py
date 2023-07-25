import psycopg2
from pool_cursors import Cursors
from person import Person


class Person_Dao:
    def insert(self, person: Person, num_apto):
        sql = "insert into pessoa (cpf, nome, telefone, data_cadastro, num_apto) values (%s, %s, %s, %s, %s);"
        values = (person.get_cpf(), person.get_nome(), person.get_telefone(), person.get_data_cadastro(), num_apto)

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
                cursor.execute("delete from pessoa where cpf = %s", (cpf,))
            print("Morador excluído.")
        except psycopg2.Error as erro:
            print(erro)

        Cursors.close_cursor()

    def select(self, num_apto):
        try:
            with Cursors.create_cursor() as cursor:
                cursor.execute("select * from pessoa where num_apto = %s", (num_apto,))
                res = cursor.fetchall()
            print("Select realizado.")
        except psycopg2.Error as erro:
            print(erro)

        Cursors.close_cursor()
        return res
