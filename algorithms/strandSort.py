from display import handleDrawing

def merge(array, left, mid, right):
    L = array[left:mid+1]
    R = array[mid+1:right+1]
    i = 0
    j = 0
    k = left
    while i < len(L) and j < len(R):
        # The two lines below is not part of the algorithm
        handleDrawing(array, left+i, mid+j, left, right)
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        array[k] = R[j]
        j += 1
        k += 1

             
def helper(arr,n,start):

    if start==n:
        return

    
    i=start+1
    count=start+1

    while i<n:
        #next line not a part of algo
        handleDrawing(arr,i,count-1,start,n-1)
        if arr[i]>arr[count-1]:
            
            arr.insert(count,arr.pop(i))
            count+=1
        i+=1
    if start!=0:
        op = merge(arr,0,start-1,count-1)
    helper(arr,n,count)

def strandSort(arr,*args):
    size = len(arr)
    
    helper(arr,size,0)