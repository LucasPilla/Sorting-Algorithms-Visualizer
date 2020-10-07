from display import handleDrawing


def selectionSort(array, *args):
    size = len(array)
    for i in range(size-1):
        smallIndex = i
        for j in range(i, size):
            handleDrawing(array, j, -1, i, -1)
            if array[j] < array[smallIndex]:
                smallIndex = j
        array[i], array[smallIndex] = array[smallIndex], array[i]
