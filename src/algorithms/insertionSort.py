def insertionSort(array, *args):
    """
    
    Insertion Sort works by building up a sorted list one element at a time. 
    Starting from the second element of the input list, the algorithm iterates 
    over the remaining unsorted elements, comparing each element with the previous 
    ones and shifting elements to the right until the correct position is found 
    for the current element. The process repeats until all elements have been inserted 
    into the sorted portion of the list.

    Time complexity: O(n^2), where n is the number of elements in the list
    
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
