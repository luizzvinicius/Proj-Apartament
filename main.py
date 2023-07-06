'''Módulo com funções muito usadas no projeto'''
from utils import uteis, validation


def main():
    '''Função que executa o programa de fato.'''
    # print("[ 1 ] Cadastrar proprietário do apartamento")
    # print("[ 2 ] Cadastrar moradores do apartamento")
    # print("[ 3 ] Cadastrar carro(s) do apartamento")
    # print("[ 4 ] Adicionar observação ao carro")
    # print("[ 5 ] Editar cor do carro(s)")
    # apartament = apartament_register()
    owner = person_register(owner=True)

    # msg = "Quantas pessoas vão morar no apartamento? "
    # people_in_apartament = uteis.ler_option(msg, max_opt=4, exept_msg="Quantidade inválida. Máximo 4")
    # people = {}
    # for i in range(1, people_in_apartament+1):
    #     print(f"\n{i}º Morador")
    #     people.setdefault(f"person{i}", person_register())

    # print("Você possui carro?\n[ 1 ] Sim\n[ 2 ] Não\n")
    # opt = uteis.ler_option("Digite o número: ", max_opt=2)
    # car = car_register(opt)
    # print()

    print(owner)
    # print(people)
    # print(car)
    # print(apartament)


def apartament_register():
    '''Função que cria a numeração do apartamento'''
    bloco = uteis.ler_option("Bloco: ", max_opt=29, exept_msg="Número de bloco inválido.")
    bloco = "0" + str(bloco) if bloco < 10 else str(bloco)

    num_apto = 0
    while True:
        num_apto = uteis.ler_inteiro("Número do apartamento: ")
        if validation.apto(num_apto) is True:
            num_apto = str(num_apto)
            break

    return {"bloco": bloco, "apartamento": num_apto, "Banco de dados": bloco + num_apto}


def person_register(owner=False):
    '''Função que registra as pessoas ou proprietário que moram no apartamento'''
    msg = "Nome do proprietário do apartamento: " if owner else "Nome: "
    name = "1"
    while True:
        name = input(msg).strip()
        if validation.name(name) is True:
            break
        print("Formato de nome inválido.\n")

    cpf = 0
    while True:
        try:
            cpf = input("CPF (apenas números): ").strip()
            if validation.cpf(cpf) is not False:
                cpf = validation.cpf(cpf)
                break
            raise ValueError("\033[31mCPF inválido.\033[m\n")
        except ValueError as expt:
            print(expt)

    return {"name": name, "cpf": cpf}


def car_register(opt):
    '''
        Função que registra o carro do apartamento.\n
        Parâmetro opt = 1 para possui carro, qualquer outro número para não possui carro.
    '''
    if opt == 1:
        while True:
            placa = input("Qual a placa do carro: ").strip()
            if validation.placa(placa) is True:
                break
            print("Placa inválida.\n")

        color = uteis.ler_string("Qual a cor do carro: ")
        model = uteis.ler_string("Qual o modelo do carro: ")
    car = {
        "placa": placa or None,
        "cor": color or None,
        "model": model or None,
        "observation": "Nenhuma observação"
    }
    return car


main()
