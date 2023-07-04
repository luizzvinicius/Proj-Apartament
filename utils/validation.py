'''Validation module'''
def cpf(str_cpf):
    '''Transforma a string CPF para o formato xxx.xxx.xxx-xx'''
    return str_cpf[0:3] + "." + str_cpf[3:6] + "." + str_cpf[6:9] + "-" + str_cpf[9:11]
