def cocktailSort(array, *args):
    """
    Sorts an array using the Cocktail Sort Algorithm.
    
    Cocktail Sort Algorithm, a.k.a. Bidirectional Bubble Sort or Shaker Sort, 
    is a variation of the Bubble Sort Algorithm. It sorts the array in both directions, 
    first from left to right, then from right to left, alternating the direction 
    until the array is sorted. It improves the performance of the Bubble Sort, 
    especially when the array has a large number of elements that are already in order 
    because it can avoid unnecessary iterations through the array.
    
    Args:
        array: A list of comparable elements to be sorted.
    
    Yields:
        A tuple containing the current state of the array and the indices of the two elements 
        that are being compared or swapped. If only one index is relevant, the other value is -1.
    """
    n = len(array)
    swapped = True
    start = 0
    end = n-1
    while swapped:
        swapped = False
        for i in range(start, end):
            yield array, i, i+1, -1, -1
            if (array[i] > array[i+1]):
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
        if swapped is False:
            break
        swapped = False
        end = end-1
        for i in range(end-1, start-1, -1):
            yield array, -1, -1, i, i+1
            if (array[i] > array[i+1]):
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
        start = start+1
