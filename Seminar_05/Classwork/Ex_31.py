"""Последовательностью Фибоначчи
Требуется найти N-е число Фибоначчи"""


def find_fibo(fibo_lst, x):
    if len(fibo_lst) == x:
        return fibo_lst[-1]
    else:
        fibo_lst.append(fibo_lst[-1] + fibo_lst[-2])
        return find_fibo(fibo_lst, x)


print(find_fibo([0, 1], int(input('Введите номер числа Фиббоначи: '))))
