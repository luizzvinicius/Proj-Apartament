'''Módulo com funções de leitura do teclado'''
def ler_string(msg, exept_msg="Inválido"):
    '''Função que lê uma string e a retorna capitalizada'''
    while True:
        palavra = input(msg).strip()
        if palavra.isidentifier():
            return palavra.capitalize()
        print(exept_msg + "\n")


def ler_inteiro(msg, exept_msg="Inválido"):
    '''Função que lê um inteiro e o retorna'''
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print(exept_msg + "\n")


def ler_float(msg, exept_msg="Inválido"):
    '''Função que lê um float e o retorna'''
    while True:
        try:
            num = input(msg).replace(",", ".")
            return float(num)
        except ValueError:
            print(exept_msg + "\n")


def ler_option(msg, max_opt, exept_msg="Opção inválida."):
    '''Função que lê opções, dado o parâmetro max_opt, e a retorna'''
    while True:
        opt = ler_inteiro(msg, "Digite um número")
        if opt < 1 or opt > max_opt:
            print(f"\033[31m{exept_msg}\033[m\n")
            continue
        return opt
