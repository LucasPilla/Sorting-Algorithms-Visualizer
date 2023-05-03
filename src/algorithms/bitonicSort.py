# bitonic sort for length not a power of two https://www.inf.hs-flensburg.de/lang/algorithmen/sortieren/bitonic/oddn.htm

def bitonicSort(array, *args):
    """
    Bitonic sort is a sorting algorithm that sorts a sequence 
    of numbers by recursively dividing 
    the sequence into two bitonic sequences, 
    sorting each sequence in a specific order, 
    and merging the two sequences in a bitonic manner 
    until the entire sequence is sorted in ascending order.

    Time complexity: O(n log² n)
    """
    yield from bitonic(array, 0, len(array), True)


def bitonic(array, low, cnt, dir):
    """
    Recursively divide the input array into two halves, sort each half independently
    in the opposite direction of the other half, and then merge the two halves back
    together in a bitonic manner.
    """
    if cnt > 1:
        k = int(cnt / 2)
        yield from bitonic(array, low, k, not dir)
        yield from bitonic(array, low + k, cnt-k, dir)
        yield from bitonicMerge(array, low, cnt, dir)


def compAndSwap(array, i, j, dir):
    """
    Compare the elements at indices i and j in the input array and swap them
    if they are not in the correct order (as determined by the dir parameter).
    """
    if (dir and array[i] > array[j]) or (not dir and array[i] <= array[j]):
        array[i], array[j] = array[j], array[i]
        yield array, i, -1, j, -1


def bitonicMerge(array, low, cnt, dire):
    """
    Merge two bitonic sequences in the given array.

    This function recursively divides the sequence into two parts,
    calls itself for each part, and then merges them into a single
    bitonic sequence.
    """

    if cnt > 1:
        k = greatestPowerOfTwoLessThan(cnt)
        for i in range(low, low + cnt-k):
            yield from compAndSwap(array, i, i + k, dire)
        yield from bitonicMerge(array, low, k, dire)
        yield from bitonicMerge(array, low + k, cnt-k, dire)

def greatestPowerOfTwoLessThan(n):
    """
    Returns:
        the greatest power of 2 that is less than the
        input number n. This is used in the bitonic sort algorithm to find
        the correct sequence size to merge.
    """

    k = 1
    while(k > 0 and k < n):
        k = k << 1
    return k >> 1

