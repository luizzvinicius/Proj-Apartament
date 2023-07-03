'''Módulo com funções muito usadas no projeto'''
from utils import uteis


def main():
    '''Função que executa o programa de fato.'''
    owner = person_register(owner=True)

    msg = "Quantas pessoas vão morar no apartamento? "
    people_in_apartament = uteis.ler_option(
        msg, max_opt=4, exept_msg="Gente demais")
    people = {}
    for i in range(1, people_in_apartament+1):
        print(f"{i}º Morador:")
        people.setdefault(f"person{i}", person_register())
        print()
    print()

    print("Você possui carro?\n[ 1 ] Sim\n[ 2 ] Não\n")
    opt = uteis.ler_option("Digite o número: ", max_opt=2)
    if opt == 1:
        car = car_register()
    print()

    print(owner)
    print(people)
    print(car)


def apartament_register():
    '''Função que cria a numeração do apartamento'''
    apartament = {
        "bloco": uteis.ler_string("Bloco: "),
        "num": uteis.ler_string("Número: ")
    }
    return apartament


def person_register(owner=False):
    '''Função que registra as pessoas ou proprietário que moram no apartamento'''
    if owner:
        name = input("Nome do proprietário do apartamento: ")
    else:
        name = input("Nome do morador do apartamento: ")
    person = {
        "name": name,
        "cpf": input("CPF do proprietário do apartamento: ")
    }
    return person


def car_register():
    '''Função que registra o carro do apartamento'''
    car = {
        "placa": uteis.ler_string("Qual a placa do carro: ", exept_msg="Placa inválida"),
        "cor": uteis.ler_string("Qual a cor do carro: ", exept_msg="Cor inválida"),
        "modelo": uteis.ler_string("Qual o modelo do carro: ", exept_msg="Modelo inválido")
    }
    return car


main()
