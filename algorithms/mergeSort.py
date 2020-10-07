from display import handleDrawing


def mergeSort(array, left, right):
    if left < right:
        mid = int((left+right)/2)
        mergeSort(array, left, mid)
        mergeSort(array, mid+1, right)
        merge(array, left, mid, right)


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
