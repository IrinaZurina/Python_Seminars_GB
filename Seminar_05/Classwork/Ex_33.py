"""Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
максимальные – на минимальные."""

from random import randint


def change_my_marks(marks):
    max_mark = max(marks)
    min_mark = min(marks)
    marks = list(map(str, marks))
    return ' '.join(marks).replace(str(max_mark), str(min_mark), marks.count(str(max_mark)))


marks_list = [randint(1, 5) for _ in range(int(input('Введите количество оценок: ')))]
print(*marks_list)
print(change_my_marks(marks_list))
