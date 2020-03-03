# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

class OfficeEquipmentStorage:

    def __init__(self, name, brand, model, price, quantity):
        self.brand = brand
        self.model = model
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.my_unit = {'Наименование: ': self.name,
                        'Бренд устройства: ': self.brand,
                        'Модель: ': self.model,
                        'Цена за еденицу: ': self.price,
                        'Количество: ': self.quantity}

    def __str__(self):
        return f'Полное наименование: {self.name + " " + self.brand + " " + self.model}.\nЦена за еденицу: {self.price}.\nКоличество: {self.quantity}.'

storage = OfficeEquipmentStorage('МФУ','HP', 'DeskJet 2130', 3500.00, 100)
print(storage)