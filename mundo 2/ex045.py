import random; import time

itens = ('pedra', 'papel', 'tesoura')
print("Suas opções:\n[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura")
userChoice = int(input("Qual sua jogada? "))
compChoice = random.randint(1, 3)

resultado = "ganhou"
if userChoice == compChoice:
    resultado = "empatou"
elif (userChoice == 1 and compChoice == 2) or (userChoice == 2 and compChoice == 3) or (userChoice == 3 and compChoice == 1):
    resultado = "perdeu"

print("Jo")
time.sleep(1)
print("Ken")
time.sleep(1)
print("Po")
print("=-" * 15)
print(f"Sua escolha foi {itens[userChoice-1]}")
print(f"Escolha do computador foi {itens[compChoice-1]}")
print("=-" * 15)
print(f"Você {resultado}")
