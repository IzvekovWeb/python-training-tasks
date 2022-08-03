
def corountine(func):
    def inner(*args, **kwrags):
        g = func(*args, **kwrags)
        g.send(None)
        return g
    return inner


class CustomException(Exception):
    pass



def subgen():
    while True:
        try:
            message = yield
        except CustomException:
            print('Exception!!')
        else:
            print('-------', message)


@corountine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except CustomException as e:
    #         g.throw(e)

    yield from g