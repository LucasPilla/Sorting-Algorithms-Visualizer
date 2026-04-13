def countingSort(array, *args):
    """
    Counting sort.

    Counts occurrences of each key, turns counts into positions, then places each element
    in sorted order. Assumes non-negative integer keys; uses a bucket of size max(A) + 1.

    Time complexity: O(n + k), where n is len(array) and k is max(A) + 1 for this implementation.
    """
    size = len(array)
    A = array.copy()
    C = [0]*(max(A)+1)
    for i in range(size):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(0, size):
        yield array, (C[A[size - i - 1]] - 1,), (size - i - 1,)
        array[C[A[size-i-1]]-1] = A[size-i-1]
        C[A[size-i-1]] -= 1
