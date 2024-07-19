class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white', 'Purple', 'ORANGE'] # Текущие цвета

    def __init__(self, owner:str , model:str, color:str, e_p:str):
        self.owner = owner     # владелец транспорта.(владелец может меняться)
        self.__model = model  # модель(марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = e_p # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self._color = color #  название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_owner(self):
        return f'Владелец: {self.owner}'

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self._color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\n{self.get_owner()}')

    def set_color(self, new_color:str):
        help_list = []
        for farbe in self.__COLOR_VARIANTS:
            help_list.append(farbe.upper())
        if new_color not in help_list:
            print(f'Нельзя сменить цвет на {new_color}')
        else:
            self._color = new_color


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()