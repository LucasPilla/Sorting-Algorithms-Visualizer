from math import floor

def stoogeSort(arr, l, h):
    """
    Sorts the array using the Stooge Sort Algorithm.

    Stooge Sort Algorithm is a recursive sorting algorithm that sorts 
    an array by recursively sorting the first two-thirds of the array, 
    then the last two-thirds of the array, and finally the first two-thirds 
    of the array again. 
    
    It is named after James Stooge, who was a member of a 
    comedy trio called "The Three Stooges." In each recursive call, if the first 
    element of the subarray is greater than the last element, it swaps these two 
    elements. 
    
    The algorithm runs in O(n^(log 3/log 1.5)) time, which is approximately O(n^2.7095), 
    making it slower than most other sorting algorithms.

    Args:
        arr (list): The array to be sorted.
        l (int): The starting index of the array.
        h (int): The ending index of the array.

    Yields:
        tuple: A tuple containing the array, the starting index of the subarray, the ending index of the subarray, 
        the index of the middle element in the subarray, and the index of the element being swapped. 

    """

    if l >= h:
        return

    if arr[l] > arr[h]:
        middle = floor((h + l) / 2)
        yield arr, l, h, middle, -1
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t

    if h-l + 1 > 2:
        t = (int)((h-l + 1)/3)

        yield from stoogeSort(arr, l, (h-t))
        yield from stoogeSort(arr, l + t, (h))
        yield from stoogeSort(arr, l, (h-t))
