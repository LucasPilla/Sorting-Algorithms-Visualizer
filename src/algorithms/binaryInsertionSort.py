def binaryInsertionSort(array, *args):
    """
    Binary insertion sort.

    Like insertion sort but finds the insertion index with binary search; still shifts
    elements in a contiguous array, so moves dominate.

    Time complexity: O(n log n) comparisons; O(n²) time for typical array/list implementations due to shifting (n is the number of elements).
    """
    for i in range(1, len(array)):
        val = array[i]
        j = binary_search(array, val, 0, i - 1)
        yield array, (0, i - 1), (j, i)
        array[:] = array[:j] + [val] + array[j:i] + array[i + 1:]


def binary_search(arr, val, start, end):
    """
    Find the insertion index for *val* in sorted *arr[start : end+1]*.

    Time complexity: O(log n) comparisons for a range of length n.

    Example:
        >>> arr = [1, 2, 4, 5, 6]
        >>> binary_search(arr, 3, 0, 4)
        2
    """
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = round((start + end) / 2)
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid
