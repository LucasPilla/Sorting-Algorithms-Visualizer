def exchangeSort(array, *args):
    size = len(array)
    for i in range(size - 1):
        for j in range(i + 1, size):
            yield array, i, j, -1, -1
            if array[i] > array[j]:
                array[j], array[i] = array[i], array[j]
