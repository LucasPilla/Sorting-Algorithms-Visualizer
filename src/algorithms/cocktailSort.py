def cocktailSort(array, *args):
    """
    Cocktail sort (bidirectional bubble sort).

    Alternates left-to-right and right-to-left passes, swapping out-of-order neighbors,
    until a full pass makes no swaps.

    Time complexity: O(n²) average and worst case; O(n) best case when already sorted.
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
