# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

user_input = input('Введите строку из нескольких слов или символов, разделённых пробелом: ')

split = user_input.split(' ')
for i, slice in enumerate(split, 1):
    if len(slice) > 10:
        slice = slice[0:10]
    print(f"{i}) {slice}")