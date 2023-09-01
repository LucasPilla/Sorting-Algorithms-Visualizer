def quickSort_LR(array, low, high):
    """
    quickSort_LR() function sorts an array in ascending order using the QuickSort Algorithm. 
    The algorithm recursively partitions the array into subarrays around a pivot element and sorts 
    each subarray independently. The partition() function is used to partition the array into two 
    subarrays, such that all elements to the left of the pivot are less than or equal to the pivot, 
    and all elements to the right are greater than or equal to the pivot.

    Time complexity: O(nlog²n).
    """

    if low < high:
        p = partition(array, low, high)
        yield array, p, high, low, -1
        yield from quickSort_LR(array, low, p)
        yield from quickSort_LR(array, p + 1, high)

def partition(array, low, high):
    """
    Partitions the array into two subarrays around a pivot element and returns the pivot index.

    Returns:
        An integer index of the pivot element after partitioning the array.
    """

    pivot = array[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while array[i] < pivot:
            i += 1

        j -= 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]
