# 5) Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

income = int(input('Выручка фирмы: '))
outcome = int(input('Издержки фирмы: '))

if income > outcome:
    profit = income - outcome
    print(f'Прибыль фирмы: {profit}')
    efficiency = profit / outcome
    print(f'Коэффициент рентабельности: {efficiency}')
    workers = int(input('Количество сотрудников: '))
    profit_per_worker = profit / workers
    print(f'Прибыль фирмы в расчете на одного сотрудника: {profit_per_worker}')
elif income == outcome:
    print('Фирма не получает прибыли.')
else:
    print('Фирма несёт убытки.')