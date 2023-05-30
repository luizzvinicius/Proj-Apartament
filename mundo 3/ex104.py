def leiaInt(msg):
    num = ""
    while True:
        num = input(msg)
        if num.isnumeric() is False:
            print("Digite um número inteiro!\n")
        else:
            break
    return int(num)


opt = leiaInt("Digite um número: ")
print(opt)
