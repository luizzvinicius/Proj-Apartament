'''Módulo com funções muito usadas no projeto'''
import dotenv
import datetime
import vehicle
import person
from utils import uteis, validation


dotenv.load_dotenv(verbose=True, override=True)
last_bloco = int(dotenv.get_key(".env", "last_bloco"))


def main():
    '''Função que executa o programa de fato.'''
    
    apartament = apartament_register()
    # owner = person.person_register(owner=True)

    # msg = "Quantas pessoas vão morar no apartamento? "
    # people_in_apartament = uteis.ler_option(msg, max_opt=4, exept_msg="Quantidade inválida. Máximo 4")
    # people = {}
    # for i in range(1, people_in_apartament+1):
    #     print(f"\n{i}º Morador")
    #     people.setdefault(f"person{i}", person.person_register())

    # print("Você possui veículo?\n[ 1 ] Sim\n[ 2 ] Não")
    # opt = uteis.ler_option("Digite o número: ", max_opt=2)
    
    # if opt == 1:
    #     print("\nQual categoria?\n[ 1 ] Carro\n[ 2 ] Moto")
    #     category = uteis.ler_option("Digite o número: ", max_opt=2, exept_msg="Categoria inválida.")
    #     automobile = vehicle.register(opt, category)
    # else:
    #     automobile = vehicle.register(opt)

    # if opt == 1: # provisório
    #     print(f"Qual alteração você quer fazer no(a) {automobile['categoria']}?\n[ 1 ] Adicionar observação\n[ 2 ] Alterar cor")
    #     modification = uteis.ler_option("Digite o número: ", max_opt=2)
    #     automobile = vehicle.alter(automobile, modification)
    #     print(automobile)
    #     automobile = vehicle.delete()
    
    # print(automobile)
    # print(owner)
    # print(people)
    print(apartament)


def apartament_register():
    '''Função que cria a numeração do apartamento.'''
    bloco = uteis.ler_option("Bloco: ", max_opt=last_bloco, exept_msg="Número de bloco inválido.")
    bloco = "0" + str(bloco) if bloco < 10 else str(bloco)

    num_apto = 0
    while True:
        num_apto = uteis.ler_inteiro("Número do apartamento: ")
        num_apto = str(num_apto)
        if len(num_apto) == 1:
            num_apto = "00" + num_apto

        if validation.apto(num_apto) is True:
            break

    return {"bloco": bloco, "apartamento": num_apto, "Banco de dados": bloco + num_apto}


main()
