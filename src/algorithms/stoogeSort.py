from math import floor

def stoogeSort(arr, l, h):
    """
    Stooge sort.

    Recursively sorts the first two-thirds, then the last two-thirds, then the first
    two-thirds again (deliberately inefficient).

    Time complexity: O(n^(log_{3/2} 3)) ≈ O(n^2.71) (n is the subarray length).
    """

    if l >= h:
        return

    if arr[l] > arr[h]:
        middle = floor((h + l) / 2)
        yield arr, (l, h), (middle,)
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t

    if h-l + 1 > 2:
        t = (int)((h-l + 1)/3)

        yield from stoogeSort(arr, l, (h-t))
        yield from stoogeSort(arr, l + t, (h))
        yield from stoogeSort(arr, l, (h-t))
