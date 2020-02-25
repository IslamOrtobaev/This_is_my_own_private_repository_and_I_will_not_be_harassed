# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Выбранный предмет для отрисовки: {self.title}.'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Выбранный предмет для отрисовки: {self.title}. Идёт отрисовка ручкой.'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Выбранный предмет для отрисовки: {self.title}. Идёт отрисовка карандашом.'


class Marker(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Выбранный предмет для отрисовки: {self.title}. Идёт отрисовка маркером.'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
marker = Marker('Маркер')
print(pen.draw())
print(pencil.draw())
print(marker.draw())

# Но ведь слово Handle как существительное значит - ручку/рукоять, а если глагол - упралять/справляться