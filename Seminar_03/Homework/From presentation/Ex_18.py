"""Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел A. Последняя строка содержит число X
"""

from random import randint
size = int(input('Введите размер списка: '))
nums_tuple = tuple(randint(1, size) for _ in range(size))
print(*nums_tuple)
num_X = int(input('Введите искомое число: '))
mod = 0
flag = False
for _ in range(len(nums_tuple)):
    for i in nums_tuple:
        if i == num_X - mod or i == num_X + mod:
            print(i)
            flag = True
            break
    mod += 1
    if flag:
        break
