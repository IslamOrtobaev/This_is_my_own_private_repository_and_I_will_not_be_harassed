"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

quantity = int(input('Введите количество чисел: '))
max_number = 0
summ_max_number = 0

for i in range(1, quantity + 1):
    digit = int(input(f'Число {str(i)}: '))
    residue = 0
    max_digit = digit
    while digit > 0:
        residue += digit % 10
        digit = digit // 10
    if residue > summ_max_number:
        summ_max_number = residue
        max_number = max_digit

print(f'Число {max_number} имеет максимальную сумму цифр: {summ_max_number}')