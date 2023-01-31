"""Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
отломить k долек, если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника)."""

chocolate_length = int(input('Длина шоколадки: '))
chocolate_width = int(input('Ширина шоколадки: '))
num_of_pieces = int(input('Количество долек: '))
if num_of_pieces % chocolate_length == 0 or num_of_pieces % chocolate_width == 0:
    print(f'Вы можете отломить от шоколадки {num_of_pieces} дольки/долек')
else:
    print(f'Вы не можете отломить от шоколадки {num_of_pieces} дольки/долек')
