"""
Задание 3. По введенным пользователем координатам двух
точек вывести уравнение прямой,
проходящей через эти точки.

Подсказка:
Запросите у пользователя значения координат X и Y для первой и второй точки
Найдите в учебнике по высшей математике формулы расчета:
k – угловой коэффициент (действительное число), b – свободный член (действительное число)
Сформируйте уравнение прямой по формуле: y = kx + b – функция общего вида

Пример:
X1_VAL = 2, Y1_VAL = 3, X2_VAL = 4, Y2_VAL = 5
Уравнение прямой, проходящей через эти точки: y = 1.0x + 1.0
"""

X1_VAL = int(input('Введите значение координат X для первой точки: '))
Y1_VAL = int(input('Введите значение координат Y для первой точки: '))
X2_VAL = int(input('Введите значение координат X для второй точки: '))
Y2_VAL = int(input('Введите значение координат Y для второй точки: '))

A = Y2_VAL - Y1_VAL
B = X1_VAL - X2_VAL
C = X2_VAL*Y1_VAL - X1_VAL*Y2_VAL
k = -A/B
b = -C/B

print(f'Уравнение прямой, проходящей через эти точки: y = {k}x + {b}')