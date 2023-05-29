print("Caixa eletrônico")
# 4.399999852466863e-06

valor = int(input("Qual valor você quer sacar? R$"))
ced100, ced50, ced20, ced10 = 0, 0, 0, 0
while True:
    if valor >= 100:
        valor -= 100
        ced100 += 1
        continue
    if valor >= 50:
        valor -= 50
        ced50 += 1
        continue
    if valor >= 20:
        valor -= 20
        ced20 += 1
        continue
    if valor >= 10:
        valor -= 10
        ced10 += 1
        continue
    break

print(f"{ced100} cédulas de 100")
print(f"{ced50} cédulas de 50")
print(f"{ced20} cédulas de 20")
print(f"{ced10} cédulas de 10")
