def selectionSort(array, *args):
    """
    Sorts an array using the Selection Sort Algorithm.

    Selection Sort Algorithm works by finding the smallest element in the unsorted
    part of the array and moving it to the beginning of the unsorted part. This is
    repeated until the entire array is sorted.

    Args:
        array (list): The list to be sorted.
        *args: Optional arguments.

    Yields:
        tuple: A tuple containing the array, the current index being considered, -1,
        the index of the smallest value, and -1.
    
    """
    size = len(array)
    for i in range(size-1):
        smallIndex = i
        for j in range(i, size):
            yield array, j, -1, i, -1
            if array[j] < array[smallIndex]:
                smallIndex = j
        array[i], array[smallIndex] = array[smallIndex], array[i]
