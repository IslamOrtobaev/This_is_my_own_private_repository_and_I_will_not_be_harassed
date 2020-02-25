# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length = None
    _width = None
    mass_per_meter = 25
    thickness = 5
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculate(self):
        asphalt_mass = (self._length * self._width * self.mass_per_meter * self.thickness) // 1000
        print(f'{self._length}м*{self._width}м*{self.mass_per_meter}кг*{self.thickness}см = {asphalt_mass}т')

road = Road(5000, 20)
road.mass_calculate()