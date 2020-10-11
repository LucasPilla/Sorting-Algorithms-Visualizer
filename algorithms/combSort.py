#!/usr/bin/python3
# code: utf-8
from display import handleDrawing


def get_gap(prev_gap=None, a_length=None) -> int:
    """
    Gets the next gap

    :param prev_gap: previous gap
    :param a_length: length of currently sorting array
    :return: new gap 
    """
    if prev_gap is None:
        raise ValueError("previous \'gap\' is needed")
    if isinstance(prev_gap, int) is False:
        raise TypeError("\'gap\' must be \'int\' type")
    if a_length is None:
        raise ValueError("array length is needed")
    if isinstance(a_length, int) is False:
        raise TypeError("\'a_length\' must be \'int\' type")

    gap = int((prev_gap * a_length)/1.3)

    if gap < 1:
        return 1
    return gap
    

a = get_gap(10, 10)
print(a)