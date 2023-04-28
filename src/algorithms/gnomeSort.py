def gnomeSort(a, *args):
    """
    Sorts an array of integers using the Gnome Sort Algorithm.

    Gnome Sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements that are 
    in the wrong order until the entire list is sorted. It gets its name from the idea that it is similar to how a garden 
    gnome sorts his flower pots. 
    
    Args:
        a (list): A list of integers to be sorted.
    
    Yields:
        tuple: A tuple containing the current state of the list and the indices of the elements being compared in each 
        iteration. If no elements are being compared, -1 is returned for those values.
    """
    i, size = 0, len(a)
    while i < size:
        if a[i-1] <= a[i] or i == 0:
             yield a, i, i-1, -1, -1
             i += 1
        else:
            yield a, i, i-1, -1, -1
            a[i-1],a[i] = a[i],a[i-1]
            i -= 1
