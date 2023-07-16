from datetime import date as d
from utils import validation

def person_register(owner=False):
    '''Função que registra as pessoas ou proprietário que moram no apartamento.'''
    msg = "Nome do proprietário do apartamento: " if owner else "Nome: "
    name = "1"
    while True:
        name = input(msg).strip().title().split(" ")
        if validation.name(name) is True:
            name = " ".join(name)
            break
        print("Formato de nome inválido.\n")

    cpf = 0
    while True:
        try:
            cpf = input("CPF (no formato xxx.xxx.xxx-xx): ").strip()
            if validation.cpf(cpf) is True:
                break
            raise ValueError("\033[31mFormato inválido.\033[m\n")
        except ValueError as expt:
            print(expt)
    
    phone_number = "1"
    msg = "Seu número de telefone (com DDD, 9 inicial, sem parênteses e espaço): "
    while True:
        phone_number = input(msg).strip()
        if validation.phone_number(phone_number) is True:
            phone_number = f"({phone_number[0:2]}) {phone_number[2:7]}-{phone_number[7:]}"
            break
        print("Telefone inválido.\n")

    return {"name": name, "cpf": cpf, "telefone": phone_number, "data": d.today()}