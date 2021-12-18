from random import randint

def quickSort_LR(array, low, high):
    if high - low > 0:
        pivot, left, right = array[randint(low, high)], low, high
        
        while left <= right:
            while array[left]  < pivot: left  += 1
            while array[right] > pivot: right -= 1
            
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
            
            yield array, pivot, high, low, -1
            
        yield from quickSort_LR(array, low, right)
        yield from quickSort_LR(array, left, high)
        
