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

variants={}
for key in algorithmsDict.keys():
    variants[key]=["Generic"]
print(variants)
variants['shell'] = ['ShellGaps - θ(N^2)',"CiuraGaps - Unknown","TokudaGaps - Unknown", "KnuthGaps - θ(N^3/2)" ]