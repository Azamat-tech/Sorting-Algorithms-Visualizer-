def selectionSort(array):
    for item in range(len(array)):
        minimum_item_id = item 
        for item2 in range(item+1, len(array)):
            if array[minimum_item_id] > array[item2]:
                minimum_item_id = item2
        array[item], array[minimum_item_id] = array[minimum_item_id], array[item]
