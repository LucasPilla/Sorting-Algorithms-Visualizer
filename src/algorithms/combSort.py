def get_gap(prev_gap) -> int:
    """
    Computes the gap between elements in the array based on the previous gap.
    The gap is computed by dividing the previous gap by 1.3 and rounding down.
    The gap is always at least 1.
    """

    gap = int(prev_gap/1.3)
    if gap < 1:
        return 1
    return gap
    

def combSort(array, *args):
    """
    Comb Sort Algorithm is a variation of the Bubble Sort Algorithm.
    It works by comparing and swapping elements that are far apart in the array
    and gradually reducing the gap between elements until the gap is 1.
    The gap between elements is computed by dividing the previous gap by 1.3 and 
    rounding down, with a minimum gap of 1.

    Time complexity: O(n^2), where n is the number of elements in the list
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
