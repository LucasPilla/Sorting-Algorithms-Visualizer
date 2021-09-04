from algorithms import *
from algorithms.binaryinsertionSort import binaryinsertionSort
from algorithms.bitonicSort import bitonicSort
from algorithms.pancakeSort import pancakeSort
from algorithms.timSort     import timSort
from algorithms.stoogeSort  import stoogeSort
from algorithms.strandSort  import strandSort
from algorithms.oddevenSort import oddevenSort
from algorithms.exchangeSort import exchangeSort


algorithmsDict = {'insertion'       : insertionSort,
                  'bubble'          : bubbleSort,
                  'selection'       : selectionSort,
                  'merge'           : mergeSort,
                  'quick'           : quickSort,
                  'counting'        : countingSort,
                  'cocktail'        : cocktailSort,
                  'cycle'           : cycleSort,
                  'bogo'            : bogoSort,
                  'heap'            : heapSort,
                  'radix'           : radixSort,
                  'shell'           : shellSort,
                  'gnome'           : gnomeSort,
                  'comb'            : combSort,
                  'bitonic'         : bitonicSort,
                  'pancake'         : pancakeSort,
                  'binary insertion': binaryinsertionSort,
                  'bucket'          : bucketSort,
                  'tim'             : timSort,
                  'stooge'          : stoogeSort,
                  'strand'          : strandSort,
                  'odd-even'        : oddevenSort,
                  'pigeonhole'      : pigeonholeSort,
                  'exchange'        : exchangeSort}

