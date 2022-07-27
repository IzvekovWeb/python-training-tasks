def fibonachi(n):
    """Числа Фибоначчи – это ряд чисел, в котором каждое следующее число равно сумме двух предыдущих.
    
    Построить последовательность до n-го числа
    """

    a = b = 1
    arr = [0, a, b]
    for i in range(n):
        fib = a + b
        a = b
        b = fib
        arr.append(fib)
    return arr

def fibonachi_recursion_search(n):
    if n in (1, 2):
        return 1
    return fibonachi_recursion_search(n - 1) + fibonachi_recursion_search(n - 2)


print(fibonachi(10))
print(fibonachi_recursion_search(10))