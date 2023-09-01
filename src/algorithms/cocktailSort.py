def cocktailSort(array, *args):
    """    
    Cocktail sort is a variation of Bubble sort that sorts a list in both directions, 
    first from left to right like in Bubble sort, then from right to left, and so on 
    until the list is sorted. It has a slightly better average-case performance than 
    Bubble sort because it can move large elements to the right more quickly.
    
    Time complexity: O(n^2) where n is the number of elements in the list. 
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
