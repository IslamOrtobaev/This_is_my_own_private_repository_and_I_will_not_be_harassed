# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

"""
def my_func(num, exp):
    num = float(num)
    exp = int(exp)
    if num < 0:
        num = num*(-1)
    if exp > 0:
        exp = exp*(-1)
    return num**exp
"""
def my_func(num, exp):
    num = float(num)
    exp = int(exp)
    if num < 0:
        num = num * (-1)
    if exp < 0:
        exp = exp * (-1)
    counter = 0
    result = 1
    while counter < exp:
        result = result * num
        counter = counter + 1
    return 1/result

print(my_func(2,3))

