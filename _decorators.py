def simple_decorator():
    def decorator(func):
        """Универсальный декоратор, добавляющий действия о и после функции"""

        def wrapper(*args, **kwargs):
            print('Какие-то действия ДО функции')
            res = func(*args, **kwargs)
            print('Какие-то действия ПОСЛЕ функции')

            return res 

        return wrapper

    @decorator
    def some_func(title):
        print(f'Действия функции some_func - {title}')
        return 123


    # some_func = decorator(some_func)
    print(some_func("Заголовок"))

def parametrized_decorator():

    def param_decorator(pow=2):
        def decorator(func):
            '''Возводит результат функции в степень pow'''
        
            def wrapper(x, *args, **kwargs):
                return x**pow
        
            return wrapper
        
        return decorator
    
    @param_decorator(pow=3)
    def some_func(a):
        return a + 2
    
    print(some_func(5))

parametrized_decorator()