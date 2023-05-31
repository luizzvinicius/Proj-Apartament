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
        try:
            num = input(msg)
            return int(num)
        except ValueError:
            print(exeptMsg + "\n")
        continue


def lerFloat(msg, exeptMsg="Inválido"):
    while True:
        try:
            num = input(msg).replace(",",".")
            return float(num)
        except ValueError:
            print(exeptMsg + "\n")
        continue


def lerOption(msg, range):
    while True:
        opt = lerInteiro(msg, "Digite um número")
        if opt < int(range[0]) or opt > int(range[2:]):
            print("\033[31mOpção inválida.\033[m" + "\n")
            continue
        break
    return opt
