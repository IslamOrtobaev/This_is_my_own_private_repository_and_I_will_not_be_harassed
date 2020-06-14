# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from itertools import count
from math import factorial

def fact():
    for n in count(1):
        yield factorial(n)

gen = fact()
counter = 1
n = int(input('Введите N: '))

for i in gen:
    if counter <= n:
        print(i)
        counter += 1
    else:
        break
"""
n = int(input('Введите N: '))
sequence_list = [element for element in range(0, n + 1)] # если я использую этот список, то идёт вывод от 0! до n!, что не совсем по условию
#sequence_list = [element for element in range(1, n + 1)] # если я использую этот список, то возникает ошибка

# Как будет правильно? 
# Почему возникает ошибка?

print(sequence_list)

def fact():
    for sequence_element in sequence_list:
        yield factorial(sequence_list[sequence_element])

fact = fact()
counter = 0

for element_factorial in fact:
    if counter <= n:
        print(element_factorial)
        counter += 1
"""
