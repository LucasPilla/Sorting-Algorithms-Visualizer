def quickSort_LR(array, low, high):
    """
    Quicksort (Hoare / LR partition).

    Uses Hoare partition around ``array[low]``; recurses on ``[low..p]`` and ``[p+1..high]``.

    Time complexity: O(n log n) expected; O(n²) worst case (n is the subarray length).
    """

    if low < high:
        p = partition(array, low, high)
        yield array, (p, high), (low,)
        yield from quickSort_LR(array, low, p)
        yield from quickSort_LR(array, p + 1, high)

def partition(array, low, high):
    """Hoare partition; returns index *j* such that elements on each side can be sorted recursively."""

    pivot = array[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while array[i] < pivot:
            i += 1

        j -= 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]
