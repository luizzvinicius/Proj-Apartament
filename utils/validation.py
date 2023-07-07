'''Validation module'''
import re


def cpf(str_cpf):
    '''Transforma a string CPF para o formato xxx.xxx.xxx-xx'''
    if len(str_cpf) == 11:
        return str_cpf[0:3] + "." + str_cpf[3:6] + "." + str_cpf[6:9] + "-" + str_cpf[9:11]
    return False


def apto(num_apto):
    '''Valida o número do apartamento'''
    num_apto = str(num_apto)
    if len(num_apto) == 1:
        num_apto = "00" + num_apto
    elif len(num_apto) == 2 or len(num_apto) > 3:
        print("\033[31mNúmero de apartamento inválido.\033[m\n")
        return False
    if not (num_apto[0] in ("0", "1", "2", "3") and num_apto[1] == "0" and num_apto[2] in ("1", "2", "3", "4")):
        print("\033[31mNúmero de apartamento inválido.\033[m\n")
        return False
    return True


def placa(str_palca):
    '''Valida se a placa do carro obedece o padrão normal ou mercosul'''
    if re.match(r"^[a-z]{3}\d{1}[a-z0-9]{1}\d{2}$", str_palca):
        return True
    return False


def name(str_nome):
    '''Valida uma string permitindo apenas letras, acentos e espaços'''
    if re.match(r"^[a-zA-ZÀ-ÿ\s]+$", str_nome):
        return True
    return False
