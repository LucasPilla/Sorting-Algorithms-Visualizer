def binaryinsertionSort(array, *args):
    """
    Sorts a given array in ascending order using Binary Insertion Sort Algorithm.

    Binary Insertion Sort is an optimized variant of traditional insertion sort, which uses Binary Search to find
    the appropriate position to insert an element in a sorted list. The algorithm has an average case time complexity
    of O(n^2), but with an optimized implementation of Binary Search, it can be reduced to O(n log n).

    Args:
        array (list): A list of comparable elements to be sorted in ascending order

    Yields:
        tuple: A tuple containing the sorted list after each iteration, the start and end index of the sublist being
               sorted in the current iteration, the index where the current element is inserted, and the index of the
               current element.

    Example:
        >>> array = [5, 2, 4, 6, 1, 3]
        >>> list(binaryinsertionSort(array))
        ([5, 2, 4, 6, 1, 3], 0, 0, 0, 0)
        ([2, 5, 4, 6, 1, 3], 1, 1, 0, 1)
        ([2, 4, 5, 6, 1, 3], 1, 2, 1, 2)
        ([2, 4, 5, 6, 1, 3], 2, 2, 1, 3)
        ([1, 2, 4, 5, 6, 3], 0, 3, 1, 4)
        ([1, 2, 3, 4, 5, 6], 0, 4, 2, 5)
    """
    for i in range(1, len(array)):
        val = array[i]
        j = binary_search(array, val, 0, i - 1, i)
        yield array, 0, i-1, j, i
        array[0:len(array)] = array[:j] + [val] + array[j:i] + array[i + 1:]


def binary_search(arr, val, start, end, current):
    """
    Searches for the appropriate position of a value in a sorted list using Binary Search Algorithm.

    Binary Search is an algorithm that uses a divide-and-conquer approach by comparing 
    the middle value of the list with the target value and eliminating half of the list 
    on each iteration.

    Args:
        arr (list): A list of comparable elements in ascending order
        val (any): The value to be searched in the list
        start (int): The start index of the sublist being searched
        end (int): The end index of the sublist being searched
        current (int): The index of the current element being inserted in the list

    Returns:
        int: The appropriate position of the value in the list.

    Example:
        >>> arr = [1, 2, 4, 5, 6]
        >>> binary_search(arr, 3, 0, 4, 4)
        2
    """
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = round((start + end) / 2)
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end, current)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1, current)
    else:
        return mid
