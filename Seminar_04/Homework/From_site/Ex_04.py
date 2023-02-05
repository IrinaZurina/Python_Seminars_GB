"""Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
и записать в файл многочлен степени k."""

from random import randint
power = int(input('Введите значение степени: '))
coefficients = [randint(0, 10) for _ in range(power + 1)]
print(coefficients)
terms = []
for i in range(power, 1):
    terms.append(f'{coefficients[len(coefficients) - i - 1]}x\u207{i}')