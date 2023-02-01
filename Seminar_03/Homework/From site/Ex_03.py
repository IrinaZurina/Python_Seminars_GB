"""Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов."""

from random import uniform
num_list = [round(uniform(0, 10), 2) for _ in range(int(input('Введите размер списка: ')))]
print(num_list)
digits_sum_list = []
for num in num_list:
    digits_sum = 0
    for i in range(str(num).find('.') + 1, len(str(num))):
        digits_sum += int(str(num)[i])
    digits_sum_list.append(digits_sum)
print(digits_sum_list)
print(max(digits_sum_list))
