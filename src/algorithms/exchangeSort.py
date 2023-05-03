def exchangeSort(array, *args):
    """
    Exchange Sort is a simple sorting algorithm that repeatedly swaps adjacent elements 
    in the array if they are in the wrong order. The algorithm iterates through 
    the array multiple times, comparing adjacent elements and swapping them if
    they are in the wrong order. Each iteration moves the smallest unsorted element 
    to its correct position in the sorted portion of the array.

    Time complexity: O(n^2), where n is the number of elements in the list

    """
    size = len(array)
    for i in range(size - 1):
        for j in range(i + 1, size):
            yield array, i, j, -1, -1
            if array[i] > array[j]:
                array[j], array[i] = array[i], array[j]
