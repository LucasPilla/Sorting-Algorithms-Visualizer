import random

def quickSort(array, left, right):
    """
    QuickSort works by selecting a pivot element from the array and partitioning the other 
    elements into two sub-arrays, according to whether they are less than or greater 
    than the pivot. The process is then repeated on the two sub-arrays until the sub-arrays 
    contain only one element or are empty. The sub-arrays are then combined to form the final 
    sorted array. 

    Time complexity: O(nlog²n).
    
    :param array: The list to be sorted.
    :param left: The index of the left boundary of the subarray.
    :param right: The index of the right boundary of the subarray.
    :return: The sorted list.
    """
    if left >= right:
        return

    index = left
    random_index = random.randint(left, right)
    array[right], array[random_index] = array[random_index], array[right
    
    pivot = array[right]

    for j in range(left, right):
        yield array, j, right, index, -1
        if array[j] < pivot:
            array[j], array[index] = array[index], array[j]
            index += 1

    array[index], array[right] = array[right], array[index]

    yield from quickSort(array, left, index - 1)
    yield from quickSort(array, index + 1, right)

