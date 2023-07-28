import psycopg2
from person import Person
from pool_cursors import Cursors


class PersonDao:
    def insert(self, person: Person, num_apt):
        sql = "insert into pessoa (cpf, nome, telefone, data_cadastro, num_apto) values (%s, %s, %s, %s, %s)"
        values = (person.get_cpf(), person.get_name(), person.get_phone(), person.get_date(), num_apt)

        with Cursors() as cursor:
            try:
                cursor.execute(sql, values)
                print(f"{person.get_name()} adicionado(a).")
            except psycopg2.Error as erro:
                print(erro)

    def delete(self, cpf):
        with Cursors() as cursor:
            try:
                cursor.execute("delete from pessoa where cpf = %s", (cpf,))
                print("Morador excluído.")
            except psycopg2.Error as erro:
                print(erro)

    def select(self, num_apt):
        with Cursors() as cursor:
            try:
                cursor.execute(
                    "select * from pessoa where num_apto = %s", (num_apt,))
                res = cursor.fetchall()
                print("Select realizado.")
            except psycopg2.Error as erro:
                print(erro)
        return res
