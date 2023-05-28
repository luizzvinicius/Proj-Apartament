from random import randint

print("Par ou ímpar")

ladoJogador, nJogador, nComputador, wins = 0, 0, 0, 0
while True:
    while ladoJogador not in (1, 2):
        print("[ 1 ] Par\n[ 2 ] Ímpar")
        ladoJogador = int(input("Você escolhe par ou ímpar? "))
        print()
    print("Você escolheu", "par." if ladoJogador == 1 else "ímpar.")

    nJogador = int(input("Número entre 0 e 10: "))
    nComputador = randint(0, 10)
    print(f"\nVocê escolheu {nJogador}\nO computador escolheu {nComputador}\n")
    
    if ladoJogador == 1 and (nJogador + nComputador) % 2 == 1:
        break
    if ladoJogador == 2 and (nJogador + nComputador) % 2 == 0:
        break

    print("Você ganhou")
    wins += 1
    ladoJogador = 0

print(f"Você ganhou {wins} vezes.")
print(f"Você perdeu porque deu {nJogador + nComputador}")
