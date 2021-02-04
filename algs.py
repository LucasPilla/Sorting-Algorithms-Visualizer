from algorithms import *
from algorithms.binaryinsertionSort import binaryinsertionSort
from algorithms.bitonicSort import bitonicSort
from algorithms.pancakeSort import pancakeSort
from algorithms.timSort import timSort
from algorithms.stoogeSort import stoogeSort
from algorithms.strandSort import strandSort

algorithmsDict = {
    'insertionsort': insertionSort,
    'bubblesort': bubbleSort,
    'selectionsort': selectionSort,
    'mergesort': mergeSort,
    'quicksort': quickSort,
    'countingsort': countingSort,
    'cocktailsort': cocktailSort,
    'cyclesort': cycleSort,
    'bogosort': bogoSort,
    'heapsort': heapSort,
    'radixsort': radixSort,
    'shellsort': shellSort,
    'gnomesort': gnomeSort,
    'combsort': combSort,
    'bitonicsort': bitonicSort,
    'pancakesort': pancakeSort,
    'binaryinsertionsort': binaryinsertionSort,
    'bucketsort': bucketSort,
    'timsort' :timSort,
    'stoogesort': stoogeSort,
    'strandsort':strandSort
}

algorithmsVarDict = {
    'insertionsort': ['insertionsort','shellsort','binaryinsertionsort','timsort'],
    'bubblesort':['bubblesort','cocktailsort','combsort','shellsort'],
    'selectionsort':['selectionsort','heapsort','cocktailsort','pancakesort'],
    'mergesort':['mergesort','timsort'],
    'quicksort':['quicksort'],
    'countingsort':['countingsort'],
    'cyclesort':['cyclesort'],
    'bogosort':['bogosort'],
    'radixsort':['radixsort'],
    'gnomesort':['gnomesort'],
    'bitonicsort':['bitonicsort'],
    'bucketsort':['bucketsort'],
    'stoogesort':['stoogesort'],
}

def runAlgorithm(algorithm, array):
    return algorithmsDict[algorithm](array, 0, len(array)-1)
