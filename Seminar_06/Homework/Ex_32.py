"""Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного максимума) """

from random import randint

num_list = [randint(1, 100) for _ in range(int(input('Введите размер массива: ')))]
left_endpoint = int(input('Введите минимум диапазона: '))
right_endpoint = int(input('Введите максимум диапазона: '))
indexes_list = []
for i in range(len(num_list)):
    if left_endpoint <= num_list[i] <= right_endpoint:
        indexes_list.append(i)
print(num_list)
print(indexes_list)
