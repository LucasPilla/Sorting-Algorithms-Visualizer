def get_gap(prev_gap) -> int:
    """Next comb-sort gap: ⌊previous / 1.3⌋, floored at 1."""

    gap = int(prev_gap/1.3)
    if gap < 1:
        return 1
    return gap
    

def combSort(array, *args):
    """
    Comb sort.

    Like bubble sort but compares elements *gap* apart; gap shrinks each pass until 1.

    Time complexity: O(n²) worst case; typically faster than bubble sort in practice (n is the number of elements).
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
