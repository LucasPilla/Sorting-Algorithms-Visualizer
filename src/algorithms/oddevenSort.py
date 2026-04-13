def swap(array, i, j):
    """Swap ``array[i]`` and ``array[j]``."""

    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def oddevenSort(array, *args):
    """
    Odd-even sort (Brick sort).

    Alternates odd-index and even-index adjacent comparisons, like parallel bubble passes.

    Time complexity: O(n²) sequential work; O(n) parallel rounds in the PRAM model (n is the number of elements).
    """
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(array) - 1, 2):
            yield array, (i, i + 1), ()
            if array[i] > array[i + 1]:
                swap(array, i, i + 1)
                sorted = False

        for i in range(0, len(array) - 1, 2):
            yield array, (i, i + 1), ()
            if array[i] > array[i + 1]:
                swap(array, i, i + 1)
                sorted = False
