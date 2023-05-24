dias = int(input("Quantos dias rodados? "))
quilometragem = int(input("Quantos Km rodados? "))

print(f"O aluguel fica R${0.15 * quilometragem + 60 * dias :.2f}")
