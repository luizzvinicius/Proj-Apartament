'''Módulo com funções muito usadas no projeto'''
from datetime import date
import dotenv
from utils import formatting
from utils import reader, validation
from connection_pool import Connection
from apartament import Apartament
from vehicle import Vehicle
from person import Person
from Dao.apartamentDao import ApartamentDao
from Dao.personDao import PersonDao
from Dao.ownerDao import OwnerDao
from Dao.vehicleDao import VehicleDao


dotenv.load_dotenv(verbose=True, override=True)
last_bloco = int(dotenv.get_key(".env", "last_bloco"))

day = date.today()

opt_msg = (
    'Cadastrar apartamento',
    'Cadastrar morador',
    'Cadastrar veículo',
    'Editar cor/observação do veículo',
    'Deletar proprietário e apartamento',
    'Deletar morador do apartamento',
    'Deletar veículo do apartamento',
    'Consultas',
    'Encerrar'
)
query_msg = (
    'Consultar apartamento (mostrar tudo)',
    'Consultar proprietário (CPF)',
    'Consultar morador (nº apartamento)',
    'Consultar veículo (placa)'
)


def main(option_msg, queries_msg):
    '''Função que recebe as mensagens e executa o programa de fato.'''
    print("-=" * 30)
    print(f"{'Portaria do condomínio' :^55}")
    print("-=" * 30)

    while True:
        formatting.show_array(opt_msg)
        choice = reader.read_option("Sua escolha: ", max_opt=len(option_msg)) - 1

        if choice == 0:
            # cadastrar apartamento
            owner = person_register(owner=True)
            apartament = apartament_register()
            people = apartament_residents()

            OwnerDao().insert(owner)
            ApartamentDao().insert(apartament, owner.get_cpf())
            for person in people:
                PersonDao().insert(person, apartament.get_number())

            print("Você possui veículo?\n[ 1 ] Sim\n[ 2 ] Não")
            opt = reader.read_option("Digite o número: ", max_opt=2)
            if opt == 1:
                print("\nQual categoria?\n[ 1 ] Carro\n[ 2 ] Moto")
                category = reader.read_option("Digite o número: ", max_opt=2, exept_msg="Categoria inválida.")
                automobile = vehicle_register(category)
                VehicleDao().insert(automobile, apartament.get_number())

        if choice == 1:
            #   cadastrar morador
            num_apt = read_num_apt()
            res = PersonDao().select(num_apt)
            if len(res) == 0:
                print("Apartamento não cadastrado.")
            elif len(res) == 4:
                print("Limite máximo de moradores por apartamento atingido.")
            else:
                person = person_register()
                PersonDao().insert(person, num_apt)

        if choice == 2:
            # cadastrar veículo
            placa = read_placa()
            res = VehicleDao().select(placa)
            if len(res) == 4:
                print("Limite máximo de veículos por apartamento atingido.")
            else:
                num_apt = read_num_apt()
                print("\nQual categoria?\n[ 1 ] Carro\n[ 2 ] Moto")
                category = reader.read_option("Digite o número: ", max_opt=2, exept_msg="Categoria inválida.")
                automobile = vehicle_register(category)
                VehicleDao().insert(automobile, num_apt)

        if choice == 3:
            # editar cor/observação
            placa = read_placa()
            res = VehicleDao().select(placa)
            if len(res) == 0:
                print("Veículo não cadastrado.")
            else:
                print("\nQual campo?\n[ 1 ] Cor\n[ 2 ] Observação")
                opt = reader.read_option("Digite o número: ", max_opt=2, exept_msg="Campo inválido.")
                field = "cor" if opt == 1 else "observacao"
                new_value = input(f"Digite a nova {field}: ").strip().lower()
                VehicleDao().update(field, new_value, placa)

        if choice == 4:
            # deletar proprietário
            cpf = reader.read_eleven_digits("CPF")
            OwnerDao().delete(cpf)

        if choice == 5:
            # deletar morador
            num_apt = read_num_apt()
            res = PersonDao().select(num_apt)
            formatting.show_array(res)
            opt = reader.read_option("Qual morador: ", max_opt=len(res)) - 1
            # terminar

        if choice == 6:
            # deletar veículo
            placa = read_placa()
            VehicleDao().delete(placa)
            # terminar

        if choice == 7:
            print()
            formatting.show_array(queries_msg)
            n_consulta = reader.read_option("Sua escolha: ", max_opt=len(queries_msg)) - 1

            if n_consulta == 0:
                cpf = reader.read_eleven_digits("CPF")
                res = ApartamentDao().select(cpf)
                formatting.show_apartament(res)

            if n_consulta == 1:
                cpf = reader.read_eleven_digits("CPF")
                res = OwnerDao().select(cpf)
                formatting.show_person(res)

            if n_consulta == 2:
                num_apt = read_num_apt()
                people = PersonDao().select(num_apt)
                formatting.show_person(people)

            if n_consulta == 3:
                placa = read_placa()
                res = VehicleDao().select(placa)
                if len(res) == 0:
                    print("Não há veículos com essa placa.\n")
                else:
                    formatting.show_vehicle(res)

        if choice == 8:
            Connection.close_conn()
            break
    print("\nPortaria encerrada.")


def read_num_apt():
    bloco = reader.read_option("Bloco: ", max_opt=last_bloco, exept_msg="Número de bloco inválido.")
    bloco = "0" + str(bloco) if bloco < 10 else str(bloco)

    num_apt = 0
    while True:
        num_apt = reader.read_int("Número do apartamento: ")
        num_apt = str(num_apt)
        if len(num_apt) == 1:
            num_apt = "00" + num_apt
        if validation.apt(num_apt) is True:
            break
    return bloco + num_apt


def apartament_register():
    '''Função que cria a numeração do apartamento.'''
    num_apt = read_num_apt()
    return Apartament(num_apt, day)


def apartament_residents():
    '''Registra moradores do apartamento'''
    msg = "Quantas pessoas vão morar no apartamento? "
    people_in_apartament = reader.read_option(msg, max_opt=4, exept_msg="Quantidade inválida. Mínimo 1, máximo 4.")

    people = []
    for i in range(1, people_in_apartament+1):
        print(f"\n{i}º Morador")
        person = person_register()
        people.append(person)

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

    cpf = reader.read_eleven_digits("CPF")
    phone = reader.read_eleven_digits("Telefone")

    return Person(name, cpf, phone, day)


def read_placa():
    while True:
        placa = input("Qual a placa do(a) veículo: ").strip().lower()
        if validation.placa(placa) is True:
            return placa
        print("Placa inválida.\n")


def vehicle_register(category):
    '''Função que registra o veículo do apartamento.'''
    category = "carro" if category == 1 else "moto"

    placa = read_placa()
    color = reader.read_string(f"Qual a cor do(a) {category}: ")
    model = reader.read_string(f"Qual o modelo do(a) {category}: ")

    return Vehicle(placa, category, color, model, "Nenhuma observação", day)


main(opt_msg, query_msg)
