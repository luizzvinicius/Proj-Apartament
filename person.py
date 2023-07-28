class Person:
    '''Classe que cria o proprietátio e moradores do apartamento.'''

    def __init__(self, name, cpf, phone, register_date):
        self.__name = name
        self.__cpf = cpf
        self.__phone = phone
        self.__register_date = register_date

    def to_string(self):
        name = self.__name
        cpf = self.__cpf
        phone = self.__phone
        date = self.__register_date
        return f"Person: [CPF: {cpf}, nome: {name}, telefone: {phone}, register_date: {date}]"

    def get_cpf(self):
        return self.__cpf

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_date(self):
        return self.__register_date
