num = int(input("Número para conversão: "))
print("[ 1 ] Binário")
print("[ 2 ] Octal")
print("[ 3 ] Hexadecimal")
escolha = int(input("Escolha a base: "))

if escolha == 1:
    print(f"{num} convertido em binário é: {bin(num)[2:]}")
elif escolha == 2:
    print(f"{num} convertido em octal é: {oct(num)[2:]}")
elif escolha == 3:
    print(f"{num} convertido em hexadecimal é: {hex(num)[2:]}")
else:
    print("Escolha inválida")
