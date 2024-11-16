def slowSort(array, *args):
    """
    The slow sort is an example of Multiply And Surrender a tongue-in-cheek joke of divide and conquer.
    Slow sort stores the maximum element of the array at the last position by recursively divides the array by half and compares each of them. 
    Then it recursively calls the array without the previous maximum element and stores the new maximum element at the new last position.
    The best case is worse than the bubble sort

    Time complexity: O(N ^ ( (log N) / (2+e) ) ) where e is a small positive number

    """

    def recursiveSlowSort(array, start, end):
        if start >= end:
            return

        middle_idx = (start + end) // 2

        yield from recursiveSlowSort(array, start, middle_idx)

        yield from recursiveSlowSort(array, middle_idx + 1, end)

        if array[end] < array[middle_idx]:
            array[end], array[middle_idx] = array[middle_idx], array[end]
            yield array, start, middle_idx, end, -1

        yield from recursiveSlowSort(array, start, end - 1)

    yield from recursiveSlowSort(array, 0, len(array) - 1)
