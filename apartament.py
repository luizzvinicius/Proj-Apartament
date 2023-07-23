class Apartament:
    """Classe apartamento"""

    def __init__(self, numero, data_cadastro):
        self.__numero = numero
        self.__data_cadastro = data_cadastro

    def to_string(self):
        '''Retorna todas as informações do apartamento.'''
        return f"Apartamento: [número: {self.__numero}, data_cadastro: {self.__data_cadastro}]"

    def get_numero(self):
        return self.__numero

    def get_data(self):
        return self.__data_cadastro
