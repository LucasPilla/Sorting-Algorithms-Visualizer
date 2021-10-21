def swap(array,i,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def oddevenSort(array, *args):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1,len(array)-1,2):
            yield array,i,i+1,-1,-1
            if array[i] > array[i+1]:
                swap(array,i,i+1)
                sorted = False

        for i in range(0,len(array)-1,2):
            yield array,i,i+1,-1,-1
            if array[i] > array[i+1]:
                swap(array,i,i+1)
                sorted = False
 