from display import handleDrawing

def wiggleSort(array, *args):
        n = len(array)
        nums = array.copy()
        nums.sort()
    
        
        i = 1
        j = n - 1
        while(j >= 0):
            
            if(i >= n):
                i = 0

            if j == 0:
                handleDrawing(array, i, j, -1, -1, greenRows = array)    
            
            handleDrawing(array, i, j, -1, -1)
            array[i] = nums[j]
            i += 2
            j -= 1
            
