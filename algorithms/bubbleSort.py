from display import handleDrawing


def bubbleSort(array, *args):
    size = len(array)
    for i in range(size):
        for j in range(size - i - 1):
            handleDrawing(array, j, j+1, -1, -1)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
