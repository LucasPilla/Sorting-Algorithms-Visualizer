def pancakeSort(array, *args):
    """
    Sorts an array using the Pancake Sort Algorithm and yields the state of the array after each flip.

    Pancake Sort Algorithm is a sorting algorithm that works by repeatedly flipping the largest unsorted 
    element to the front of the unsorted portion of the list, and then flipping the entire unsorted portion 
    of the list to move the largest element to its correct position. This process is repeated until the entire list is sorted.

    Args:
        array (list): The list to be sorted.

    Yields:
        tuple: A tuple containing the current state of the array after each flip. The tuple has the format
        (array, max_index, -1, -1, -1), where array is the current state of the array, max_index is the index of the
        maximum value in the unsorted portion of the array, and the other values are set to -1.

    """
    for i in range(len(array)):
        max_index = array.index(max(array[:len(array) - i]))
        yield array, max_index, -1, -1, -1
        flip(array, max_index)
        yield array, 0, -1, -1, -1
        flip(array, len(array) - 1 - i)
        yield array, -1 , -1, len(array) - 1 - i, -1


def flip(array, n):
    """
    Flips the first n elements of an array.

    Args:
        array (list): The list to be flipped.
        n (int): The number of elements to be flipped.

    """
    for i in range(n):
        if i >= n - i:
            break
        array[n - i], array[i] = array[i], array[n - i]
