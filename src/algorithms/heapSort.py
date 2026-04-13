def heapSort(array, *args):
    """
    Heapsort.

    Builds a max-heap, then repeatedly swaps the root with the last heap position and
    sifts down to restore the heap property.

    Time complexity: O(n log n) time and O(1) extra space (in-place; n is the number of elements).
    """
    yield from heapify(array, len(array))
    end = len(array) - 1
    while end > 0:
        yield array, (), (0, end)
        array[end], array[0] = array[0], array[end]
        end -= 1
        yield from siftDown(array, 0, end)


def heapify(array, count):
    """Turn *array[:count]* into a max-heap by sifting down from the last parent."""
    start = (count-1) // 2
    while start >= 0:
        yield from siftDown(array, start, count - 1)
        start -= 1


def siftDown(array, start, end):
    """Sift the element at *start* down in the max-heap bounded by *end*."""
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
            yield array, (root, swap), ()
            array[root], array[swap] = array[swap], array[root]
            root = swap
