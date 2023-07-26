import psycopg2
from pool_cursors import Cursors
from vehicle import Vehicle


class Vehicle_DAO:
    def insert(self, vehicle: Vehicle, num_apto):
        sql = "insert into veiculo (placa, categoria, cor, modelo, observacao, data_cadastro, num_apto) values (%s, %s, %s, %s, %s, %s, %s)"
        values = (vehicle.get_placa(), vehicle.get_categoria(), vehicle.get_cor(), vehicle.get_modelo(), vehicle.get_observacao(), vehicle.get_data(), num_apto)

        try:
            with Cursors.create_cursor() as cursor:
                cursor.execute(sql, values)
            print(f"{vehicle.get_categoria()} adicionado(a).")
        except psycopg2.Error as erro:
            print(erro)

        Cursors.close_cursor()

    def delete(self, placa):
        try:
            with Cursors.create_cursor() as cursor:
                cursor.execute("delete from veiculo where placa = (%s)", (placa,))
            print("Veículo excluído.")
        except psycopg2.Error as erro:
            print(erro)

        Cursors.close_cursor()

    def update(self, field, new_value, placa):
        sql = "update veiculo set (%s) = (%s) where placa = (%s)"
        try:
            with Cursors.create_cursor() as cursor:
                cursor.execute(sql, (field, new_value, placa))
            print(f"{field} alterado(a).")
        except psycopg2.Error as erro:
            print(erro)

        Cursors.close_cursor()

    def select(self, placa):
        sql = "select * from veiculo where placa = (%s)"
        try:
            with Cursors.create_cursor() as cursor:
                cursor.execute(sql, (placa,))
                res = cursor.fetchall()
            print("Select realizado.")
        except psycopg2.Error as erro:
            print(erro)

        Cursors.close_cursor()
        return res
