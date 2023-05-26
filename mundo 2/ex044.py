total = float(input("Valor da compra: "))
print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista dinheiro")
print("[ 2 ] à vista cartão")
print("[ 3 ] 2x cartão")
print("[ 4 ] 3x ou mais cartão")
opt = int(input("Esolha: "))

if opt == 1:
    print(f"Ganhou desconto de 10%. Total de {total * 0.90}")
elif opt == 2:
    print(f"Ganhou desconto de 5%. Total de {total * 0.95}")
elif opt == 3:
    print(f"Serão 2 parcelas de R${total / 2 :.2f}. Total de {total :.2f}")
elif opt == 4:
    parcelas = int(input("Quantas parcelas? "))
    print(f"Juros de 20%. Serão {parcelas} parcelas de R${total * 1.2 / parcelas :.2f}. Total de {total * 1.2 :.2f}")
else:
    print("Opção inválida")
