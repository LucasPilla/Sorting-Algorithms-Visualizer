def counting_Sort(array, exp1):
    """
    Perform counting sort on the given array based on a given exponent value.

    Returns:
        int: Returns 0 if the input array and the sorted array are the same, otherwise None.
    """
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
        yield output, count[int(index % 10)]-1, -1, int(index % 10), -1
        output[count[int(index % 10)] - 1] = array[i]
        count[int(index % 10)] -= 1
        i -= 1
    i = 0
    if(array != output):
        pass
    else:
        return 0
    for i in range(0, len(array)):
        array[i] = output[i]
    del(output)


def radixSort(array, *args):
    """
    Sort the input list of integers using Radix Sort Algorithm.

    Radix Sort Algorithm sorts a list of integers by grouping them 
    by individual digits that share the same place value and position. 
    It starts by sorting the list based on the least significant digit, 
    then gradually moves to the most significant digit until the entire 
    list is sorted.
    
    Time complexity: O(d * (n + k)), where d is the number of digits in the 
    maximum element, n is the number of elements in the list, 
    and k is the range of values that the digits can take.
    """
    max1 = max(array)
    g = 1
    exp = 1
    while max1 / exp > 0:
        g = yield from counting_Sort(array, exp)
        if g==0:
            break
        exp *= 10
