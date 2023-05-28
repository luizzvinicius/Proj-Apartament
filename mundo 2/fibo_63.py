qtdTermos = int(input("Quantos termos para mostrar? "))

c, n0, n3 = 0, 0, 0
n1 = 1
while c < qtdTermos:
    print(n3, end=" ")
    n3 = n0 + n1
    n0 = n1
    n1 = n3
    c += 1
