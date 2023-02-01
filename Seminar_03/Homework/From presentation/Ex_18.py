"""Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел A. Последняя строка содержит число X
"""

from random import randint
size = int(input('Введите размер списка: '))
nums_tuple = tuple(randint(1, size) for _ in range(size))
print(nums_tuple)
num_X = int(input('Введите искомое число: '))
num_X_less = num_X_more = num_X
flag = False
while not flag:
    if num_X_more in nums_tuple:
        print(num_X_more)
        flag = True
    elif num_X_less in nums_tuple:
        print(num_X_less)
        flag = True
    else:
        num_X_less -= 1
        num_X_more += 1
