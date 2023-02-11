"""Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных строках. """

from random import randint

num_list = [randint(1, 10) for _ in range(int(input('Введите размер массива: ')))]
print(*num_list)
nums_pairs_count = {}
for num in set(num_list):
    nums_pairs_count.setdefault(num, num_list.count(num) // 2)
print(nums_pairs_count)
print(sum(nums_pairs_count.values()))
