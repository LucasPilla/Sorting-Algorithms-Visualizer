def exchangeSort(array, *args):
    """
    Sorts the input array using the Exchange Sort Algorithm.

    Exchange Sort is a simple sorting algorithm that repeatedly swaps adjacent elements 
    in the array if they are in the wrong order. The algorithm iterates through 
    the array multiple times, comparing adjacent elements and swapping them if
    they are in the wrong order. Each iteration moves the smallest unsorted element 
    to its correct position in the sorted portion of the array.

    Args:
        array (list): The unsorted input array.

    Yields:
        tuple: A tuple containing the current state of the array and the indices of 
        the elements being compared in the current iteration.
    """
    size = len(array)
    for i in range(size - 1):
        for j in range(i + 1, size):
            yield array, i, j, -1, -1
            if array[i] > array[j]:
                array[j], array[i] = array[i], array[j]
