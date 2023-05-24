# formatando para ficar ocupando dois espaços
num = int(input("Digite um valor para a tabuada: "))

print("============")
for i in range(1, 11):
    print(f"{num} x {i :2} = {num*i :2}")
print("============")
