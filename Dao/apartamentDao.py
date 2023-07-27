import psycopg2
from apartament import Apartament
from pool_cursors import Cursors


class ApartamentDao:
    def insert(self, apt: Apartament, cpf):
        sql = "insert into apartamento (numero, cpf, data_cadastro) values (%s, %s, %s)"

        with Cursors() as cursor:
            try:
                cursor.execute(sql, (apt.get_number(), cpf, apt.get_date()))
                print("Apartamento criado.")
            except psycopg2.Error as erro:
                print(erro)

    def select(self, cpf):
        query1 = "select * from proprietario where cpf = %s"
        query2 = "select numero, data_cadastro from apartamento where cpf = %s"
        query3 = "select * from veiculo where num_apto = (select numero from apartamento where cpf = %s)"
        query4 = "select * from pessoa where num_apto = (select numero from apartamento where cpf = %s)"

        with Cursors() as cursor:
            try:
                cursor.execute(query1, (cpf,))
                res1 = cursor.fetchall()
                cursor.execute(query2, (cpf,))
                res2 = cursor.fetchall()
                cursor.execute(query3, (cpf,))
                res3 = cursor.fetchall()
                cursor.execute(query4, (cpf,))
                res4 = cursor.fetchall()
                print("Select realizado")
            except psycopg2.Error as erro:
                print(erro)
        return {"proprietario": res1, "apartamento": res2, "veiculo": res3, "moradores": res4}
