from display import handleDrawing

def wiggleSort(array, *args):
        n = len(array)
        nums = array.copy()
        nums.sort()
    
        # 3 5 9 1 2 4
        
        # 1 2 3 4 5 9             2 1 4 3 9 5

        # 3 9 2 5 1 4
        
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
            

        # # Traverse all even elements
        # for i in range(0, n, 2):
            
        #     # If current even element is smaller than previous
        #     if (i> 0 and array[i] < array[i-1]):
        #         handleDrawing(array, i, i-1, -1, -1)
        #         array[i],array[i-1] = array[i-1],array[i]
            
        #     # If current even element is smaller than next
        #     if (i < n-1 and array[i] < array[i+1]):
        #         handleDrawing(array, i, i+1, -1, -1)
        #         array[i],array[i+1] = array[i+1],array[i]