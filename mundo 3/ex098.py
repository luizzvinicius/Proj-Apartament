from time import sleep


def contador():
    """
        Função sem parâmetros e sem retorno que personaliza a função range
    """
    print("Personalize seu contador!")
    start = int(input("Digite o início: "))
    
    print("Digite o fim:", end="")
    end = int(input("{:^4}".format("")))
    
    print("Digite o passo:", end="")
    step = int(input("{:^2}".format("")))

    if start > end:
        if step == 0:
            step = -1
        elif step > 0:
            step = -step
    print("\nContador:", end=" ")
    for i in range(start, end, step):
        print(i, end=" ", flush=True)
        sleep(0.5)

help(contador)
contador()
