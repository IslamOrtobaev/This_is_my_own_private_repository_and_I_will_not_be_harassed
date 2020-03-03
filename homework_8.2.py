# 2.Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivisionCheck:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(numerator, denominator):
        try:
            return numerator / denominator
        except:
            return f'Я не делю на ноль!'


div = ZeroDivisionCheck(10, 100)
print(ZeroDivisionCheck.divide_by_zero(10, 0))
print(ZeroDivisionCheck.divide_by_zero(10, 0.1))
print(div.divide_by_zero(100, 0))