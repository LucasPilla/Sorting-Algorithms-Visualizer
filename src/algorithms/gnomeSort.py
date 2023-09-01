def gnomeSort(a, *args):
    """
    Gnome Sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements that are 
    in the wrong order until the entire list is sorted. It gets its name from the idea that it is similar to how a garden 
    gnome sorts his flower pots.

    Time complexity: O(n ^ 2), where n is the number of elements in the list 
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
