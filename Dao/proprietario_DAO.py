from pool_cursors import Cursors
from person import Person


class Proprietario_DAO:
    def insert(self, person: Person):
        sql = "insert into proprietario (cpf, nome, telefone, data_cadastro) values (%s, %s, %s, %s);"
        values = (person.get_cpf(), person.get_nome(), person.get_telefone(), person.get_data_cadastro())

        with Cursors.create_cursor() as cursor:
            cursor.execute(sql, values)
            Cursors.close_cursor()
        print(f"{person.get_nome()} adicionado(a).")

    def delete(self, cpf):
        with Cursors.create_cursor() as cursor:
            cursor.execute("delete from proprietario where cpf = %s", (cpf,))
            Cursors.close_cursor()
        print("Todos os registros relacionados a esse proprietário foram apagados.")

    def select(self, cpf):
        with Cursors.create_cursor() as cursor:
            cursor.execute("select * from proprietario where cpf = %s", (cpf,))
            res = cursor.fetchall()
            Cursors.close_cursor()
        print("Select realizado.")
        return res
