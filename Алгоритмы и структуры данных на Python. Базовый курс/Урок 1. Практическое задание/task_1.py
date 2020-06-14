"""
Задание 1.
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
#print(124 // 100) = 1 - отбросить остаток
#print((124 // 10) % 10) = 2 - остаток от деления числа 12 на 10
#print(124 % 10) = 4 - остаток от деления числа 124 на 10

Пример: Целое трехзначное число 123
Сумма = 6
Произведение = 6

Подсказка: для получения отдельных цифр числа используйте арифм. операции
и НЕ ИСПОЛЬЗУЙТЕ операции с массивами
"""
user_input_number = input("Введите трёхзначное число: ")

while len(user_input_number) != 3:
    user_input_number = input("Введите ТРЁХЗНАЧНОЕ число: ")

user_input_number = int(user_input_number)

first = user_input_number // 100
second = (user_input_number // 10) % 10
third = user_input_number % 10
summ = first + second + third
multiply = first * second * third

print(f'Сумма: {summ}\nПроизведение: {multiply}')