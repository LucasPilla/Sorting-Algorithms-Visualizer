from display import handleDrawing


def counting_Sort(array, exp1):

    n = len(array)
    output = []
    for i in range(0,n):
        output.append(array[i])
    count = [0] * (10)
    for i in range(0, n):
        index = (array[i] / exp1)
        count[int(index % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (array[i] / exp1)
        handleDrawing(output, count[int(index % 10)]-1, -1, int(index % 10), -1)
        output[count[int(index % 10)] - 1] = array[i]
        count[int(index % 10)] -= 1
        i -= 1
    i = 0
    if(array != output):
        pass
    else:
        return(0)
    for i in range(0, len(array)):
        array[i] = output[i]
    del(output)


def radixSort(array, *args):

    max1 = max(array)
    g = 1
    exp = 1
    while max1 / exp > 0:
        g = counting_Sort(array, exp)
        if(g == 0):
            break
        exp *= 10
