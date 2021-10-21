from random import randint


def bogoSort(array, *args):
    is_sorted = False
    arrayLen = len(array)
    count = 0
    while not is_sorted:
        count += 1
        for i in range(arrayLen):
            j = randint(0, arrayLen-1)
            array[i], array[j] = array[j], array[i]

        for k in range(len(array)-1):
            yield array, k, k+1, -1, -1
            if array[k] > array[k+1]:
                is_sorted = False
                break
            is_sorted = True
        if count > 4000:
            is_sorted= True
