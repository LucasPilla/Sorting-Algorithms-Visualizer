from display import handleDrawing


def get_gap(prev_gap=None, a_length=None) -> int:
    gap = int((prev_gap * a_length)/13)
    if gap < 1:
        return 1
    return gap
    

def combSort(_list=None):
    a_length = len(_list)
    gap = a_length
    swapped = True

    while gap != 1 or swapped:
        gap = get_gap(prev_gap=gap, a_length=len(_list))
        swapped = False

        for idx in range(0, a_length - gap):
            if _list[idx] > _list[idx + gap]:
                _list[idx], _list[idx + gap] = _list[idx + gap], _list[idx]
                swapped = True
