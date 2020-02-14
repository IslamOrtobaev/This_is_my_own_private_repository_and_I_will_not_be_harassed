# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(x = int(input('Введите X: ')), y = int(input('Введите Y: ')), z = int(input('Введите Z: '))):
    start_list = [x, y, z]
    finish_list = []
    a = max(start_list)
    finish_list.append(a)
    start_list.remove(a)
    b = max(start_list)
    finish_list.append(b)
    start_list.remove(b)
    return sum(finish_list)

print(my_func())