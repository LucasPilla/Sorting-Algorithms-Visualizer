def insertionSort(array, *args):
    mySortedRows = []
    size = len(array)
    for i in range(0, size):
        j = i-1
        key = array[i]
        mySortedRows.append(i)        
        while j >= 0 and array[j] > key:
            yield array, j, -1, i, -1
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    mySortedRows.clear()
