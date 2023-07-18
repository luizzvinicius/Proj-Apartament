'''Módulo com funções de leitura do teclado'''


def ler_string(msg, exept_msg="Inválido"):
    '''Função que lê uma string e a retorna já sem os espaços em branco.'''
    while True:
        palavra = input(msg).strip()
        if palavra.isidentifier():
            return palavra
        print(exept_msg + "\n")


def ler_inteiro(msg, exept_msg="Inválido"):
    '''Função que lê um inteiro e o retorna.'''
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print(exept_msg + "\n")


def ler_option(msg, max_opt, exept_msg="Opção inválida."):
    '''Função que lê opções, dado o parâmetro max_opt, e a retorna.'''
    while True:
        opt = ler_inteiro(msg, "Digite números")
        if 0 < opt <= max_opt:
            return opt
        print(f"\033[31m{exept_msg}\033[m\n")


def format_cpf(str_cpf):
    '''Formata o CPF para xxx.xxx.xxx-xx'''
    return f"{str_cpf[0:4]}.{str_cpf[3:6]}.{str_cpf[6:9]}-{str_cpf[9:]}"


def format_phone_number(phone_number):
    '''Formata o número de telefone para (DDD) 99999-9999'''
    return f"({phone_number[0:2]}) {phone_number[2:7]}-{phone_number[7:]}"


def show_array(array):
    '''Função que mostra um objeto na forma listada.'''
    for i, msg in enumerate(array, start=1):
        print(f"[ {i} ] {msg}")
