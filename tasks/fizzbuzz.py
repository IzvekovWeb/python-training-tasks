"""
Напишите программу, которая выводит на экран числа от 1 до 100. 
При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz», 
а вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5, 
то программа должна выводить слово «FizzBuzz»
"""

def fizzbuzz():
    array = []
    for i in range(1, 100):
        if i % 5 == 0 and i % 3 == 0:
            array.append('FizzBuzz')
        elif i % 5 == 0:
             array.append('Buzz')
        elif i % 3 == 0:
            array.append('Fizz')
        else:
            array.append(i)
    print(array)


fizzbuzz()