from display import handleDrawing

# bitonic sort for length not a power of two https://www.inf.hs-flensburg.de/lang/algorithmen/sortieren/bitonic/oddn.htm

def bitonicSort(array, *args):
    bitonic(array, 0, len(array), True)


def bitonic(array, low, cnt, dir):
    if cnt > 1:
        k = int(cnt / 2)
        bitonic(array, low, k, not dir)
        bitonic(array, low + k, cnt-k, dir)
        bitonicMerge(array, low, cnt, dir)


def compAndSwap(array, i, j, dir):
    if (dir and array[i] > array[j]) or (not dir and array[i] <= array[j]):
        array[i], array[j] = array[j], array[i]
        handleDrawing(array, i, -1, j, -1)


def bitonicMerge(array, low, cnt, dire):
    if cnt > 1:
        k = greatestPowerOfTwoLessThan(cnt)
        for i in range(low, low + cnt-k):
            compAndSwap(array, i, i + k, dire)
        bitonicMerge(array, low, k, dire)
        bitonicMerge(array, low + k, cnt-k, dire)

def greatestPowerOfTwoLessThan(n):
    k = 1
    while(k>0 and k<n):
        k = k<<1
    return k>>1
