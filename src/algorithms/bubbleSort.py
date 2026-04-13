def bubbleSort(array, *args):
    """
    Bubble sort.

    Repeatedly steps through the list, compares adjacent elements, and swaps them
    if they are in the wrong order, until no swaps occur on a full pass.

    Time complexity: O(n²) average and worst case; O(n) best case when the list is already sorted (early exit).
    """
    size = len(array)
    for i in range(size):
        swapped = False
        for j in range(size - i - 1):
            yield array, (j, j + 1), ()
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
