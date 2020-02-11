# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = [1, 2, 3, 5, 6, 7]

print(my_list)

i = 0

if len(my_list) % 2 == 0:
    while i < len(my_list):
        x = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = x
        i = i + 2
else:
    while i < len(my_list) - 1:
        x = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = x
        i = i + 2

print(my_list)
