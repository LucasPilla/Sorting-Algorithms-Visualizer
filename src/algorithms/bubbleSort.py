def bubbleSort(array):
    """
    Bubble Sort is a simple comparison-based sorting algorithm that 
    repeatedly compares adjacent elements in a list and swaps them 
    if they are in the wrong order until the list is sorted.
    
    Time complexity: O(n^2), where n is the number of elements in the list.
    
    :param array: The list to be sorted.
    :return: The sorted list.
    """
    size = len(array)
    for i in range(size):
        swapped = False
        for j in range(size - i - 1):
            # Visualize the current state of the array and the elements being compared
            yield array, j, j + 1
            if array[j] > array[j + 1]:
                # Swap the elements if they are in the wrong order
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break

