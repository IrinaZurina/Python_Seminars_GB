"""Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его характеристику."""


def same_by(characteristic, objects: list):
    result_list = []
    for i in range(len(objects) - 1):   # на каждой итерации добавляем в список true/false
        result_list.append(characteristic(objects[i]) == characteristic(objects[i + 1]))
    return all(result_list)


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')