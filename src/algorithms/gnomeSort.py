def gnomeSort(a, *args):
    """
    Gnome sort.

    Walks forward while order holds; on a violation swaps backward like insertion sort
    but one step at a time.

    Time complexity: O(n²) average and worst case; O(n) best case when the input is sorted.
    """
    i, size = 0, len(a)
    while i < size:
        if a[i-1] <= a[i] or i == 0:
             yield a, (i, i - 1), ()
             i += 1
        else:
            yield a, (i, i - 1), ()
            a[i-1],a[i] = a[i],a[i-1]
            i -= 1
