# Задача 2: Найдите сумму цифр трехзначного числа.

user_num = int(input('Введите трехзначное число: '))
# Блок проверки числа на трехзначность
flag = False
while not flag:
    if user_num < 100 or user_num > 999:
        flag = False
        print('Введено неправильное число')
        user_num = int(input('Введите трехзначное число: '))
    else:
        flag = True

# Блок нахождения суммы цифр числа
sum_of_digits = 0
while user_num > 0:
    sum_of_digits += user_num % 10
    user_num //= 10
print(sum_of_digits)
