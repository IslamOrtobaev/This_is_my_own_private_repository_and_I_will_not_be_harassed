# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def show_user(name, surname, birth, location, mail, phone):
    print(name, surname, birth, location, mail, phone)
show_user(name='', surname='', birth='', location='', mail='', phone='')