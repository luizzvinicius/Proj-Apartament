from utils import uteis, validation


def register(opt):
    '''Função que registra o veículo do apartamento.\n
        Parâmetro opt = 1 para possui veículo, qualquer outro número para não possui.
    '''
    category = placa = color = model = None
    if opt == 1:
        print("\nQual categoria?\n[ 1 ] Carro\n[ 2 ] Moto")
        category = uteis.ler_option("Digite o número: ", max_opt=2, exept_msg="Categoria inválida.")
        category = "carro" if category == 1 else "moto"
        
        while True:
            placa = input(f"Qual a placa do(a) {category}: ").strip()
            if validation.placa(placa) is True:
                break
            print("Placa inválida.\n")

        color = uteis.ler_string(f"Qual a cor do(a) {category}: ")
        model = uteis.ler_string(f"Qual o modelo do(a) {category}: ")
    car = {
        "categoria": category,
        "placa": placa,
        "cor": color,
        "modelo": model,
        "observação": "Nenhuma observação"
    }
    return car


def alter(car, option):
    '''Recebe um objeto carro e um parâmetro (1- observation; 2- color) e o retorna alterado.'''
    vehicle_key = "observação" if option == 1 else "cor"
    new_info = input(f"Qual a nova {vehicle_key} do(a) {car['categoria']}: ").strip()

    car[vehicle_key] = new_info
    return car


def delete():
    '''Define todas as informações do carro para None.'''
    return {"categoria": None, "placa": None, "cor": None, "modelo": None, "observação": None}
