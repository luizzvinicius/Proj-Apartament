'''Módulo de formatação de strings.'''


def format_cpf(str_cpf):
    '''Formata o CPF para xxx.xxx.xxx-xx'''
    return f"{str_cpf[0:4]}.{str_cpf[3:6]}.{str_cpf[6:9]}-{str_cpf[9:]}"


def format_phone_number(phone_number):
    '''Formata o número de telefone para (DDD) 99999-9999'''
    return f"({phone_number[0:2]}) {phone_number[2:7]}-{phone_number[7:]}"
