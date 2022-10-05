def introSort(array):
    maxdepth = (len(array).bit_length() - 1)*2
    introsort_helper(array, 0, len(array), maxdepth)
 
def introsort_helper(array, start, end, maxdepth):
    if end - start <= 1:
        return
    elif maxdepth == 0:
        heapsort(array, start, end)
    else:
        p = partition(array, start, end)
        introsort_helper(array, start, p + 1, maxdepth - 1)
        introsort_helper(array, p + 1, end, maxdepth - 1)
 
def partition(array, start, end):
    pivot = array[start]
    i = start - 1
    j = end
 
    while True:
        i = i + 1
        while array[i] < pivot:
            i = i + 1
        j = j - 1
        while array[j] > pivot:
            j = j - 1
 
        if i >= j:
            return j
 
        swap(array, i, j)
 
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
 
def heapsort(array, start, end):
    build_max_heap(array, start, end)
    for i in range(end - 1, start, -1):
        swap(array, start, i)
        max_heapify(array, index=0, start=start, end=i)
 
def build_max_heap(array, start, end):
    def parent(i):
        return (i - 1)//2
    length = end - start
    index = parent(length - 1)
    while index >= 0:
        max_heapify(array, index, start, end)
        index = index - 1
 
def max_heapify(array, index, start, end):
    def left(i):
        return 2*i + 1
    def right(i):
        return 2*i + 2
 
    size = end - start
    l = left(index)
    r = right(index)
    if (l < size and array[start + l] > array[start + index]):
        largest = l
    else:
        largest = index
    if (r < size and array[start + r] > array[start + largest]):
        largest = r
    if largest != index:
        swap(array, start + largest, start + index)
        max_heapify(array, largest, start, end)