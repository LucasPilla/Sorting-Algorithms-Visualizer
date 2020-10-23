from display import handleDrawing


def binaryinsertionSort(array, *args):
    for i in range(1, len(array)):
        val = array[i]
        handleDrawing(array, i, -1, -1, -1)
        j = binary_search(array, val, 0, i - 1)
        array[0:len(array)] = array[:j] + [val] + array[j:i] + array[i + 1:]
        handleDrawing(array, i+1, -1, j, -1)


def binary_search(arr, val, start, end):
    handleDrawing(arr, -1, -1, start, end)
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = round((start + end) / 2)
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid
