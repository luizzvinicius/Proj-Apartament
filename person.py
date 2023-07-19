class Person:
    '''Classe que cria o proprietátio e moradores do apartamento.'''

    def __init__(self, info, data_cadastro):
        self.cpf = info['cpf']
        self.nome = info['name']
        self.telefone = info['telefone']
        self.data_cadastro = data_cadastro

    def to_string(self):
        return f"Person: [CPF: {self.cpf}, nome: {self.nome}, telefone: {self.telefone}, data_cadastro: {self.data_cadastro}]"

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_telefone(self):
        return self.telefone

    def set_telefone(self, telefone):
        self.telefone = telefone

    def get_data_cadastro(self):
        return self.data_cadastro
