"""Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел A. Последняя строка содержит число X
"""

from random import randint
size = int(input('Введите размер списка: '))
numbers = tuple(randint(1, size) for _ in range(size))
print(*numbers)
num_X = int(input('Введите искомое число: '))
mod = 0
flag = False
for _ in range(len(set(numbers))):
    for i in set(numbers):
        if i == num_X - mod or i == num_X + mod:
            print(i)
            flag = True
            break
    if flag:
        break
    mod += 1
