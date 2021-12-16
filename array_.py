import pygame
import display

from random    import randint, shuffle
from itertools import chain

# Declared in display.py
# 1. global variables : numBars, delay, do_sorting, paused, timer_space_bar
# 2. widgets : sizeBox, delayBox, shuffleBox, algorithmBox, playButton, stopButton

    
def make_asc_saw(array):
    n_saw = 8
    value = 0
    temp  = tuple([] for i in range(n_saw))
    
    for i in array:
        temp[value].append(i)
        value = (value + 1) % n_saw
        
    array[:] = chain.from_iterable(temp)

def make_dsc_saw(array):
    reverse(array)
    make_asc_saw(array)
    
def sorted_(array):
    pass

def reverse(array):
    array.reverse()
    
def random(array):
    shuffle(array)



shufflesDict = {'random'     : random,
                'sorted'     : sorted_,
                'reverse'    : reverse,
                'saw (asc.)' : make_asc_saw,
                'saw (desc.)': make_dsc_saw}


def create_array(array):
    array[:] = (int(10 + 390*(i/display.numBars)) for i in range(display.numBars))
    shufflesDict[display.shuffleBox.get_active_option()](array)
    
