# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input("Введите месяц по номеру: "))

if month == 1 or month == 12 or month == 2:
    print(seasons_dict.get(1), type(seasons_dict))
    print(seasons_list[0], type(seasons_list))
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2), type(seasons_dict))
    print(seasons_list[1], type(seasons_list))
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3), type(seasons_dict))
    print(seasons_list[2], type(seasons_list))
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4), type(seasons_dict))
    print(seasons_list[3], type(seasons_list))
else:
    print("Такого месяца не существует.")