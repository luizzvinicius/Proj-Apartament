# Arquivo para testar velocidade do código
'''
    Falta fazer:
    mostrar res select
    Criar testes
    arrumar linguagem
    
'''
# from person import Person
# from Dao.ownerDao import OwnerDao

# p = Person('Marina oliveira tenorio', '25032142049', '82984227890', '2023-07-06')
# p1 = Person('Marina oliveira tenorio', '25032142050', '82984227890', '2023-07-06')
# p2 = Person('Marina oliveira tenorio', '25032142051', '82984227890', '2023-07-06')
# p3 = Person('Marina oliveira tenorio', '25032142052', '82984227890', '2023-07-06')
# p4 = Person('Marina oliveira tenorio', '25032142053', '82984227890', '2023-07-06')
# p5 = Person('Marina oliveira tenorio', '25032142054', '82984227890', '2023-07-06')


# OwnerDao().insert(p)
# OwnerDao().insert(p1)
# OwnerDao().insert(p2)
# OwnerDao().insert(p3)
# OwnerDao().insert(p4)
# OwnerDao().insert(p5)

obj = {'proprietario': [('72945524449', 'Marcelo Luiz Da Silva', '82991165644', '2023, 7, 27')], 
       'apartamento': [('02203', '2023, 7, 27')], 
       'veiculo': [('muv1122', 'carro', 'branca', 'ranger', 'íra voltar em 5 dias', '02203', '2023, 7, 27')], 
       'moradores': [
                    ('72945524449', 'Marcelo Luiz Da Silva','82991165644', '2023, 7, 27', '02203'),
                    ('87036258420', 'Danielle De Siqueira Costa','82991165644', '2023, 7, 27', '02203'),
                    ('11776422473', 'Luiz Vinicius Márdelle', '82993422157', '2023, 7, 27', '02203')
                    ]}
print(obj['proprietario'][0][1])
