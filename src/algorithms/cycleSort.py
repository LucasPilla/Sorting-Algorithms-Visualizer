def cycleSort(array, *args):
    """
    Cycle Sort is an in-place sorting algorithm that is most useful 
    for situations where memory writes are more expensive than reads. 
    It minimizes the number of memory writes to sort an array. It works 
    by dividing the array into cycles, where each cycle contains one value 
    that is in its correct position. The algorithm then moves through the cycles, 
    swapping values until the entire array is sorted.

    Time complexity: O(n^2), where n is the number of elements in the list
    """
    for cycle_start in range(0, len(array) - 1):
        item = array[cycle_start]
        pos = cycle_start
        
        for i in range(cycle_start + 1, len(array)):
            if array[i] < item:
                pos += 1

        if pos == cycle_start:
            continue

        while array[pos] == item:
            pos += 1
        yield array, cycle_start, pos, -1, -1
        array[pos], item = item, array[pos]

        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, len(array)):
                if array[i] < item:
                    pos += 1

            while array[pos] == item:
                pos += 1
            yield array, cycle_start, pos, -1, -1
            array[pos], item = item, array[pos]
