class Vehicle:
    def __init__(self, placa, category, color, model, obs, date):
        self.__placa = placa
        self.__category = category
        self.__color = color
        self.__model = model
        self.__obs = obs
        self.__date = date

    def to_string(self):
        placa = self.__placa
        cat = self.__category
        color = self.__color
        model = self.__model
        obs = self.__obs
        data = self.__date
        return f"Veículo: [placa: {placa}, cat: {cat}, color: {color}, model: {model}, obs: {obs}, data: {data}]"

    def get_placa(self):
        return self.__placa

    def get_category(self):
        return self.__category

    def get_color(self):
        return self.__color

    def get_model(self):
        return self.__model

    def get_obs(self):
        return self.__obs

    def get_date(self):
        return self.__date
