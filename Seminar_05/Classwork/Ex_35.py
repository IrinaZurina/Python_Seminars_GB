"""Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым"""


def num_is_prime(x):
    count = 0
    for f in range(1, x + 1):
        if x % f == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


answer = 'Yes' if num_is_prime(int(input('Введите натуральное число: '))) else 'NO'
print(answer)