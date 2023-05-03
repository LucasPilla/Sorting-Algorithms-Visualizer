def countingSort(array, *args):
    """
    Counting Sort is an efficient, non-comparison-based sorting algorithm that works by counting
    the number of occurrences of each value in the input array and using this information to place
    each element in the right position in the output array. This implementation uses a separate
    array to keep track of the count of each integer value and then modifies this count array to
    determine the position of each element in the sorted output array.

    Time complexity: O(n + k), where n is the number of elements in the list 
    and k is the maximum value in the list

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
