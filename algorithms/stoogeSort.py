from display import handleDrawing
from math import floor


def stoogeSort(arr, l, h): 
    if l >= h: 
        return

    if arr[l]>arr[h]: 
        
        middle = floor((h + l) / 2)
        handleDrawing(arr, l, h, middle, -1)
        t = arr[l] 
        arr[l] = arr[h] 
        arr[h] = t 

    if h-l + 1 > 2: 
        t = (int)((h-l + 1)/3) 

        stoogeSort(arr, l, (h-t)) 
        stoogeSort(arr, l + t, (h)) 
        stoogeSort(arr, l, (h-t)) 
