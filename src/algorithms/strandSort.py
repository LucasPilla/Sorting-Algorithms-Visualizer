def merge(array, left, mid, right):
    """
    Merge two sorted subarrays of array:
    The left subarray is array[left..mid]
    The right subarray is array[mid+1..right]
    This function is used in Merge Sort algorithm.

    Args:
        array: list of elements to be sorted
        left: int, leftmost index of left subarray
        mid: int, rightmost index of left subarray
        right: int, rightmost index of right subarray

    Yields:
        A tuple of array and 4 integers representing the state of merge operation:
            - left+i: the index of the next item from left subarray to be compared
            - mid+j: the index of the next item from right subarray to be compared
            - left: the leftmost index of current merge iteration
            - right: the rightmost index of current merge iteration
    """

    L = array[left:mid+1]
    R = array[mid+1:right+1]
    i = 0
    j = 0
    k = left
    while i < len(L) and j < len(R):
        # The two lines below is not part of the algorithm
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

             
def helper(arr,n,start):
    """
    A helper function used in Strand Sort algorithm for sorting a list in-place.

    Args:
        arr: list to be sorted
        n: int, length of arr
        start: int, index of the first element in the sublist being sorted

    Yields:
        A tuple of arr and 4 integers representing the state of strand sort iteration:
            - i: the index of the current element in sublist being processed
            - count-1: the last element in sublist already sorted
            - start: the first index of current sublist
            - n-1: the last index of current sublist
    """

    if start==n:
        return

    
    i=start+1
    count=start+1

    while i<n:
        #next line not a part of algo
        yield arr,i,count-1,start,n-1
        if arr[i]>arr[count-1]:
            
            arr.insert(count,arr.pop(i))
            count+=1
        i+=1
    if start!=0:
        yield from merge(arr,0,start-1,count-1)
    yield from helper(arr,n,count)

def strandSort(arr,*args):
    """
    Sorts a list in-place using Strand Sort Algorithm.

    Strand sort is a sorting algorithm that sorts a list by repeatedly 
    pulling sorted sublists out of the original list and merging them together. 
    The algorithm works by repeatedly taking a sublist of elements from the original 
    list that are in increasing order, and removing these elements from the original list. 
    These sublists are then merged together in order to form a new, sorted list. 
    The process is repeated until the entire original list has been sorted.

    Args:
        arr: list to be sorted
        *args: additional arguments that are not used in the function.

    Yields:
        A sequence of tuples representing the state of Strand Sort Algorithm:
        Each tuple is a sequence of list arr and 4 integers, that represent the
        state of an iteration in the helper function. The last tuple contains 
        the fully sorted list.
    """

    size = len(arr)
    
    yield from helper(arr,size,0)