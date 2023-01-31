"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх
одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть."""

# var 1 - без коллекций
from random import randint
coin_num = int(input('Введите количество монеток: '))
eagle_num, tail_num = 0, 0
for _ in range(coin_num):
    coin = randint(0, 1)
    print(coin, end=' ')
    if coin == 0:
        eagle_num += 1
    else:
        tail_num += 1
print()
if eagle_num == tail_num:
    print(f'Все равно какие монеты переворачивать, их число одинаково и равно {eagle_num}')
elif eagle_num < tail_num:
    print(f'Переверните монеты с орлами {eagle_num} раз(а)')
else:
    print(f'Переверните монеты с решками {tail_num} раз(а)')

#var2 через кортеж
from random import randint
coins = tuple(randint(0, 1) for _ in range(int(input('Введите количество монеток: '))))
print(*coins)
eagle_num = coins.count(0)
tail_num = coins.count(1)
if eagle_num == tail_num:
    print(f'Все равно какие монеты переворачивать, их число одинаково и равно {eagle_num}')
elif eagle_num < tail_num:
    print(f'Переверните монеты с орлами {eagle_num} раз(а)')
else:
    print(f'Переверните монеты с решками {tail_num} раз(а)')


