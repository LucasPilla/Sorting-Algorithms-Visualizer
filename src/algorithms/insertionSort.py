def insertionSort(array, *args):
    """
    Sorts a given list using the Insertion Sort Algorithm.

    Insertion Sort works by building up a sorted list one element at a time. 
    Starting from the second element of the input list, the algorithm iterates 
    over the remaining unsorted elements, comparing each element with the previous 
    ones and shifting elements to the right until the correct position is found 
    for the current element. The process repeats until all elements have been inserted 
    into the sorted portion of the list.

    Args:
        array (list): The list to be sorted.

    Yields:
        tuple: A tuple containing the current state of the list, along with indices indicating the current elements being
        compared and/or swapped. The tuple format is (array, index1, index2, index3, index4), where index1 and index2
        correspond to the indices of the two elements being compared, and index3 and index4 correspond to the indices of
        the two elements being swapped (if applicable).

    """
    mySortedRows = []
    size = len(array)
    for i in range(0, size):
        j = i-1
        key = array[i]
        mySortedRows.append(i)
        while j >= 0 and array[j] > key:
            yield array, j, -1, i, -1
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    mySortedRows.clear()
