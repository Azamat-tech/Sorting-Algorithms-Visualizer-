from random import randint

def partition(array, start, end, pivot):
    i = start
    j = end - 1

    while True:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        
        if j <= i:
            return j + 1

        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

def quickSort(array, start, end):
    if end - start < 2:
        return
    pivot = array[randint(start, end - 2)]
    k = partition(array, start, end, pivot)
    quickSort(array, start, k)
    quickSort(array, k, end)

def sort(array):
    quickSort(array, 0, len(array))
