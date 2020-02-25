# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала.'
    def stop(self):
        return f'{self.name} остановилась.'
    def turn(self, direction):
        return f'{self.name} повернула {direction}.'
    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed}.'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} превышает допустимую скорость на {self.speed - 60}.'
        else:
            return f'{self.name} едет со скоростью {self.speed}.'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} превышает допустимую скорость на {self.speed - 40}.'
        else:
            return f'{self.name} едет со скоростью {self.speed}.'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car_1 = TownCar(60, 'Баклажан', 'Лада 2106', False)
print(town_car_1.color)
print(town_car_1.go())
print(town_car_1.show_speed())
print(town_car_1.turn('враво'))
print(town_car_1.turn('влево'))
print(town_car_1.stop())
