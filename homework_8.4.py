# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class OfficeEquipmentStorage:
    def __init__(self, number):
        self.number = int(number)

class OfficeEquipment:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._loading()

    def _loading(self):
        print(f'{self.brand} {self.model} is loading...')

class Printer(OfficeEquipment):

    def printing(self):
        print('Printer is printing...')

class Scanner(OfficeEquipment):

    def scanning(self):
        print('Scanner is scanning...')

class Copier(OfficeEquipment):

    def copying(self):
        print('Copier is copying...')

p = Printer('HP', '1020')
p.printing()
s = Scanner('Canon', 'Lide 300')
s.scanning()
c = Copier('HP', 'DeskJet 2130')
c.copying()