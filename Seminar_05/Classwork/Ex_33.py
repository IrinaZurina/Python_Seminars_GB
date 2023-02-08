"""Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
максимальные – на минимальные."""

from random import randint


def change_my_marks(marks):
    max_mark = '5'
    min_mark = '1'
    return marks.replace(max_mark, min_mark, marks.count(max_mark))


marks_list = ''.join(str(randint(1, 5)) for _ in range(int(input('Введите количество оценок: '))))
print(*list(marks_list))
print(*list(change_my_marks(marks_list)))
