from math import ceil, floor


def getShellGaps(N):
    """
    The gap sequence is computed as follows: starting with the largest gap
    possible, divide it by 2 at each iteration until reaching 1. The resulting
    gaps are returned in decreasing order.

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

    Returns:
        list: A list of integers representing the gap sequence proposed by
            Ciura.
    """
    return [1750, 701, 301, 132, 57, 23, 10, 4, 1]


def getTokudaGaps(N):
    """
    Compute gap sequence proposed by Tokuda.

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

    Time complexity: O(n^2). It depends on the increment sequence used.

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
