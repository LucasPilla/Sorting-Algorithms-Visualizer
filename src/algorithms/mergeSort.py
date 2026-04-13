def mergeSort(array, left, right):
    """
    Merge sort.

    Divide-and-conquer: split the range in half, sort each half recursively, then
    merge the two sorted halves.

    Time complexity: O(n log n) time and O(n) auxiliary space for the merge (n is the range length).
    """
    if left < right:
        mid = int((left+right)/2)
        yield from mergeSort(array, left, mid)
        yield from mergeSort(array, mid+1, right)
        yield from merge(array, left, mid, right)


def merge(array, left, mid, right):
    """Merge two sorted contiguous ranges [left..mid] and [mid+1..right] in place."""
    L = array[left:mid+1]
    R = array[mid+1:right+1]
    i = 0
    j = 0
    k = left
    while i < len(L) and j < len(R):
         # The two lines below are not part of the algorithm
        yield array, (left + i, mid + j), (left, right)
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        array[k] = R[j]
        j += 1
        k += 1

