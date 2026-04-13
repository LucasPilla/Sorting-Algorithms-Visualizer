import random
from random import randint

def quickSort(array, left, right):
    """
    Quicksort (Lomuto-style partition with a randomly chosen pivot).

    Partitions elements around a pivot, then recursively sorts the left and right parts.

    Time complexity: O(n log n) expected time; O(n²) worst case (e.g. adversarial input or poor pivots). n is the subarray length.
    """
    if left >= right:
        return
    index = left
    random_index = randint(left, right)
    array[right], array[random_index] = array[random_index], array[right]
    
    for j in range(left, right):
        yield array, (j, right), (index,)
        if array[j] < array[right]:
            array[j], array[index] = array[index], array[j]
            index += 1
    array[index], array[right] = array[right], array[index]
    yield from quickSort(array, index + 1, right)
    yield from quickSort(array, left, index - 1)
