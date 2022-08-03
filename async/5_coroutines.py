
def corountine(func):
    def inner(*args, **kwrags):
        g = func(*args, **kwrags)
        g.send(None)
        return g
    return inner


def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen recieved', message)
     

class CustomException(Exception):
    pass


@corountine
def average():
    count = 0
    summ = 0
    average = 0

    while True:
        try:
            x = yield average
        except StopIteration:
            break
        except CustomException:
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
    
    return average