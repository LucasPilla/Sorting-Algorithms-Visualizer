from math import floor

def stoogeSort(arr, l, h):
    """
    Stooge Sort Algorithm is a recursive sorting algorithm that sorts 
    an array by recursively sorting the first two-thirds of the array, 
    then the last two-thirds of the array, and finally the first two-thirds 
    of the array again. 
    
    Time complexity: O(n^(log 3/log 1.5)) time, which is approximately O(n^2.7095).
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
