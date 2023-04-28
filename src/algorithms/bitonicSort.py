# bitonic sort for length not a power of two https://www.inf.hs-flensburg.de/lang/algorithmen/sortieren/bitonic/oddn.htm

def bitonicSort(array, *args):
    """
    Perform Bitonic Sort on the input array.

    Bitonic sort is an algorithm that recursively sorts the input array by
    dividing it into two halves, sorting each half independently (in the
    opposite direction of the other half), and then merging the two halves
    back together in a bitonic manner. The algorithm repeats this process
    until the entire array is sorted in ascending order.

    Parameters:
    array (list): The list to be sorted

    Yields:
    tuple: A tuple containing the current state of the array, as well as the
           indices of any elements that were swapped during the current iteration
           of the sort

    """
    yield from bitonic(array, 0, len(array), True)


def bitonic(array, low, cnt, dir):
    """
    Recursively divide the input array into two halves, sort each half independently
    in the opposite direction of the other half, and then merge the two halves back
    together in a bitonic manner.

    Parameters:
    array (list): The list to be sorted
    low (int): The starting index of the current sub-array
    cnt (int): The length of the current sub-array
    dir (bool): The direction in which to sort the current sub-array (True for ascending,
                False for descending)

    Yields:
    tuple: A tuple containing the current state of the array, as well as the
           indices of any elements that were swapped during the current iteration
           of the sort

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

    Parameters:
    array (list): The list to be sorted
    i (int): The index of the first element to compare
    j (int): The index of the second element to compare
    dir (bool): The direction in which to sort the current sub-array (True for ascending,
                False for descending)

    Yields:
    tuple: A tuple containing the current state of the array, as well as the
           indices of any elements that were swapped during the current iteration
           of the sort

    """
    if (dir and array[i] > array[j]) or (not dir and array[i] <= array[j]):
        array[i], array[j] = array[j], array[i]
        yield array, i, -1, j, -1


def bitonicMerge(array, low, cnt, dire):
    """Merge two bitonic sequences in the given array.

    This function recursively divides the sequence into two parts,
    calls itself for each part, and then merges them into a single
    bitonic sequence.

    Args:
        array (list): A list of comparable elements to be sorted.
        low (int): The starting index of the sequence to be sorted.
        cnt (int): The length of the sequence to be sorted.
        dire (bool): A boolean indicating the sorting direction.

    Yields:
        tuple: A tuple containing the state of the array and the
        indices of the two elements that were compared and possibly
        swapped in the last operation. If no swap was made, the
        corresponding index is -1.

    """
    if cnt > 1:
        k = greatestPowerOfTwoLessThan(cnt)
        for i in range(low, low + cnt-k):
            yield from compAndSwap(array, i, i + k, dire)
        yield from bitonicMerge(array, low, k, dire)
        yield from bitonicMerge(array, low + k, cnt-k, dire)

def greatestPowerOfTwoLessThan(n):
    """Return the greatest power of 2 less than n.

    This function returns the greatest power of 2 that is less than the
    input number n. This is used in the bitonic sort algorithm to find
    the correct sequence size to merge.

    Args:
        n (int): The input number.

    Returns:
        int: The greatest power of 2 that is less than n.

    """
    k = 1
    while(k > 0 and k < n):
        k = k << 1
    return k >> 1

