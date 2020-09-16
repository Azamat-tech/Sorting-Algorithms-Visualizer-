def sort(array):
    for item in range(len(array) - 1, 0, -1):
        for i in range(item):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
