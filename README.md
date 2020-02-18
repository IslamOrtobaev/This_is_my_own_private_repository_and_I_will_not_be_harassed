# This_is_my_own_private_repository_and_I_will_not_be_harassed

"""
n = int(input('Введите N: '))
sequence_list = [element for element in range(0, n + 1)] # если я использую этот список, то идёт вывод от 0! до n!, что не совсем по условию
#sequence_list = [element for element in range(1, n + 1)] # если я использую этот список, то возникает ошибка 
"""
Как будет правильно?
Почему возникает ошибка? 
"""
print(sequence_list)

def fact():
    for sequence_element in sequence_list:
        yield factorial(sequence_list[sequence_element])

fact = fact()
counter = 0

for element_factorial in fact:
    if counter <= n:
        print(element_factorial)
        counter += 1
"""
