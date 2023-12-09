from algorithms import *
#Sorted by best case complexity 
# (fastest to slowest),then alphabetically


algorithmsDict = {'bogo'            : bogoSort, #O(n)
                  'bubble'          : bubbleSort,
                  'cocktail'        : cocktailSort,
                  'gnome'           : gnomeSort,
                  'insertion'       : insertionSort,
                  'odd-even'        : oddevenSort,
                  'pancake'         : pancakeSort,
                  'tim'             : timSort,
                  'bucket'          : bucketSort, #O(n+k)
                  'counting'        : countingSort,
                  'pigeonhole'      : pigeonholeSort,
                  'binary insertion': binaryinsertionSort, #O(nlog n)
                  'comb'            : combSort,
                  'heap'            : heapSort,
                  'merge'           : mergeSort,
                  'quick'           : quickSort,
                  'shell'           : shellSort,
                  'strand'          : strandSort,
                  'tree'            : treeSort,
                  'bitonic'         : bitonicSort, #O(n log^2n)
                  'radix'           : radixSort, #O(nk)
                  'cycle'           : cycleSort, #O(n^2)
                  'exchange'        : exchangeSort,
                  'selection'       : selectionSort,
                  'stooge'          : stoogeSort #O(n^2.71)
                 }

