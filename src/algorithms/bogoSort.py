from random import randint


def bogoSort(array, *args):
    """
    Sorts an array of numbers in ascending order using the Bogo Sort algorithm.

    Bogo Sort sorts an array by randomly shuffling it and checking if the elements 
    are in sorted order. It repeatedly shuffles the array until it is sorted.

    Parameters:
        array (list): The array to be sorted.
        *args: Additional arguments, not used in this function.

    Yields:
        Tuple (list, int, int, int, int): A tuple containing:
        - The current state of the array being sorted.
        - The index of the first number being compared.
        - The index of the second number being compared.
        - The index of the number that is currently being sorted.
        - The index of the number that is currently being compared with.

    """
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
            is_sorted = True
