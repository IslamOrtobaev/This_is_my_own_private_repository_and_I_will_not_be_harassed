# 6) Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

start = int(input('Сколько спортсмен пробежал в первый день? '))
record = int(input('К какому рекорду стремится спортсмен? '))
day = 1

while start < record:
    print(f'{day}-й день: {start}')
    start = start + 0.1*start
    start = float('{:.2f}'.format(start))
    day = day + 1

print(f'{day}-й день: {start}')

print(f'На {day}-й день спортсмен достиг результата - не менее {record} км.')
