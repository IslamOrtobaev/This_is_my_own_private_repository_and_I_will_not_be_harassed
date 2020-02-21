# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('numbers.txt', 'w+') as my_file:
    user_input = input('Введите цифры через пробел: \n')
    my_file.writelines(user_input)
    my_numbers = user_input.split()
    print(sum(map(int, my_numbers)))