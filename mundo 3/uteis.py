def lerString(msg, exeptMsg="Inválido"):
    while True:
        palavra = input(msg)
        if not palavra.isidentifier():
            print(exeptMsg + "\n")
            continue
        break
    return palavra

def lerInteiro(msg, exeptMsg="Inválido"):
    while True:
        num = input(msg)
        if not num.isdecimal():
            print(exeptMsg + "\n")
            continue
        break
    return int(num)

def lerFloat(msg, exeptMsg="Inválido"):
    while True:
        num = input(msg)
        if not num.isdigit():
            print(exeptMsg + "\n")
            continue
        break
    return float(num)

def lerOption(msg, range):
    while True:
        opt = lerInteiro(msg, "Digite um número")
        if opt < int(range[0]) or opt > int(range[2:]):
            print("Opção inválida" + "\n")
            continue
        break
    return opt
