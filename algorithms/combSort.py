#!/usr/bin/python3
# coding: utf-8
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

    gap = int((prev_gap * a_length)/13)

    if gap < 1:
        return 1
    return gap
    

def combSort(_list=None) -> list:
    """
    Sort a list using \'Comb Sort\'
    :param _list: list with real numbers
    :return: sorted list
    """
    if _list is None:
        raise ValueError("a list of numbers is needed")
    if isinstance(_list, list) is False:
        raise TypeError("a \'_list\' must be \'list\' type")
    if len(_list) is False:
        raise ValueError("list is empty")
    
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
