from display import handleDrawing
from random import randint


def bogoSort(array, *args):
    is_sorted = False
    arrayLen = len(array)
    while not is_sorted:
        for i in range(arrayLen):
            j = randint(0, arrayLen-1)
            array[i], array[j] = array[j], array[i]

        for k in range(len(array)-1):
            handleDrawing(array, k, k+1, -1, -1)
            if array[k] > array[k+1]:
                is_sorted = False
                break
            is_sorted = True
