def bubbleSort(array, *args):
    size = len(array)
    for i in range(size):
        swapped = False
        for j in range(size - i - 1):
            yield array, j, j+1, -1, -1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
