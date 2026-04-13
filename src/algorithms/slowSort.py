def slowSort(array, *args):
    """
    Slowsort (“multiply and surrender”).

    Recursively forces the maximum toward the end with a deliberately wasteful structure;
    intended as a humorous inverse of divide-and-conquer.

    Time complexity: extremely large by design—far worse than any practical O(n²) sort (n is the length).
    """

    def recursiveSlowSort(array, start, end):
        if start >= end:
            return

        middle_idx = (start + end) // 2

        yield from recursiveSlowSort(array, start, middle_idx)

        yield from recursiveSlowSort(array, middle_idx + 1, end)

        if array[end] < array[middle_idx]:
            array[end], array[middle_idx] = array[middle_idx], array[end]
            yield array, (start, middle_idx), (end,)

        yield from recursiveSlowSort(array, start, end - 1)

    yield from recursiveSlowSort(array, 0, len(array) - 1)
