'''Módulo com funções muito usadas no projeto'''
from datetime import date
import dotenv
from apartament import Apartament
from vehicle import Vehicle
from person import Person
from utils import uteis, validation


dotenv.load_dotenv(verbose=True, override=True)
last_bloco = int(dotenv.get_key(".env", "last_bloco"))

date = date.today()

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


def main(option_msg, queries_msg, date_register):
    '''Função que executa o programa de fato.'''
    print("-=" * 30)
    print(f"{'Portaria do condomínio' :^55}")
    print("-=" * 30)

    while True:
        uteis.show_array(opt_msg)
        choice = uteis.ler_option("Sua escolha: ", max_opt=len(option_msg)) - 1

        match choice:
            case 0:
                num_apto = apartament_register()
                owner = person_register(owner=True)
                people = apartament_residents()

                print("Você possui veículo?\n[ 1 ] Sim\n[ 2 ] Não")
                opt = uteis.ler_option("Digite o número: ", max_opt=2)
                automobile = None
                if opt == 1:
                    print("\nQual categoria?\n[ 1 ] Carro\n[ 2 ] Moto")
                    category = uteis.ler_option("Digite o número: ", max_opt=2, exept_msg="Categoria inválida.")
                    automobile = vehicle_register(category)

                apartamento = Apartament(num_apto, date_register)
                owner = Person(owner, date_register)

                print(apartamento.to_string())
                print(owner.to_string())
                for p in people:
                    print(p.to_string())
                if automobile is not None:
                    print(automobile.to_string())

            # case 1:

            # case 2:

            # case 3:

            # case 4:
            #     print(f"Qual alteração você quer fazer no(a) {automobile['categoria']}?")
            #     print("[ 1 ] Adicionar observação\n[ 2 ]Alterar cor")
            #     opt = uteis.ler_option("Digite o número: ", max_opt=2)
            #     automobile = vehicle.alter(automobile, opt)
            #     print(automobile)

            # case 5:
            #     automobile = vehicle.delete()
            #     print("Veículo apagado do sistema.")

            case 6:
                uteis.show_array(queries_msg)
                choice = uteis.ler_option("Sua escolha: ", max_opt=len(queries_msg)) - 1

            case 7:
                break
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
    '''Registra moradores do apartamento'''
    msg = "Quantas pessoas vão morar no apartamento? "
    people_in_apartament = uteis.ler_option(msg, max_opt=4, exept_msg="Quantidade inválida. Máximo 4")

    people = []
    for i in range(1, people_in_apartament+1):
        print(f"\n{i}º Morador")
        person = person_register()
        people.append(Person(person, date))

    return people


def person_register(owner=False):
    '''Função que registra as pessoas ou proprietário que moram no apartamento.'''
    msg = "Nome do proprietário do apartamento: " if owner else "Nome: "
    name = "1"
    while True:
        name = input(msg).strip().title().split(" ")
        if validation.name(name) is True:
            name = " ".join(name)
            break
        print("Formato de nome inválido.\n")

    cpf = uteis.ler_onze_digitos("CPF")
    phone_number = uteis.ler_onze_digitos("Telefone")

    return {"name": name, "cpf": cpf, "telefone": phone_number}


def vehicle_register(category):
    '''Função que registra o veículo do apartamento.'''
    category = "carro" if category == 1 else "moto"

    while True:
        placa = input(f"Qual a placa do(a) {category}: ").strip().lower()
        if validation.placa(placa) is True:
            break
        print("Placa inválida.\n")

    color = uteis.ler_string(f"Qual a cor do(a) {category}: ")
    model = uteis.ler_string(f"Qual o modelo do(a) {category}: ")

    return Vehicle(placa, category, color, model, "Nenhuma observação", date.today())


"""
DAO Vehicle
def alter(option, new_info):
    '''Recebe opção (1- observation; 2- color) e nova informação.\nRealiza alteração.'''
    match option:
        case 1:
            self.observacao = new_info
        case 2:
            self.cor = new_info
        case _:
            print("Indefinido.")


def delete():
    '''Define todas as informações do carro para None.'''
    return {"categoria": None, "placa": None, "cor": None, "modelo": None, "data": None, "observação": None}
"""


main(opt_msg, query_msg, date)
