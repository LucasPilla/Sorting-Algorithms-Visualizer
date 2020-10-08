from display import handleDrawing
from math import ceil, floor


def getShellGaps(N):
    # doi:10.1145/368370.368387
    gaps, k = [], 0
    getKth = lambda k: floor(N / 2 ** k)
    while getKth(k) > 1:
        gaps.append(getKth(k))
        k += 1
    return gaps + [1]


def getCiuraGaps(*args):
    # doi:10.1007/3-540-44669-9_12
    return [1750, 701, 301, 132, 57, 23, 10, 4, 1]


def getTokudaGaps(N):
    # N. Tokuda, An Improved Shellsort, IFIP Transactions, A-12 (1992) 449-457
    gaps, k = [], 1
    getKth = lambda k: ceil((9 * (9 / 4) ** (k - 1) - 4) / 5)
    while getKth(k) <= N:
        gaps = [getKth(k)] + gaps
        k += 1
    return gaps


def getKnuthGaps(N):
    # Knuth, Donald E. (1997). The Art of Computer Programming.
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
    gaps = GAPS.get(gapType, "ciura")(len(array))
    for gap in gaps:
        for i in range(gap, len(array)):
            temp, j = array[i], i
            while j >= gap and array[j - gap] > temp:
                handleDrawing(array, j, j - gap, -1, -1)
                array[j] = array[j - gap]
                j -= gap
            handleDrawing(array, -1, -1, i, j)
            array[j] = temp
