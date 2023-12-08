import pygame
from random import randint
from time import time
from algs import algorithmsDict
import display as display

# Declared in globals.py
# 1. global variables : numBars, delay, do_sorting, paused, timer_space_bar
# Declared in display.py
# 2. widgets : sizeBox, delayBox, algorithmBox, playButton, stopButton

def main():
    # Initialize variables
    numbers = []
    running = True
    display.algorithmBox.add_options(list(algorithmsDict.keys()))

    current_alg = None
    alg_iterator = None

    timer_delay = time()
    
    # Main data visualizer loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Pause/unpause animation on spacebar press
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and display.do_sorting:
                display.paused = not display.paused
                display.timer_space_bar = time()

            display.updateWidgets(event)

        # Calculate delay for the animation
        display.delay = (display.delayBox.value-display.delayBox.rect.x-6)/1000 # delay is in ms

        # Play button clicked
        if display.playButton.isActive:
            display.playButton.isActive = False
            display.do_sorting = True
            display.start_time = time()
            current_alg = display.algorithmBox.get_active_option()
            display.numBars = int(display.sizeBox.text)
            numbers = [randint(10, 400) for i in range(display.numBars)] # random list to be sorted
            alg_iterator = algorithmsDict[current_alg](numbers, 0, display.numBars-1) # initialize iterator

        # Stop button clicked
        if display.stopButton.isActive:
            display.stopButton.isActive = False
            display.do_sorting = False
            display.paused = False
            try: # deplete generator to display sorted numbers
                while True:
                    numbers, redBar1, redBar2, blueBar1, blueBar2 = next(alg_iterator)
            except StopIteration:
                pass

        # Sorting animation
        if display.do_sorting and not display.paused:
            try:
                if time()-timer_delay >= display.delay:
                    numbers, redBar1, redBar2, blueBar1, blueBar2 = next(alg_iterator)
                    display.drawInterface(numbers, redBar1, redBar2, blueBar1, blueBar2)
                    timer_delay = time()
                    if not display.paused:
                        display.time_taken = time() - display.start_time
                        display.timeBox.update()
            except StopIteration:
                display.do_sorting = False
                display.time_taken = time() - display.start_time
                display.timeBox.update()
        # Animation paused
        elif display.do_sorting and display.paused:
            display.drawInterface(numbers, -1, -1, -1, -1)
        # No animation
        else:
            a_set = set(range(display.numBars))
            display.drawInterface(numbers, -1, -1, -1, -1, greenRows=a_set)

if __name__ == '__main__':
    main()
