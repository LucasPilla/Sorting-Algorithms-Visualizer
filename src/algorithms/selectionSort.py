def selectionSort(array, *args):
    """
    Selection sort.

    Repeatedly finds the minimum in the unsorted suffix and swaps it into place at
    the front of that suffix.

    Time complexity: O(n²) in all cases (n is the number of elements).
    """
    size = len(array)
    for i in range(size-1):
        smallIndex = i
        for j in range(i, size):
            yield array, (j,), (i,)
            if array[j] < array[smallIndex]:
                smallIndex = j
        array[i], array[smallIndex] = array[smallIndex], array[i]
