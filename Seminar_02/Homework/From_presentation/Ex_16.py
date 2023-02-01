"""Требуется вывести все целые степени двойки (т.е. числа
вида 2k ), не превосходящие числа N.
"""
# var1 без списка
user_input = int(input('Введите целое положительное число: '))
two_pow, power = 1, 1
while two_pow <= user_input:
    print(two_pow, end=' ')
    two_pow = 2 ** power
    power += 1

# var2 со списком
user_input = int(input('Введите целое положительное число: '))
two_pow_list = []
two_pow, power = 1, 1
while two_pow <= user_input:
    two_pow_list.append(two_pow)
    two_pow = 2 ** power
    power += 1
print(*two_pow_list)
