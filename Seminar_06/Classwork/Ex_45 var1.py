def sum_divisors(num):
    summ = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            # print(f'{i = }')
            summ += i
    return summ


def friends_num(number):
    for i in range(1, number):
        j = sum_divisors(i)
        if i < j <= number and i == sum_divisors(j):
            print(i, j)


friends_num(int(input('Введите число К: ')))
