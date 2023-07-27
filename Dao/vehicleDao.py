import psycopg2
from psycopg2 import sql
from pool_cursors import Cursors
from vehicle import Vehicle


class VehicleDao:
    def insert(self, vehicle: Vehicle, num_apto):
        sql = "insert into veiculo (placa, categoria, cor, modelo, observacao, data_cadastro, num_apto) values (%s, %s, %s, %s, %s, %s, %s)"
        values = (vehicle.get_placa(), vehicle.get_categoria(), vehicle.get_cor(), vehicle.get_modelo(), vehicle.get_observacao(), vehicle.get_data(), num_apto)

        with Cursors() as cursor:
            try:
                cursor.execute(sql, values)
                print(f"{vehicle.get_categoria()} adicionado(a).")
            except psycopg2.Error as erro:
                print(erro)

    def delete(self, placa):
        with Cursors() as cursor:
            try:
                cursor.execute("delete from veiculo where placa = %s", (placa,))
                print("Veículo excluído.")
            except psycopg2.Error as erro:
                print(erro)

    def update(self, field, new_value, placa):
        command = sql.SQL("update veiculo set {} = %s where placa = %s").format(sql.Identifier(field))

        with Cursors() as cursor:
            try:
                cursor.execute(command, (new_value, placa))
                print(f"{field} alterado(a).")
            except psycopg2.Error as erro:
                print(erro)

    def select(self, placa):
        sql = "select * from veiculo where placa = %s"

        with Cursors() as cursor:
            try:
                cursor.execute(sql, (placa,))
                res = cursor.fetchall()
                print("Select realizado.")
            except psycopg2.Error as erro:
                print(erro)
        return res
