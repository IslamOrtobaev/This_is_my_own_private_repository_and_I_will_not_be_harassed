"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

n = int(input('Введите N: '))
summ = n * (n + 1) // 2
cycle_summ = 0

for i in range(1, n+1):
    cycle_summ += i

print(f'Сумма от 1 до {n}: {summ}.')
print(f'Проверочная сумма от 1 до {n}: {cycle_summ}.')
