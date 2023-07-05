'''Validation module'''
from utils import uteis


def cpf(str_cpf):
    '''Transforma a string CPF para o formato xxx.xxx.xxx-xx'''
    return str_cpf[0:3] + "." + str_cpf[3:6] + "." + str_cpf[6:9] + "-" + str_cpf[9:11]


def apto(msg):
    '''Valida o número do apartamento'''
    while True:
        num_apto = uteis.ler_inteiro(msg, exept_msg="Digite um número")
        num_apto = str(num_apto)
        if len(num_apto) ==  1:
            num_apto = "00" + num_apto
        elif len(num_apto) == 2 or len(num_apto) > 3:
            print("\033[31mNúmero de apartamento inválido.\033[m\n")
            continue
        if not (num_apto[0] in ("0", "1", "2", "3") and num_apto[1] == "0" and num_apto[2] in ("1", "2", "3", "4")):
            print("\033[31mNúmero de apartamento inválido.\033[m\n")
            continue
        return num_apto
