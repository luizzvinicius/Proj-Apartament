propertyPrice = float(input("Valor do bem a ser financiado: "))
salary = float(input("Qual seu salário? "))
time = int(input("Em quantos anos quer pagar? "))

if (parcel := propertyPrice / (time * 12)) <= salary * 0.3:
    print("\nVocê foi aprovado!")
    print(f"Serão {time * 12} parcelas no valor de R${parcel :.2f}")
else:
    print("\nInfelizmente você não foi aprovado")
