def pancakeSort(array, *args):
    """
    Pancake sort.

    Only operation is reversing a prefix (a flip): bring the next largest to the front,
    then flip it into place.

    Time complexity: O(n) flips, each O(n) time → O(n²) total (n is the number of elements).
    """
    for i in range(len(array)):
        max_index = array.index(max(array[:len(array) - i]))
        yield array, max_index, -1, -1, -1
        flip(array, max_index)
        yield array, 0, -1, -1, -1
        flip(array, len(array) - 1 - i)
        yield array, -1 , -1, len(array) - 1 - i, -1


def flip(array, n):
    """Reverse *array[0 : n+1]* (inclusive upper index *n* in this implementation)."""
    for i in range(n):
        if i >= n - i:
            break
        array[n - i], array[i] = array[i], array[n - i]
