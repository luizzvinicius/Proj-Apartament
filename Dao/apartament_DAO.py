import psycopg2
from pool_cursors import Cursors
from apartament import Apartament


class Apartament_DAO:
    def insert(self, apt: Apartament, cpf):
        sql = "insert into apartamento (numero, cpf, data_cadastro) values (%s, %s, %s)"
        try:
            with Cursors().create_cursor() as cursor:
                cursor.execute(sql, (apt.get_numero(), cpf, apt.get_data()))
                print("Apartamento criado.")
        except psycopg2.Error as erro:
            print(erro)

        Cursors.close_cursor()

    def select(self):
        
        Cursors.close_cursor()
