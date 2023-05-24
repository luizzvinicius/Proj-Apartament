# formatar números para 3 casas decimais e no formato brasileiro

medida = float(input("Digite um valor em Km: "))
divisor = 10
for i in range(6):
    print(f"{i}: {medida * divisor :,.2f}".replace('_', "."))
    divisor *= 10
