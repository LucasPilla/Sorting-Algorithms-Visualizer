def selectionSort(array, *args):
    """
    Sorts an array using the Selection Sort Algorithm.

    Selection Sort Algorithm works by finding the smallest element in the unsorted
    part of the array and moving it to the beginning of the unsorted part. This is
    repeated until the entire array is sorted.

    Time complexity: O(n^2), where n is the number of elements in the list. 
    """
    size = len(array)
    for i in range(size-1):
        smallIndex = i
        for j in range(i, size):
            yield array, j, -1, i, -1
            if array[j] < array[smallIndex]:
                smallIndex = j
        array[i], array[smallIndex] = array[smallIndex], array[i]
