from display import handleDrawing


def get_gap(prev_gap) -> int:
    gap = int(prev_gap/1.3)
    if gap < 1:
        return 1
    return gap
    

def combSort(array, *args):
    size = len(array)
    gap = size
    swapped = True

    while gap != 1 or swapped:
        gap = get_gap(gap)
        swapped = False

        for idx in range(0, size - gap):
            handleDrawing(array, idx, idx+gap, -1, -1)
            if array[idx] > array[idx + gap]:
                array[idx], array[idx + gap] = array[idx + gap], array[idx]
                swapped = True
