from random import choice, shuffle
qtdAlunos = int(input("Quantos alunos? "))

alunos = []
for i in range(qtdAlunos):
    nome = input(f"Nome do {i+1} aluno: ")
    alunos.append(nome)

shuffle(alunos)
print(f"O aluno escolhido para apagar o quadro é {choice(alunos)}.")
print(f"A ordem de apresentação será: {alunos}.")
