from display import handleDrawing


def quickSort(array, left, right):
    if left >= right:
        return
    index = left
    for j in range(left, right):
        # The four lines below are not part of the algorithm
        handleDrawing(array, j, right, index, -1)
        if array[j] < array[right]:
            array[j], array[index] = array[index], array[j]
            index += 1
    array[index], array[right] = array[right], array[index]
    quickSort(array, index + 1, right)
    quickSort(array, left, index - 1)
