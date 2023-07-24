from pool_cursors import Cursors
from person import Person


class Person_DAO:
    def insert(self, person: Person, num_apto):
        sql = "insert into pessoa (cpf, nome, telefone, data_cadastro, num_apto) values (%s, %s, %s, %s, %s);"
        values = (person.get_cpf(), person.get_nome(), person.get_telefone(), person.get_data_cadastro(), num_apto)

        with Cursors.create_cursor() as cursor:
            cursor.execute(sql, values)
            Cursors.close_cursor()
        print(f"{person.get_nome()} adicionado(a).")

    def delete(self, cpf):
        with Cursors.create_cursor() as cursor:
            cursor.execute("delete from pessoa where cpf = %s", (cpf,))
            Cursors.close_cursor()
        print("Morador excluído.")

    def select(self, num_apto):
        with Cursors.create_cursor() as cursor:
            cursor.execute("select * from pessoa where num_apto = %s", (num_apto,))
            res = cursor.fetchall()
            Cursors.close_cursor()
        print("Select realizado.")
        return res
