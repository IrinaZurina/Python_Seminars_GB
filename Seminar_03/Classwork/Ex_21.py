"""Задача №21. Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
"""
user_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
             {"V":"S009"}, {" VIII": "S007"}]
values = set()
for i in range(len(user_dict)):
    for key in user_dict[i].keys():
        values.add(user_dict[i][key])
print(f'Множество уникальных значений: {values}')
