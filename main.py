'''Módulo com funções muito usadas no projeto'''
from utils import uteis, validation


def main():
    '''Função que executa o programa de fato.'''
    #apartament = apartament_register()
    # owner = person_register(owner=True)

    # msg = "Quantas pessoas vão morar no apartamento? "
    # people_in_apartament = uteis.ler_option(msg, max_opt=4, exept_msg="Quantidade inválida. Máximo 4")
    # people = {}
    # for i in range(1, people_in_apartament+1):
    #     print(f"\n{i}º Morador")
    #     people.setdefault(f"person{i}", person_register())
    #     print()

    print("Você possui carro?\n[ 1 ] Sim\n[ 2 ] Não\n")
    opt = uteis.ler_option("Digite o número: ", max_opt=2)
    car = car_register(opt)
    print()

    # print(owner)
    # print(people)
    print(car)
    #print(apartament)


def apartament_register():
    '''Função que cria a numeração do apartamento'''
    bloco = uteis.ler_option("Bloco: ", max_opt=29, exept_msg="Número de bloco inválido.")
    bloco = str(bloco).zfill(2) if bloco < 10 else str(bloco)

    num_apto = validation.apto("Número do apartamento (sem 0 a esquerda): ")
    
    return {"bloco": bloco, "apartamento": num_apto, "Banco de dados": bloco + num_apto}


def person_register(owner=False):
    '''Função que registra as pessoas ou proprietário que moram no apartamento'''
    msg = "Nome do proprietário do apartamento: " if owner else "Nome: "
    name = input(msg)
    # Regex para aceitar letras, acentos e espaços
    cpf = 0
    while True:
        try:
            cpf = input("CPF (apenas números): ")
            if len(cpf) != 11:
                raise ValueError("\033[31mCPF inválido.\033[m")
            break
        except ValueError as expt:
            print(expt)

    return {"name": name, "cpf": validation.cpf(cpf)}


def car_register(opt):
    '''
        Função que registra o carro do apartamento.\n
        Parâmetro opt = 1 para possui carro, qualquer outro número para não possui carro.
    '''
    car = {}
    if opt == 1:
        car = {
            "placa": uteis.ler_string("Qual a placa do carro: ", exept_msg="Placa inválida"),
            "cor": uteis.ler_string("Qual a cor do carro: "),
            "modelo": uteis.ler_string("Qual o modelo do carro: "),
            "observação": "Nenhuma observação"
        }
    else:
        car = {
            "placa": None,
            "cor": None,
            "modelo": None,
            "observação": "Nenhuma observação"
        }
    return car


main()
