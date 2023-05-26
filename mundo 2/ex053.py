frase = input("Digite a frase (sem acentos): ")
reverse = ""
for i in reversed(frase.replace(" ", "")):
    reverse += reverse.join(i)
print("É palíndromo" if frase.replace(" ", "") == reverse else "Não é palíndromo")
