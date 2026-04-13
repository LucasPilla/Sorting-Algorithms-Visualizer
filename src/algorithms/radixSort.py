def counting_Sort(array, exp1):
    """
    Stable counting sort on one base-10 digit (used as a radix-sort pass).

    Returns:
        0 if a pass made no change, else None after copying back into *array*.
    """
    n = len(array)
    output = []
    for i in range(0,n):
        output.append(array[i])
    count = [0] * (10)
    for i in range(0, n):
        index = (array[i] / exp1)
        count[int(index % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (array[i] / exp1)
        yield output, count[int(index % 10)]-1, -1, int(index % 10), -1
        output[count[int(index % 10)] - 1] = array[i]
        count[int(index % 10)] -= 1
        i -= 1
    i = 0
    if(array != output):
        pass
    else:
        return 0
    for i in range(0, len(array)):
        array[i] = output[i]
    del(output)


def radixSort(array, *args):
    """
    Radix sort (LSD, base 10).

    Runs stable counting sorts from the least significant digit to the most significant
    digit until all digits of the maximum value are processed.

    Time complexity: O(d · n) for these passes, with d = O(log₁₀(max)) digit rounds (n is the number of elements).
    """
    max1 = max(array)
    g = 1
    exp = 1
    while max1 / exp > 0:
        g = yield from counting_Sort(array, exp)
        if g==0:
            break
        exp *= 10
