import psycopg2
from person import Person
from pool_cursors import Cursors


class OwnerDao:
    def insert(self, person: Person):
        sql = "insert into proprietario (cpf, nome, telefone, data_cadastro) values (%s, %s, %s, %s)"
        values = (person.get_cpf(), person.get_name(), person.get_phone(), person.get_date())

        with Cursors() as cursor:
            try:
                cursor.execute(sql, values)
                print(f"{person.get_name()} adicionado(a).\n")
            except psycopg2.Error as erro:
                print(f"\n{erro}")

    def delete(self, cpf):
        with Cursors() as cursor:
            try:
                cursor.execute(
                    "delete from proprietario where cpf = %s", (cpf,))
                print("Todos os registros relacionados a esse proprietário foram apagados.\n")
            except psycopg2.Error as erro:
                print(f"\n{erro}")

    def select(self, cpf):
        with Cursors() as cursor:
            try:
                cursor.execute("select * from proprietario where cpf = %s", (cpf,))
                res = cursor.fetchall()
                print("Select realizado.\n")
            except psycopg2.Error as erro:
                print(f"\n{erro}")
        return res
