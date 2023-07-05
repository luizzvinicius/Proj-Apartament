'''Módulo com funções muito usadas no projeto'''
from utils import uteis, validation


def main():
    '''Função que executa o programa de fato.'''
    apartament = apartament_register()
    # owner = person_register(owner=True)

    # msg = "\nQuantas pessoas vão morar no apartamento? "
    # people_in_apartament = uteis.ler_option(
    #     msg, max_opt=4, exept_msg="Gente demais")
    # people = {}
    # for i in range(1, people_in_apartament+1):
    #     print(f"\n{i}º Morador")
    #     people.setdefault(f"person{i}", person_register())
    #     print()

    # print("Você possui carro?\n[ 1 ] Sim\n[ 2 ] Não\n")
    # opt = uteis.ler_option("Digite o número: ", max_opt=2)
    # car = car_register(opt)
    # print()

    # print(owner)
    # print(people)
    # print(car)
    print(apartament)


def apartament_register():
    '''Função que cria a numeração do apartamento'''
    bloco = uteis.ler_option("Bloco: ", max_opt=29, exept_msg="Número de bloco inválido.")
    
    if bloco < 10:
        bloco = str(bloco).zfill(2)
    else:
        bloco = str(bloco)
    
    while True:
        num_apto = input("Número do apartamento: ")
        if len(num_apto) < 2:
            num_apto = "00" + num_apto
        elif num_apto[0] in ("0", "1", "2", "3") and num_apto[2] in ("1", "2", "3", "4"):
            break
        elif len(num_apto) == 2 or len(num_apto) > 3:
            print("Número de apartamento inválido.")
            continue

    return {"bloco": bloco, "apartamento": num_apto, "Banco de dados": bloco + num_apto}


def person_register(owner=False):
    '''Função que registra as pessoas ou proprietário que moram no apartamento'''
    person = {}
    if owner:
        name = input("Nome do proprietário do apartamento: ")
    else:
        name = input("Nome: ")

    cpf = 0
    while True:
        try:
            cpf = input("CPF (apenas números): ")
            if len(cpf) != 11:
                raise ValueError("CPF inválido.")
            break
        except ValueError as expt:
            print(expt)

    person.setdefault("name", name)
    person.setdefault("cpf", validation.cpf(cpf))
    return person


def car_register(opt):
    '''Função que registra o carro do apartamento'''
    car = {}
    if opt == 1:
        car.setdefault("placa", uteis.ler_string(
            "Qual a placa do carro: ", exept_msg="Placa inválida"))
        car.setdefault("cor", uteis.ler_string(
            "Qual a cor do carro: ", exept_msg="Cor inválida"))
        car.setdefault("modelo", uteis.ler_string(
            "Qual o modelo do carro: ", exept_msg="Modelo inválido"))
        car.setdefault("observação", "Nenhuma observação")
    else:
        car.setdefault("placa", None)
        car.setdefault("cor", None)
        car.setdefault("modelo", None)
        car.setdefault("observação", "Apartamento não possui carro")
    return car


main()
