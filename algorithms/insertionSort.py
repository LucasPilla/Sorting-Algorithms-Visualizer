from display import handleDrawing


def insertionSort(array, *args):
    size = len(array)
    for i in range(1, size):
        j = i-1
        key = array[i]
        while j >= 0 and array[j] > key:
            handleDrawing(array, j, -1, i, -1)
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
