import random
from random import randint

def quickSort(array, left, right):
    """
    Sorts an array in place using the Quicksort Algorithm.

    QuickSort is a popular sorting algorithm that uses a divide-and-conquer strategy. 
    It works by selecting a pivot element from the array and partitioning the other 
    elements into two sub-arrays, according to whether they are less than or greater 
    than the pivot. The process is then repeated on the two sub-arrays until the sub-arrays 
    contain only one element or are empty. The sub-arrays are then combined to form the final 
    sorted array. One of the benefits of QuickSort is that it has an average-case performance 
    of O(n log n), which makes it one of the fastest sorting algorithms in practice.

    Args:
        array (list): List of elements to be sorted.
        left (int): Index of the leftmost element of the array.
        right (int): Index of the rightmost element of the array.

    Yields:
        tuple: A tuple of the form (array, j, right, index, -1), representing the state of the array during the sorting process.

    """
    if left >= right:
        return
    index = left
    random_index = randint(left, right)
    array[right], array[random_index] = array[random_index], array[right]
    
    for j in range(left, right):
        yield array, j, right, index, -1
        if array[j] < array[right]:
            array[j], array[index] = array[index], array[j]
            index += 1
    array[index], array[right] = array[right], array[index]
    yield from quickSort(array, index + 1, right)
    yield from quickSort(array, left, index - 1)
