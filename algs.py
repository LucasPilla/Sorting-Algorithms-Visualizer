from algorithms import *


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
    'radixsort': radixSort,
    'shellsort': shellSort,
    'gnomesort': gnomeSort
}


def runAlgorithm(algorithm, array):
    return algorithmsDict[algorithm](array, 0, len(array)-1)
