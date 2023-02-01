"""Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K – положительное число.
"""
from random import randint
num_list = [randint(0, 10) for _ in range(int(input('Введите размер списка: ')))]
print(*num_list)
offset = int(input('Введите размер сдвига: '))
if offset == len(num_list) / 2:
    new_list = [num_list[i + offset] if i + offset <= (len(num_list) - 1)
                else num_list[i - offset] for i in range(len(num_list))]
elif offset > len(num_list) / 2:
    new_list = [num_list[i + offset] if i + offset <= (len(num_list) - 1)
                else num_list[i - offset + 1] for i in range(len(num_list))]
else:
    new_list = [num_list[i + offset] if i + offset <= (len(num_list) - 1)
                else num_list[i - offset - 1] for i in range(len(num_list))]
print(*new_list)
