import psycopg2
from psycopg2 import sql
from pool_cursors import Cursors
from vehicle import Vehicle


class VehicleDao:
    def insert(self, vehicle: Vehicle, num_apto):
        command = "insert into veiculo (placa, categoria, cor, modelo, observacao, data_cadastro, num_apto) values (%s, %s, %s, %s, %s, %s, %s)"
        values = (vehicle.get_placa(), vehicle.get_category(), vehicle.get_color(), vehicle.get_model(), vehicle.get_obs(), vehicle.get_date(), num_apto)

        with Cursors() as cursor:
            try:
                cursor.execute(command, values)
                print(f"{vehicle.get_category()} adicionado(a).\n")
            except psycopg2.Error as erro:
                print(f"\n{erro}")

    def delete(self, placa):
        with Cursors() as cursor:
            try:
                cursor.execute("delete from veiculo where placa = %s", (placa,))
                print("Veículo excluído.\n")
            except psycopg2.Error as erro:
                print(f"\n{erro}")

    def update(self, field, new_value, placa):
        command = sql.SQL("update veiculo set {} = %s where placa = %s").format(sql.Identifier(field))

        with Cursors() as cursor:
            try:
                cursor.execute(command, (new_value, placa))
                print(f"{field} alterado(a).\n")
            except psycopg2.Error as erro:
                print(f"\n{erro}")

    def select(self, placa):
        with Cursors() as cursor:
            try:
                cursor.execute("select * from veiculo where placa = %s", (placa,))
                res = cursor.fetchall()
                print("Select realizado.\n")
            except psycopg2.Error as erro:
                print(f"\n{erro}")
        return res
