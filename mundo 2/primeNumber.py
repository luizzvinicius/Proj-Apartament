num = int(input("Digite um número: "))
divided = 0

if num in (1, 2, 3):
    print("primo")
else:
    for i in range(2, num):
        if num % i == 0:
            divided += 1
            print("não primo")
            break
    if divided == 0: print("primo")
