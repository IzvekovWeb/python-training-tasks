from datetime import datetime
import time


def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()

        res = func(*args, **kwargs)

        time = datetime.now() - start_time
        print(time)

        return res
    return wrapper
        


@count_time
def factorial_for(x):
    res = 1
    for i in range(1, x):
        res += res * i
    return res


@count_time
def factorial_recursion(x):
    if x == 1:
        return 1
    return x * factorial_recursion(x-1)

x = 100000
print(f'Факториал от {x}')

# print(f'Цикл for: {factorial_for(x)}')
# print(f'Рекурсия: {factorial_recursion(x)}')
factorial_for(x)
# factorial_recursion(x)