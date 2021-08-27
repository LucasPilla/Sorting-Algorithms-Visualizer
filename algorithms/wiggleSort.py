from display import handleDrawing

def wiggleSort(array, *args):
        n = len(array)

        for i in range(0, n, 2):
            
            # If current even element is smaller than previous
            if (i> 0 and array[i] < array[i-1]):
                handleDrawing(array, i, i-1, -1, -1)
                array[i],array[i-1] = array[i-1],array[i]
            
            # If current even element is smaller than next
            if (i < n-1 and array[i] < array[i+1]):
                handleDrawing(array, i, i+1, -1, -1)
                array[i],array[i+1] = array[i+1],array[i]