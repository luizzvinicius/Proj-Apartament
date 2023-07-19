class Vehicle:
    def __init__(self, placa, categoria, cor, modelo, observacao, data_cadastro):
        self.placa = placa
        self.categoria = categoria
        self.cor = cor
        self.modelo = modelo
        self.observacao = observacao
        self.data_cadastro = data_cadastro

    def to_string(self):
        placa = self.placa
        cat = self.categoria
        cor = self.cor
        modelo = self.modelo
        obs = self.observacao
        data = self.data_cadastro
        return f"Veículo: [placa: {placa}, cat: {cat}, cor: {cor}, modelo: {modelo}, obs: {obs}, data: {data}]"

    def get_placa(self):
        return self.placa

    def get_categoria(self):
        return self.categoria

    def get_cor(self):
        return self.cor

    def set_cor(self, cor):
        self.cor = cor

    def get_modelo(self):
        return self.modelo

    def get_observacao(self):
        return self.observacao

    def set_observacao(self, observacao):
        self.observacao = observacao

    def get_data(self):
        return self.data_cadastro
