# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.

def get_count_words(string):
    counter = 0
    flag = 0
    for i in range(len(string)):
        if string[i] != ' ' and string[i] != '\n' and flag == 0:
            counter += 1
            flag = 1
        else:
            if string[i] == ' ':
                flag = 0
    return counter

with open('random.txt') as my_file:
    lines = 1
    line_number = 0
    words = 0
    for line in my_file:
        lines += line.count('\n')
        words = get_count_words(line)
        line_number += 1
        print(f'Слов в {line_number} строке: {words}')
    print(f'Строк в файле: {lines}')

"""
В первоначальной версии программы я использовал split, но он просто считал пробелы, и считал сивол '\n' за слово.
Мне показалось это неправильно и я написал отдельную функцию. Стоило ли так делать, или же использовать split?
Как правильно?
"""