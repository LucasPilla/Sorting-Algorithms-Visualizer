def countingSort(array, *args):
    """
    Sorts an array of integers using the Counting Sort Algorithm.

    Counting Sort is an efficient, non-comparison-based sorting algorithm that works by counting
    the number of occurrences of each value in the input array and using this information to place
    each element in the right position in the output array. This implementation uses a separate
    array to keep track of the count of each integer value and then modifies this count array to
    determine the position of each element in the sorted output array.

    Args:
        array (list of int): The input array to be sorted.

    Yields:
        tuple: A tuple of the current state of the array and some indices that were modified in the
            last iteration of the algorithm. Specifically, each yielded value is a tuple of the form
            (array, x, y, i, j), where `array` is the current state of the array, `x` and `y` are
            indices of elements being compared or swapped, and `i` and `j` are indices of elements
            being updated in the count array. If no indices were modified in the last iteration,
            then the tuple is of the form (array, -1, -1, -1, -1).
    """
    size = len(array)
    A = array.copy()
    C = [0]*(max(A)+1)
    for i in range(size):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(0, size):
        yield array, C[A[size-i-1]]-1, -1, size-i-1, -1
        array[C[A[size-i-1]]-1] = A[size-i-1]
        C[A[size-i-1]] -= 1
