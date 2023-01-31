"""Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
"""

# var1 - через строки
s = input()
digit_sum = 0
for i in range(len(s)):
    if s[i].isdigit():
        digit_sum += int(s[i])
print(digit_sum)


# var2 - через десятичные числа
from decimal import *
user_num = abs(Decimal(input()))
digits_sum = 0
for digit in user_num.as_tuple().digits:
    digits_sum += digit
print(digits_sum)
