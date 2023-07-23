class Vehicle:
    def __init__(self, placa, categoria, cor, modelo, observacao, data_cadastro):
        self.__placa = placa
        self.__categoria = categoria
        self.__cor = cor
        self.__modelo = modelo
        self.__observacao = observacao
        self.__data_cadastro = data_cadastro

    def to_string(self):
        placa = self.__placa
        cat = self.__categoria
        cor = self.__cor
        modelo = self.__modelo
        obs = self.__observacao
        data = self.__data_cadastro
        return f"Veículo: [placa: {placa}, cat: {cat}, cor: {cor}, modelo: {modelo}, obs: {obs}, data: {data}]"

    def get_placa(self):
        return self.__placa

    def get_categoria(self):
        return self.__categoria

    def get_cor(self):
        return self.__cor

    def get_modelo(self):
        return self.__modelo

    def get_observacao(self):
        return self.__observacao

    def get_data(self):
        return self.__data_cadastro
