def insertionSort(array, *args):
    """
    Insertion sort.

    Builds a sorted prefix by taking each next element and shifting larger elements
    right until the correct position is found.

    Time complexity: O(n²) average and worst case; O(n) best case when the input is already sorted.
    """
    mySortedRows = []
    size = len(array)
    for i in range(0, size):
        j = i-1
        key = array[i]
        mySortedRows.append(i)
        while j >= 0 and array[j] > key:
            yield array, (j,), (i,)
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    mySortedRows.clear()
