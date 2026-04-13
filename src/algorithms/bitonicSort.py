# bitonic sort for length not a power of two https://www.inf.hs-flensburg.de/lang/algorithmen/sortieren/bitonic/oddn.htm

def bitonicSort(array, *args):
    """
    Bitonic sort.

    Recursively forms bitonic sequences and merges them; this variant supports lengths
    that are not powers of two.

    Time complexity: O(n log² n) for this sequential implementation (n is the number of elements).
    """
    yield from bitonic(array, 0, len(array), True)


def bitonic(array, low, cnt, dir):
    """Recursively build a bitonic segment of length *cnt* starting at *low*."""
    if cnt > 1:
        k = int(cnt / 2)
        yield from bitonic(array, low, k, not dir)
        yield from bitonic(array, low + k, cnt-k, dir)
        yield from bitonicMerge(array, low, cnt, dir)


def compAndSwap(array, i, j, dir):
    """Swap *array[i]* and *array[j]* if their order disagrees with *dir*."""
    if (dir and array[i] > array[j]) or (not dir and array[i] <= array[j]):
        array[i], array[j] = array[j], array[i]
        yield array, i, -1, j, -1


def bitonicMerge(array, low, cnt, dire):
    """Merge a bitonic block of length *cnt* at *low* into sorted order per *dire*."""

    if cnt > 1:
        k = greatestPowerOfTwoLessThan(cnt)
        for i in range(low, low + cnt-k):
            yield from compAndSwap(array, i, i + k, dire)
        yield from bitonicMerge(array, low, k, dire)
        yield from bitonicMerge(array, low + k, cnt-k, dire)

def greatestPowerOfTwoLessThan(n):
    """Largest power of two strictly less than *n* (used for odd-length merges)."""

    k = 1
    while(k > 0 and k < n):
        k = k << 1
    return k >> 1

