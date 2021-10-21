from math import floor


def stoogeSort(arr, l, h): 
    if l >= h: 
        return

    if arr[l]>arr[h]: 
        
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
