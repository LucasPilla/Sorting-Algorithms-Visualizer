def bubbleSort(array, *args):
    """
    Bubble Sort is a simple comparison-based sorting algorithm that 
    repeatedly compares adjacent elements in a list and swaps them 
    if they are in the wrong order until the list is sorted.
    
    Time complexity: O(n^2), where n is the number of elements in the list.
    """
    size = len(array)
    for i in range(size):
        swapped = False
        for j in range(size - i - 1):
            yield array, j, j+1, -1, -1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
