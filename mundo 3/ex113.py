n1 = int(input("Digite um número: "))

while True:
    try:
        n2 = int(input("Digite um número: "))
        if n2 == 0:
            raise ZeroDivisionError("Não pode ser 0\n")
        break
    except ZeroDivisionError as erro:
        print(erro)

print(f"Divisão entre {n1} e {n2} é {n1/n2 :.1f}")
