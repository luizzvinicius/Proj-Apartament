num = int(input("Digite um número para saber o seu fatorial: "))

fat = 1
while num >= 2:
    fat *= num
    num -= 1

print(fat)
