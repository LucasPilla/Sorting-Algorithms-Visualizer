from display import handleDrawing


def pancakeSort(array, *args):
    for i in range(len(array)):
        max_index = array.index(max(array[:len(array) - i]))
        handleDrawing(array, max_index, -1, -1, -1)
        flip(array, max_index)
        handleDrawing(array, 0, -1, -1, -1)
        flip(array, len(array) - 1 - i)
        handleDrawing(array, -1 , -1, len(array) - 1 - i, -1)


def flip(array, n):
    for i in range(n):
        if i >= n - i:
            break
        array[n - i], array[i] = array[i], array[n - i]
