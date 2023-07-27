'''Validation module'''
import re


def apt(num_apt):
    '''Valida o número do apartamento'''
    if len(num_apt) == 2 or len(num_apt) > 3:
        print("\033[31mNúmero de apartamento inválido.\033[m\n")
        return False
    if not (num_apt[0] in ("0", "1", "2", "3") and num_apt[1] == "0" and num_apt[2] in ("1", "2", "3", "4")):
        print("\033[31mNúmero de apartamento inválido.\033[m\n")
        return False
    return True


def placa(str_palca):
    '''Valida se a placa do carro obedece o padrão normal ou mercosul'''
    if re.match(r"^[A-Za-z]{3}\d{1}[A-Za-z0-9]{1}\d{2}$", str_palca):
        return True
    return False


def name(person_name):
    '''Valida uma string permitindo apenas letras, acentos e espaços'''
    if len(person_name) < 3:
        return False
    for word in person_name:
        if not re.match(r"^[a-zA-ZÀ-ÿ\s]+$", word):
            return False
    return True
