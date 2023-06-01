def lerString(msg, exeptMsg="Inválido"):
    while True:
        palavra = input(msg).strip()
        if palavra.isidentifier():
            return palavra.capitalize()
        print(exeptMsg + "\n")


def lerInteiro(msg, exeptMsg="Inválido"):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print(exeptMsg + "\n")


def lerFloat(msg, exeptMsg="Inválido"):
    while True:
        try:
            num = input(msg).replace(",", ".")
            return float(num)
        except ValueError:
            print(exeptMsg + "\n")


def lerOption(msg, max):
    while True:
        opt = lerInteiro(msg, "Digite um número")
        if opt < 1 or opt > max:
            print("\033[31mOpção inválida.\033[m\n")
            continue
        return opt
