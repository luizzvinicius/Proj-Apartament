'''Módulo de formatação de strings.'''


def cpf(str_cpf):
    '''Formata o CPF para xxx.xxx.xxx-xx'''
    return f"{str_cpf[0:4]}.{str_cpf[3:6]}.{str_cpf[6:9]}-{str_cpf[9:]}"


def phone_number(number):
    '''Formata o número de telefone para "(DDD) 99999-9999"'''
    return f"({number[0:2]}) {number[2:7]}-{number[7:]}"


def show_array(array):
    '''Função que mostra um objeto na forma listada.'''
    for i, msg in enumerate(array, start=1):
        print(f"[ {i} ] {msg}")
