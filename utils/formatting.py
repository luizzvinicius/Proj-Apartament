'''Módulo de formatação de strings.'''


def cpf(str_cpf):
    '''Formata o CPF para xxx.xxx.xxx-xx'''
    return f"{str_cpf[0:4]}.{str_cpf[3:6]}.{str_cpf[6:9]}-{str_cpf[9:]}"


def phone_number(number):
    '''Formata o número de telefone para "(DDD) 99999-9999"'''
    return f"({number[0:2]}) {number[2:7]}-{number[7:]}"


def split_num_apt(num):
    return f"Bloco {num[0:2]} Número {num[2:]}"


def date(str_date):
    return str_date.strftime("%d/%m/%Y")


def show_array(array):
    '''Função que mostra um objeto na forma listada.'''
    for i, msg in enumerate(array, start=1):
        print(f"[ {i} ] {msg}")


def show_apartament(obj):
    num_apt = split_num_apt(obj['apartamento'][0][0])
    print(f"\nProprietário do apartamento {num_apt}.")
    show_person(obj['proprietario'])

    print(f"\nMoradores do apartamento {num_apt}.")
    show_person(obj['moradores'])

    if len(obj['veiculo']) != 0:
        show_vehicle(obj['veiculo'])


def show_person(obj):
    for i in obj:
        print(f"\t{i[1]}")
        print(f"\tCPF: {cpf(i[0])}")
        print(f"\tTelefone: {phone_number(i[2])}")
        print(f"\tData de cadastro: {date(i[3])}\n")


def show_vehicle(obj):
    print("\nVeículos do apartamento.")
    for i in obj:
        print(f"\tPlaca: {i[0]}")
        print(f"\tCategoria: {i[1]}")
        print(f"\tCor: {i[2]}")
        print(f"\tModelo: {i[3]}")
        print(f"\tData de cadastro: {date(i[6])}")
        print(f"\tObservação: {i[4]}\n")
