'''Gravar a data do registro'''
from datetime import date as d
from utils import uteis, validation


def register(opt, category=None):
    '''Função que registra o veículo do apartamento.\n
        Parâmetro opt = 1 para possui veículo, qualquer outro número para não possui.
    '''
    placa = color = model = date = None
    if opt == 1:
        category = "carro" if category == 1 else "moto"
        
        while True:
            placa = input(f"Qual a placa do(a) {category}: ").strip()
            if validation.placa(placa) is True:
                break
            print("Placa inválida.\n")

        color = uteis.ler_string(f"Qual a cor do(a) {category}: ")
        model = uteis.ler_string(f"Qual o modelo do(a) {category}: ")
        date = d.today()
    car = {
        "categoria": category,
        "placa": placa,
        "cor": color,
        "modelo": model,
        "data": date,
        "observação": "Nenhuma observação"
    }
    return car


def alter(vehicle, option):
    '''Recebe um objeto carro e um parâmetro (1- observation; 2- color) e o retorna alterado.'''
    vehicle_key = "observação" if option == 1 else "cor"
    new_info = input(f"Qual a nova {vehicle_key} do(a) {vehicle['categoria']}: ").strip()

    vehicle[vehicle_key] = new_info
    return vehicle


def delete():
    '''Define todas as informações do carro para None.'''
    return {"categoria": None, "placa": None, "cor": None, "modelo": None, "data": None, "observação": None}
