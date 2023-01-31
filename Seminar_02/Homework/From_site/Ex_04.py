"""Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число."""

from random import randint
user_input = int(input('Введите целое положительное число'))
elements_list = [randint(-user_input, user_input) for _ in range(user_input)]
