"""По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
"""

user_input = int(input('Введите целое положительное число: '))
result = 1
n = user_input
if user_input == 0:
    print(f'{n}! = 1')
else:
    while user_input > 0:
        result *= user_input
        user_input -= 1
    print(f'{n}! = {result}')
