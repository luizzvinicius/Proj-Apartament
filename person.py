class Person:
    '''Classe que cria o proprietátio e moradores do apartamento.'''

    def __init__(self, info, data_cadastro):
        self.__cpf = info['cpf']
        self.__nome = info['name']
        self.__telefone = info['telefone']
        self.__data_cadastro = data_cadastro

    def to_string(self):
        cpf = self.__cpf
        nome = self.__nome
        tel = self.__telefone
        data = self.__data_cadastro
        return f"Person: [CPF: {cpf}, nome: {nome}, telefone: {tel}, data_cadastro: {data}]"

    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone

    def get_data_cadastro(self):
        return self.__data_cadastro
