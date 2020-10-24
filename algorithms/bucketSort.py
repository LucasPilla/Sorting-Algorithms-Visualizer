from display import handleDrawing

def bucketSort(array, *args):
 
    bucket = []
    for i in range(len(array)):
        bucket.append([])
    n = len(bucket)
    
    for j in array:
        index_b = int(j/n)
        handleDrawing(array,j,-1,index_b,-1)
        bucket[index_b].append(j)
        
    
    for i in range(len(array)):
        #handleDrawing(array,i,-1,bucket[i],-1)
        bucket[i]=sorted(bucket[i])
    
    k=0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            handleDrawing(array,j,-1,i,-1)
            array[k]=bucket[i][j]
            k=k+1
