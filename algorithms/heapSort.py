from display import handleDrawing


def heapSort(array, *args):
    heapify(array, len(array))
    end = len(array) - 1
    while end > 0:
        handleDrawing(array, -1, -1, 0, end, )
        array[end], array[0] = array[0], array[end]
        end -= 1
        siftDown(array, 0, end)


def heapify(array, count):
    start = (count-1) // 2
    while start >= 0:
        siftDown(array, start, count - 1)
        start -= 1


def siftDown(array, start, end):
    root = start
    while 2 * root + 1 <= end:
        child = 2 * root + 1
        swap = root
        if array[swap] < array[child]:
            swap = child
        if child + 1 <= end and array[swap] < array[child + 1]:
            swap = child + 1
        if swap == root:
            return
        else:
            handleDrawing(array, root, swap, -1, -1)
            array[root], array[swap] = array[swap], array[root]
            root = swap
