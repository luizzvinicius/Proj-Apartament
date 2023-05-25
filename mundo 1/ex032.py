import calendar; import datetime
# Expressão: ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0

ano = int(input("Digite um ano (0 para analisar o ano atual): "))
if ano == 0:
    ano = datetime.date.today().year

print(f"{ano} é bissexto" if calendar.isleap(ano) is True else f"{ano} não é bissexto")
