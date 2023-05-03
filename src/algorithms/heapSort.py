def heapSort(array, *args):
    """
    Sorts an array using the Heap Sort Algorithm.

    Heap Sort is a comparison-based sorting algorithm that works by first 
    constructing a heap (a type of tree-based data structure) from the given 
    elements, and then repeatedly extracting the maximum element from the heap 
    and placing it at the end of the sorted array. The process of extracting 
    the maximum element involves swapping it with the last element in the heap, 
    then fixing the heap to maintain the heap property. This process is repeated 
    until all elements have been extracted and placed in their correct position 
    in the sorted array. 
    
    Time complexity: O(nlog²n).
    """
    yield from heapify(array, len(array))
    end = len(array) - 1
    while end > 0:
        yield array, -1, -1, 0, end
        array[end], array[0] = array[0], array[end]
        end -= 1
        yield from siftDown(array, 0, end)


def heapify(array, count):
    """
    Creates a max heap from an array.
    """
    start = (count-1) // 2
    while start >= 0:
        yield from siftDown(array, start, count - 1)
        start -= 1


def siftDown(array, start, end):
    """
    Moves the element at the specified index down the tree 
    until it is in the correct position in the heap.
    """
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
            yield array, root, swap, -1, -1
            array[root], array[swap] = array[swap], array[root]
            root = swap
