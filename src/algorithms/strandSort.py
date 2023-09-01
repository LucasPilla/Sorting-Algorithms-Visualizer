def merge(array, left, mid, right):
    """
    Merge two sorted subarrays of array:
    The left subarray is array[left..mid]
    The right subarray is array[mid+1..right]
    This function is used in Merge Sort algorithm.
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
    Strand sort is a sorting algorithm that sorts a list by repeatedly 
    pulling sorted sublists out of the original list and merging them together. 
    The algorithm works by repeatedly taking a sublist of elements from the original 
    list that are in increasing order, and removing these elements from the original list. 
    These sublists are then merged together in order to form a new, sorted list. 
    The process is repeated until the entire original list has been sorted.

    Time complexity: O(n^2).
    
    """

    size = len(arr)
    
    yield from helper(arr,size,0)