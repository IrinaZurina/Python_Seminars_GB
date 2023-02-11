"""Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
"""
from random import randint

num_list_1 = [randint(1, 20) for _ in range(int(input('Введите размер первого массива: ')))]
num_list_2 = [randint(1, 20) for _ in range(int(input('Введите размер второго массива: ')))]
print(*num_list_1)
print(*num_list_2)
list1_unique_nums = set(num_list_1) - set(num_list_2)
for i in num_list_1:
    if i in list1_unique_nums:
        print(i, end=' ')
