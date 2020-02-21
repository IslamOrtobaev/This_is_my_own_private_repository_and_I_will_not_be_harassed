# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('payday.txt', 'r') as my_file:
    salary = []
    below_average = []
    employees = my_file.read().split('\n')
    for employee in employees:
        employee = employee.split()
        if float(employee[1]) < 20000:
           below_average.append(employee[0])
        salary.append(employee[1])
print(f'Оклад меньше 20.000: {below_average} \nCредний оклад: {round((sum(map(float, salary)) / len(salary)), 2)}')