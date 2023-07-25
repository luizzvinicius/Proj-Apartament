from pool_cursors import Cursors
from vehicle import Vehicle


class Vehicle_DAO:
    def insert(self, vehicle: Vehicle, num_apto):
        sql = "insert into veiculo (placa, categoria, cor, modelo, observacao, data_cadastro, num_apto) values (%s, %s, %s, %s, %s);"
        values = (vehicle.get_placa, vehicle.get_nome(), vehicle.get_telefone(), vehicle.get_data_cadastro(), num_apto)

        with Cursors.create_cursor() as cursor:
            cursor.execute(sql, values)
            Cursors.close_cursor()
        print("Veículo adicionado.")

    def delete(self, placa):
        with Cursors.create_cursor() as cursor:
            cursor.execute("delete from veiculo where placa =", (placa,))
            Cursors.close_cursor()
        print("Veículo excluído.")

    def update(self, field, new_value, placa):
        with Cursors.create_cursor() as cursor:
            cursor.execute("update veiculo set (%s) = (%s) where placa = (%s)", (field, new_value, placa))
            Cursors.close_cursor()
        print("Veículo alterado")