import pygame
from random import randint
from time import time
from algs import algorithmsDict
import variables
import display

# declared in variables.py : numBars, delay, do_sorting, paused, timer_space_bar
# declared in display.py : sizeBox, delayBox, algorithmBox, startButton


def main():
    numbers = []
    running = True
    display.algorithmBox.add_options(list(algorithmsDict.keys()))

    current_alg = None
    alg_iterator = None

    timer_delay = time()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and variables.do_sorting:
                variables.paused = not variables.paused
                variables.timer_space_bar = time()

            display.sizeBox.update(event)
            display.delayBox.update(event)
            display.algorithmBox.update()
            display.startButton.update()

        variables.delay = (display.delayBox.value-display.delayBox.rect.x-6)/1000 # delay is in ms
        display.startButton.is_playing = variables.do_sorting

        if display.startButton.isActive: # play-stop button clicked
            display.startButton.isActive = False
            if variables.do_sorting: # deplete generator to display sorted numbers
                variables.do_sorting = False
                variables.paused = False
                try:
                    while True:
                        numbers, redBar1, redBar2, blueBar1, blueBar2 = next(alg_iterator)
                except StopIteration:
                    pass
            else: # initiate generator
                variables.do_sorting = True
                current_alg = display.algorithmBox.get_active_option()
                variables.numBars = int(display.sizeBox.text)
                numbers = [randint(10, 400) for i in range(variables.numBars)] # random list to be sorted
                alg_iterator = algorithmsDict[current_alg](numbers, 0, variables.numBars-1) # initialize iterator

        if variables.do_sorting and not variables.paused:
            try:
                if time()-timer_delay >= variables.delay:
                    numbers, redBar1, redBar2, blueBar1, blueBar2 = next(alg_iterator)
                    display.drawInterface(numbers, redBar1, redBar2, blueBar1, blueBar2)
                    timer_delay = time()
            except StopIteration:
                variables.do_sorting = False
        elif variables.do_sorting and variables.paused:
            display.drawInterface(numbers, -1, -1, -1, -1)
        else:
            a_set = set(range(variables.numBars))
            display.drawInterface(numbers, -1, -1, -1, -1, greenRows=a_set)

if __name__ == '__main__':
    main()
