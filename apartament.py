class Apartament:
    """Classe apartamento"""

    def __init__(self, numero, data_cadastro):
        self.numero = numero
        self.data_cadastro = data_cadastro

    def to_string(self):
        '''Retorna todas as informações do apartamento.'''
        return f"Apartamento: [número: {self.numero}, data_cadastro: {self.data_cadastro}]"

    def get_numero(self):
        return self.numero
