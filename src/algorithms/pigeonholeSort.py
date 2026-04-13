def pigeonholeSort(array, *args):
    """
    Pigeonhole sort.

    Counts how many of each value occur, then writes them back in order. Best when
    the value span is small compared to n.

    Time complexity: O(n + k), where n is the number of elements and k is (max − min + 1).
    """

    minV = min(array)
    maxV = max(array)
    A = array.copy()
    size = maxV - minV + 1
    C = [0] * (size)
    i = 0
    for x in array:
        yield A, i, -1, -1, -1
        C[x - minV] += 1
        A[i] = A[i] / (C[x - minV] + 1)
        i += 1

    i = 0
    for count in range(size):
        while C[count] > 0:
            yield A, i - 1, -1, C[count] * minV, -1
            C[count] -= 1
            array[i] = count + minV
            A[i] = array[i]
            i += 1
