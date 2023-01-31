"""Требуется вывести все целые степени двойки (т.е. числа
вида 2k ), не превосходящие числа N.
"""
user_input = int(input('Введите целое положительное число: '))
two_pow = 1
power = 1
while two_pow <= user_input:
    print(two_pow, end=' ')
    two_pow = 2 ** power
    power += 1

