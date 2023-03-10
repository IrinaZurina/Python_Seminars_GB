"""Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
Пример:
- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}"""

# ??? Мне не очень понятно, почему в примере в итоговом словаре первая сумма не равна первому члену последовательности...

user_input = int(input('Введите целое положительное число: '))
sum_dict = {1: 2}   # инициируем словарь, где ключ - номер члена последовательности, значение - сумма членов последовательности
sequence = [(1 + 1 / 1) ** 1]   # список для записи членов последовательности
for i in range(2, user_input + 1):
    sum_dict.setdefault(i, (sum_dict[i - 1] + (1 + 1 / i) ** i))   # добавляем в словарь новые ключи и значения
    sequence.append((1 + 1 / i) ** i)   # добавляем в список новые члены последовательности
print(*sequence)
for key, value in sum_dict.items():
    print(f'{key}: {int(round(value, 0))},', end=' ')   #выводим словарь с округленными значениями суммы членов последовательности
