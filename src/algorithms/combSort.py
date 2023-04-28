def get_gap(prev_gap) -> int:
    """
    Computes the gap between elements in the array based on the previous gap.
    The gap is computed by dividing the previous gap by 1.3 and rounding down.
    The gap is always at least 1.

    Args:
        prev_gap: Previous gap size used for comparison sorting.

    Returns:
        The next gap size to use for comparison sorting.
    
    """
    gap = int(prev_gap/1.3)
    if gap < 1:
        return 1
    return gap
    

def combSort(array, *args):
    """
    Sorts an array in ascending order using the Comb Sort Algorithm.

    Comb Sort Algorithm is a variation of the Bubble Sort Algorithm.
    It works by comparing and swapping elements that are far apart in the array
    and gradually reducing the gap between elements until the gap is 1.
    The gap between elements is computed by dividing the previous gap by 1.3 and 
    rounding down, with a minimum gap of 1.

    Args:
        array: A list of integers to be sorted.

    Yields:
        A tuple (array, i, i+gap, -1, -1) representing the current state of the sorting algorithm.
        `array` is the current state of the input list.
        `i` and `i+gap` are indices of the elements being compared.
        The last two values are always -1, as they are not used in this algorithm.

    """
    size = len(array)
    gap = size
    swapped = True

    while gap != 1 or swapped:
        gap = get_gap(gap)
        swapped = False

        for idx in range(0, size - gap):
            yield array, idx, idx+gap, -1, -1
            if array[idx] > array[idx + gap]:
                array[idx], array[idx + gap] = array[idx + gap], array[idx]
                swapped = True
