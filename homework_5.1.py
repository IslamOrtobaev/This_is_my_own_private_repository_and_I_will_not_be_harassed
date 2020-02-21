# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_list = []

while True:
    user_input = input('Введите строку: ')
    if user_input == '':
        print(my_list)
        exit()
    else:
        line = user_input + '\n'
        my_list.append(line)

    with open('random.txt', 'w') as my_file:
        my_file.writelines(my_list)