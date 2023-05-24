# importante para a verificação de strings
nome = input("Digite uma palavra: ")

print(f"Tipo primitivo {type(nome)}")
print(f"É um número? {nome.isnumeric()}")
print(f"É apenas letra? {nome.isalpha()}")
print(f"É um número ou letra? {nome.isalnum()}")
print(f"Todos os caracteres são maiúsculos? {nome.isupper()}")
print(f"Todos os caracteres são minúsculos? {nome.islower()}")
