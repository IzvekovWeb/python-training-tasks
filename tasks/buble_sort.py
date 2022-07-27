def buble_sort(arr):
    """Сортировка 'пузырьком'\перестановкой 

    Сложность O(n^2)
    """

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1) :
            if arr[j] > arr[j + 1]:
                t = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = t

array = [1, 5, 74, 3, 2, 17, 100, 4]

buble_sort(array)
print(array)