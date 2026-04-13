from algorithms.binaryInsertionSort import binary_search


def calculate_min_run(n):
    """Minimum run size for this Timsort-style merge (Python-style heuristic, min run ≈ 32)."""
    last_bit = 0
    RUN_LEN  = 32
    
    while n >= RUN_LEN:
        last_bit |= n & 1
        n >>= 1

    return n + last_bit


def _binary_insertion_sort_run(arr, start, end):
    """Binary-insertion-sort the inclusive range ``arr[start:end+1]`` (yields intermediate states)."""
    for i in range(start, end + 1):
        val = arr[i]
        j   = binary_search(arr, val, start, i - 1)
        yield arr, (start, i - 1), (j, i)
        arr[:] = arr[:j] + [val] + arr[j:i] + arr[i + 1:]


def merge(arr, left, mid, right):
    """Merge sorted ``arr[left:mid+1]`` and ``arr[mid+1:right+1]`` into place."""

    left_arr_size  = mid - left + 1
    right_arr_size = right - mid
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    k, i, j = left, 0, 0
    while i < left_arr_size and j < right_arr_size:
        yield arr, (left + i, mid + j), (left, right)

        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1

        else:
            arr[k] = right_arr[j]
            j += 1

        k += 1

    if i < left_arr_size:
        arr[k:right + 1] = left_arr[i:]
    else:
        arr[k:right + 1] = right_arr[j:]


def timSort(arr, beginning, ending):
    """
    Timsort (simplified).

    Forms short runs with binary insertion sort, then repeatedly merges runs by doubling
    width (similar spirit to Python's list.sort, but not identical).

    Time complexity: O(n log n) worst case for merge-based phases (n is len(arr)); *beginning* and *ending* are accepted for API consistency but unused.
    """
    arr_len = len(arr)
    min_run = calculate_min_run(arr_len)

    for start in range(0, arr_len, min_run):
        end = min(start + min_run - 1, arr_len - 1)
        yield from _binary_insertion_sort_run(arr, start, end)

    size = min_run
    while size < arr_len:
        for left in range(0, arr_len, 2 * size):
            mid   = min(arr_len - 1, left + size - 1)
            right = min(left + 2 * size - 1, arr_len - 1)
            yield from merge(arr, left, mid, right)
        size *= 2
