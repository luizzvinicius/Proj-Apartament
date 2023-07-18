'''Módulo com funções muito usadas no projeto'''
import dotenv
import datetime
import apartament
import vehicle
import person
from utils import uteis, validation


dotenv.load_dotenv(verbose=True, override=True)
last_bloco = int(dotenv.get_key(".env", "last_bloco"))

opt_msg = (
    'Cadastrar apartamento',
    'Editar proprietário do apartamento',
    'Editar moradores do apartamento (cadastrar novamente)',
    'Editar cor/observação do veículo',
    'Deletar morador do apartamento',
    'Deletar veículo do apartamento',
    'Consultas',
    'Encerrar'
)
query_msg = (
    'Consultar apartamento (mostrar tudo)',
    'Consultar proprietário (CPF ou nome)',
    'Consultar morador (nº apartamento ou Nome)',
    'Consultar veículo (Placa ou modelo)'
)


def main(option_msg, queries_msg):
    '''Função que executa o programa de fato.'''
    print("-=" * 30)
    print(f"{'Portaria do condomínio' :^55}")
    print("-=" * 30)

    # passa o objeto para a classeDAO cadastrar
    while True:
        uteis.show_array(opt_msg)
        choice = uteis.ler_option("Sua escolha: ", max_opt=len(option_msg)) - 1

        match choice:
            case 0:
                num_apto = apartament_register()
                owner = person.person_register(owner=True)
                people = apartament_residents()

                print("Você possui veículo?\n[ 1 ] Sim\n[ 2 ] Não")
                opt = uteis.ler_option("Digite o número: ", max_opt=2)

                if opt == 1:
                    print("\nQual categoria?\n[ 1 ] Carro\n[ 2 ] Moto")
                    category = uteis.ler_option(
                        "Digite o número: ", max_opt=2, exept_msg="Categoria inválida.")
                    automobile = vehicle.register(opt, category)
                else:
                    automobile = vehicle.register(opt)

                if opt == 1:
                    print(f"Qual alteração você quer fazer no(a) {automobile['categoria']}?\n[ 1 ] Adicionar observação\n[ 2 ] Alterar cor")
                    modification = uteis.ler_option("Digite o número: ", max_opt=2)
                    automobile = vehicle.alter(automobile, modification)
                    print(automobile)
                    automobile = vehicle.delete()

            # case 1:

            # case 2:

            # case 3:

            # case 4:

            # case 5:

            case 6:
                uteis.show_array(queries_msg)
                choice = uteis.ler_option("Sua escolha: ", max_opt=len(option_msg)) - 1
            case 7:
                break

    # print(automobile)
    # print(owner)
    # print(people)
    # print(apartament)
    print("Portaria encerrada.")


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
    return bloco + num_apto


def apartament_residents():
    msg = "Quantas pessoas vão morar no apartamento? "
    people_in_apartament = uteis.ler_option(msg, max_opt=4, exept_msg="Quantidade inválida. Máximo 4")
    
    people = {}
    for i in range(1, people_in_apartament+1):
        print(f"\n{i}º Morador")
        people.setdefault(f"person{i}", person.person_register())
    
    return people


main(opt_msg, query_msg)
