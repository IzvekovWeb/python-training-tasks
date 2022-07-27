def it1():
    some_list = [1, 2, 3, 4, 5, 6]
    iterator = iter(some_list)

    print(next(iterator))

    for i in range(8):
        try: 
            print(next(iterator))
        except StopIteration:
            print('Итератор закончился')


class MyIterator():
    '''Итератор бесконечного перебора чисел'''

    def __init__(self, start=0):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num


def it2():
    count =  MyIterator()
    
    for i in range(8):
        try: 
            print(next(count))
        except StopIteration:
            print('Итератор закончился')

favorite_numbers = [6, 57, 4, 7, 68, 95]

def it3_1():
    """Выражение генератора"""

    a = (a ** 2 for a in favorite_numbers)
    print(a)
    print(dir(a))
    print(type(a))
    print()
    print(next(a))
    print(next(a))
    print(next(a))

def it3_2():

    def gen():
        """Функция генератора"""

        for a in favorite_numbers:
            yield a ** 2
    
    g = gen()

    print(next(g))
    print(next(g))
    print(next(g))

# it3_1()
# print()
# it3_2()