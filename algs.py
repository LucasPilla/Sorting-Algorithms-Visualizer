from algorithms import *
from algorithms.binaryinsertionSort import binaryinsertionSort
from algorithms.bitonicSort import bitonicSort
from algorithms.pancakeSort import pancakeSort
from algorithms.timSort import timSort
from algorithms.stoogeSort import stoogeSort
from algorithms.strandSort import strandSort
from algorithms.oddevenSort import oddevenSort


algorithmsDict = {'insertion'       : [insertionSort, "O(n^2)"],
                  'bubble'          : [bubbleSort, "O(n^2)"],
                  'selection'       : [selectionSort, "O(n^2)"],
                  'merge'           : [mergeSort, "O(nlogn)"],
                  'quick'           : [quickSort, "O(nlogn)"],
                  'counting'        : [countingSort, "O(n)"],
                  'cocktail'        : [cocktailSort, "O(n^2)"],
                  'cycle'           : [cycleSort, "O(n^2)"],
                  'bogo'            : [bogoSort, "inf"],
                  'heap'            : [heapSort, "O(nlogn)"],
                  'radix'           : [radixSort, "O(nk)"],
                  'shell'           : [shellSort, "O((nlogn))^2)"],
                  'gnome'           : [gnomeSort, "O(n^2)"],
                  'comb'            : [combSort, "O(n^2)"],
                  'bitonic'         : [bitonicSort, "O(nlog^2)"],
                  'pancake'         : [pancakeSort, "O(nlogn)"],
                  'binary insertion': [binaryinsertionSort, "O(n^2)"],
                  'bucket'          : [bucketSort, "O(n+k)"],
                  'tim'             : [timSort, "O(nlogn)"],
                  'stooge'          : [stoogeSort, "O(nlog 3 / log 1.5 )"],
                  'strand'          : [strandSort, "O(n^2)"],
                  'odd-even'        : [oddevenSort, "O(n^2)"]}

timeComplexityOpt = ["All", "O(n)", "O(nlogn)", "O(nlog^2)", "O(n^2)", "O(nlog 3 / log 1.5 )", "inf"]


def runAlgorithm(algorithm, array):
    return algorithmsDict[algorithm][0](array, 0, len(array) - 1)


def returnAlgoList(current_tc):
    if current_tc != "All":
        temp = []
        for i in algorithmsDict:
            if algorithmsDict[i][1] == current_tc:
                temp.append(i)
        return temp
    else:
        return list(algorithmsDict.keys())
