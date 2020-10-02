# Handles the drawing and controls while executing the algorithm
from display import handleDrawing
from random import randint

def bubbleSort(array, *args):
    size = len(array)
    for i in range(size):
        for j in range(size - i - 1):
            handleDrawing(array, j, j+1, -1, -1)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


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


def quickSort(array, left, right):
    if left >= right:
        return
    index = left
    for j in range(left, right):
        # The four lines below are not part of the algorithm
        handleDrawing(array, j, right, index, -1)
        if array[j] < array[right]:
            array[j], array[index] = array[index], array[j]
            index += 1
    array[index], array[right] = array[right], array[index]
    quickSort(array, index + 1, right)
    quickSort(array, left, index - 1)


def insertionSort(array, *args):
    size = len(array)
    for i in range(1, size):
        j = i-1
        key = array[i]
        while j >= 0 and array[j] > key:
            handleDrawing(array, j, -1, i, -1)
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key


def selectionSort(array, *args):
    size = len(array)
    for i in range(size-1):
        smallIndex = i
        for j in range(i, size):
            handleDrawing(array, j, -1, i, -1)
            if array[j] < array[smallIndex]:
                smallIndex = j
        array[i], array[smallIndex] = array[smallIndex], array[i]


def countingSort(array, *args):
    size = len(array)
    A = array.copy()
    C = [0]*size
    for i in range(size):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(0, size):
        handleDrawing(array, C[A[size-i-1]]-1, -1, size-i-1, -1)
        array[C[A[size-i-1]]-1] = A[size-i-1]
        C[A[size-i-1]] -= 1


def cocktailSort(array, *args):
    n = len(array)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
        swapped = False
        for i in range (start, end):
            handleDrawing(array,i,i+1,-1,-1)
            if (array[i] > array[i+1]) :
                array[i], array[i+1]= array[i+1], array[i]
                swapped=True
        if (swapped==False):
            break
        swapped = False
        end = end-1
        for i in range(end-1, start-1,-1):
            handleDrawing(array,-1,-1,i,i+1)
            if (array[i] > array[i+1]):
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
        start = start+1

def bogoSort(array, *args):
    is_sorted = False
    arrayLen = len(array)
    while not is_sorted:
        for i in range(arrayLen):
            j = randint(0, arrayLen-1)
            array[i], array[j] = array[j], array[i]

        for k in range(len(array)-1):
            handleDrawing(array, k, k+1, -1, -1)
            if array[k] > array[k+1]:
                is_sorted = False
                break
            is_sorted = True
                

def heapify(array, count):
    start = (count-1) // 2
    while start >= 0:
        siftDown(array, start, count - 1)
        start -= 1

def siftDown(array, start, end):
    root = start
    while 2 * root + 1 <= end:
        child = 2 * root + 1
        swap = root
        if array[swap] < array[child]:
            swap = child
        if child + 1 <= end and array[swap] < array[child + 1]:
            swap = child + 1
        if swap == root:
            return
        else:
            handleDrawing(array, root, swap, -1, -1)
            array[root], array[swap] = array[swap], array[root]
            root = swap

def heapSort(array, *args):
    heapify(array, len(array))
    end = len(array) - 1
    while end > 0:
        handleDrawing(array, -1, -1, 0, end, )
        array[end], array[0] = array[0], array[end]
        end -= 1
        siftDown(array, 0, end)
        
algorithmsDict = {
    'insertionsort': insertionSort,
    'bubblesort': bubbleSort,
    'selectionsort': selectionSort,
    'mergesort': mergeSort,
    'quicksort': quickSort,
    'countingsort': countingSort,
    'cocktailsort': cocktailSort,
    'bogosort': bogoSort,
    'heapsort': heapSort,
}


def runAlgorithm(algorithm, array):
    return algorithmsDict[algorithm](array, 0, len(array)-1)
