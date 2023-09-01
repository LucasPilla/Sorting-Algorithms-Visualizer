def mergeSort(array, left, right):
    """
    Sorts a given array using the Merge Sort algorithm.

    Merge Sort algorithm is a divide and conquer algorithm 
    that recursively divides the input list in half and sorts 
    each half before merging them back together. This process 
    is repeated until the entire list is sorted. 
    
    Time complexity: O(nlog²n).
    """
    if left < right:
        mid = int((left+right)/2)
        yield from mergeSort(array, left, mid)
        yield from mergeSort(array, mid+1, right)
        yield from merge(array, left, mid, right)


def merge(array, left, mid, right):
    """
    Merges two sorted arrays into a single sorted array.
    """
    L = array[left:mid+1]
    R = array[mid+1:right+1]
    i = 0
    j = 0
    k = left
    while i < len(L) and j < len(R):
         # The two lines below are not part of the algorithm
        yield array, left+i, mid+j, left, right
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

