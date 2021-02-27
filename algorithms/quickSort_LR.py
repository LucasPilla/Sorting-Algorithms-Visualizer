from display import handleDrawing

def quickSort_LR(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quickSort_LR(array, low, p)
        quickSort_LR(array, p + 1, high)

def partition(array, low, high):
    pivot = array[low]
    i     = low - 1
    j     = high + 1
    
    while True:
        i += 1
        while array[i] < pivot: i += 1
        
        j -= 1
        while array[j] > pivot: j -= 1
        
        handleDrawing(array, j, high, low, -1)
        if i >= j: return j
        array[i], array[j] = array[j], array[i]
