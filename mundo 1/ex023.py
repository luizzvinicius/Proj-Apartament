num = input("Digite um número: ")

if len(num) < 4:
    num = num.zfill(4)

print(f"Unidade: {num[3]}")
print(f"Dezena: {num[2]}")
print(f"Centena: {num[1]}")
print(f"Milhar: {num[0]}")
