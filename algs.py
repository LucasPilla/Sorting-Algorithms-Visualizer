from algorithms import *
from algorithms.bitonicSort import bitonicSort
from algorithms.pancakeSort import pancakeSort

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
    'pancakesort': pancakeSort
}


def runAlgorithm(algorithm, array):
    return algorithmsDict[algorithm](array, 0, len(array)-1)
