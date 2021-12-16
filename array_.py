import pygame
import display

from random import randint, shuffle


# Declared in display.py
# 1. global variables : numBars, delay, do_sorting, paused, timer_space_bar
# 2. widgets : sizeBox, delayBox, shuffleBox, algorithmBox, playButton, stopButton


def create_array(array):
    array[:] = (int(10 + 390*(i/display.numBars)) for i in range(display.numBars))
    
    if display.shuffleBox.get_active_option() == 'sorted' : pass
    if display.shuffleBox.get_active_option() == 'reverse': array.reverse()
    if display.shuffleBox.get_active_option() == 'random' : shuffle(array)