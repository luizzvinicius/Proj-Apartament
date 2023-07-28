class Apartament:
    """Classe apartamento"""

    def __init__(self, number, register_date):
        self.__number = number
        self.__register_date = register_date

    def to_string(self):
        '''Retorna todas as informações do apartamento.'''
        return f"Apartamento: [número: {self.__number}, data_cadastro: {self.__register_date}]"

    def get_number(self):
        return self.__number

    def get_date(self):
        return self.__register_date
