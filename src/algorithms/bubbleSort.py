def bubbleSort(array, *args):
    """
    Sorts an array in ascending order using Bubble Sort Algorithm.

    Bubble Sort Algorithm is a simple sorting algorithm that repeatedly 
    steps through the list to be sorted, compares adjacent elements and 
    swaps them if they are in the wrong order. The pass through the list 
    is repeated until the list is sorted. Because it only uses comparisons 
    to operate on elements, it is a comparison sort. 
    
    The algorithm gets its name from the way smaller elements "bubble" to 
    the top of the list as it is repeatedly passed through.

    Args:
        array (list): The array to be sorted.

    Yields:
        tuple: A tuple containing the array, index of the first element being compared, index of the second element being compared,
        -1 to indicate that no element has been swapped, and -1 to indicate that no element has been sorted.

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
