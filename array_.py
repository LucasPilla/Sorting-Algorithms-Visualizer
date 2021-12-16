import pygame
import display

from random import randint, shuffle


# Declared in display.py
# 1. global variables : numBars, delay, do_sorting, paused, timer_space_bar
# 2. widgets : sizeBox, delayBox, shuffleBox, algorithmBox, playButton, stopButton


def sorted_(array):
    pass

def reverse(array):
    array.reverse()
    
def random(array):
    shuffle(array)


shufflesDict = {'random' : random,
                'sorted' : sorted_,
                'reverse': reverse}


def create_array(array):
    array[:] = (int(10 + 390*(i/display.numBars)) for i in range(display.numBars))
    shufflesDict[display.shuffleBox.get_active_option()](array)
    
