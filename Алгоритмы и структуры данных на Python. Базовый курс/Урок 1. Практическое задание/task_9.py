"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))
avg = 0
if number_1 == number_2 == number_3:
    avg = number_1
    print(f'Введены равные числа.')
else:
    if number_1 < number_2 < number_3 or number_1 > number_2 > number_3:
        avg = number_2
        print(f'Среднее число: {avg}.')
    elif number_1 > number_2 and number_3 > number_2:
        if number_1 > number_3:
            avg = number_3
            print(f'Среднее число: {avg}.')
        else:
            avg = number_1
            print(f'Среднее число: {avg}.')
    elif number_1 < number_2 and number_3 < number_2:
        if number_1 < number_3:
            avg = number_3
            print(f'Среднее число: {avg}.')
        else:
            avg = number_1
            print(f'Среднее число: {avg}.')
