def exchangeSort(array, *args):
    """
    Exchange sort.

    For each i, compares index i with every j > i and swaps if out of order (similar
    spirit to selection sort, using explicit swaps).

    Time complexity: O(n²) (n is the number of elements).
    """
    size = len(array)
    for i in range(size - 1):
        for j in range(i + 1, size):
            yield array, i, j, -1, -1
            if array[i] > array[j]:
                array[j], array[i] = array[i], array[j]
