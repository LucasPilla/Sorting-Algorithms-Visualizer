from math import ceil, floor


def getShellGaps(N):
    """
    Compute gap sequence for Shell sort.

    The gap sequence is computed as follows: starting with the largest gap
    possible, divide it by 2 at each iteration until reaching 1. The resulting
    gaps are returned in decreasing order.

    Args:
        N (int): The length of the array to be sorted.

    Returns:
        list: A list of integers representing the gap sequence for Shell sort.
    """
    gaps, k = [], 0
    getKth = lambda k: floor(N / 2 ** k)
    while getKth(k) > 1:
        gaps.append(getKth(k))
        k += 1
    return gaps + [1]


def getCiuraGaps(*args):
    """
    Return the gap sequence proposed by Ciura.

    The sequence was proposed in the paper "Best Increments for the Average
    Case of Shellsort" by Marcin Ciura.

    Returns:
        list: A list of integers representing the gap sequence proposed by
            Ciura.
    """
    return [1750, 701, 301, 132, 57, 23, 10, 4, 1]


def getTokudaGaps(N):
    """
    Compute gap sequence proposed by Tokuda.

    The sequence was proposed in the paper "An Improved Shellsort" by N. Tokuda.
    ( N. Tokuda, An Improved Shellsort, IFIP Transactions, A-12 (1992) 449-457)

    Args:
        N (int): The length of the array to be sorted.

    Returns:
        list: A list of integers representing the gap sequence proposed by
            Tokuda.
    """
    gaps, k = [], 1
    getKth = lambda k: ceil((9 * (9 / 4) ** (k - 1) - 4) / 5)
    while getKth(k) <= N:
        gaps = [getKth(k)] + gaps
        k += 1
    return gaps


def getKnuthGaps(N):
    """
    Compute gap sequence proposed by Knuth.

    The sequence was proposed in the book "The Art of Computer Programming" by
    Donald E. Knuth.
    (Knuth, Donald E. (1997). The Art of Computer Programming.)

    Args:
        N (int): The length of the array to be sorted.

    Returns:
        list: A list of integers representing the gap sequence proposed by
            Knuth.
    """
    gaps, k = [], 0
    getKth = lambda k: (3 ** k - 1) // 2
    while getKth(k) < ceil(N / 3):
        gaps = [getKth(k)] + gaps
        k += 1
    return gaps


# different gap sequences
GAPS = {
    "ciura": getCiuraGaps,
    "shell": getShellGaps,
    "tokuda": getTokudaGaps,
    "knuth": getKnuthGaps
}


def shellSort(array, *args, gapType="ciura"):
    """
    Sort an array using Shell sort.

    The algorithm works by performing multiple passes over the array with a
    decreasing gap size. At each pass, the array is divided into subarrays of
    size equal to the gap. The subarrays are sorted using insertion sort. The
    gap size is reduced at each pass until it reaches 1, at which point the
    algorithm degenerates to a simple insertion sort.

    Args:
        array (list): the list to be sorted.
        gapType (str): specifies which gap sequence to use for the algorithm. Defaults to 'ciura'.

    Yields:
        tuple: a tuple containing the state of the array after each iteration of the algorithm. The tuple contains the following elements:
            - array (list): the current state of the array.
            - x (int): the index of the element being compared with the temporary value.
            - y (int): the index of the element being compared with the element at index x.
            - a (int): the index of the element being moved to a new location.
            - b (int): the index of the element's new location.
    """

    gaps = GAPS.get(gapType, "ciura")(len(array))
    for gap in gaps:
        for i in range(gap, len(array)):
            temp, j = array[i], i
            while j >= gap and array[j - gap] > temp:
                yield array, j, j - gap, -1, -1
                array[j] = array[j - gap]
                j -= gap
            yield array, -1, -1, i, j
            array[j] = temp
