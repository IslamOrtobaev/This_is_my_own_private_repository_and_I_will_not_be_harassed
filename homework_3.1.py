# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_division (x = int(input('Введите X: ')), y = int(input('Введите Y: '))):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return 'Я не делю на ноль.'

print(my_division())