"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Постарайтесь решить задачу двумя способами:
1. Через цикл
Вариант исполнения: в бесконечном цикле запрашивайте вид операции, например, +, - или *
Проверяйте вид операции и запускайте соответствующую команду
Предусмотрите выход из бесконечного цикла
2. Рекурсией.
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 45
Введите второе число: 56
Результат 45 + 56 = 101
Введите операцию (+, -, *, / или 0 для выхода): rth
Неверная операция. Повторите ввод
Введите операцию (+, -, *, / или 0 для выхода):

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

while True:
    operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if operation == '0': break
    if operation in ('+', '-', '*', '/'):
        while True:
            try:
                first_number = int(input('Введите первое число: '))
                break
            except ValueError:
                print('Неправильное значение!')
        while True:
            try:
                second_number = int(input('Введите второе число: '))
                break
            except ValueError:
                print('Неправильное значение!')
    if operation == '+':
       result = first_number + second_number
       print(f'Результат: {first_number} + {second_number} = {result}')
    elif operation == '-':
        result = first_number - second_number
        print(f'Результат: {first_number} - {second_number} = {result}')
    elif operation == '*':
        result = first_number * second_number
        print(f'Результат: {first_number} * {second_number} = {result}')
    elif operation == '/':
        if second_number != 0:
            result = first_number / second_number
            print(f'Результат: {first_number} / {second_number} = {result}')
        else:
            print('Не могу разделить на ноль!')
    else:
        print(f'Неправильная операция: {operation}')