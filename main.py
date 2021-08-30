import pygame
from random import randint
from time import time
from algs import algorithmsDict
import display

# Global Variables: numBars, delay, button, paused, timer_space_bar
# They were declared in display.py


def main():
    numbers = []
    running = True
    display.algorithmBox.add_options(list(algorithmsDict.keys()))

    current_alg = None
    alg_iterator = None
    do_sorting = False

    timer_delay = time()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and do_sorting:
                display.paused = not display.paused
                display.timer_space_bar = time()

            display.sizeBox.update(event)
            display.delayBox.update(event)
            display.algorithmBox.update()
            display.startButton.update()

        display.delay = (display.delayBox.value-display.delayBox.rect.x-6)/1000 # delay is in ms
        display.startButton.is_playing = do_sorting

        if display.startButton.isActive: # play-stop button clicked
            display.startButton.isActive = False
            if do_sorting: # deplete generator to display sorted numbers
                do_sorting = False
                display.paused = False
                try:
                    while True:
                        numbers, redBar1, redBar2, blueBar1, blueBar2 = next(alg_iterator)
                except StopIteration:
                    pass
            else: # initiate generator
                do_sorting = True
                current_alg = display.algorithmBox.get_active_option()
                display.numBars = int(display.sizeBox.text)
                numbers = [randint(10, 400) for i in range(display.numBars)] # random list to be sorted
                alg_iterator = algorithmsDict[current_alg](numbers, 0, display.numBars-1) # initialize iterator

        if do_sorting and not display.paused:
            try:
                if time()-timer_delay >= display.delay:
                    numbers, redBar1, redBar2, blueBar1, blueBar2 = next(alg_iterator)
                    display.drawInterface(numbers, redBar1, redBar2, blueBar1, blueBar2)
                    timer_delay = time()
            except StopIteration:
                do_sorting = False
        elif do_sorting and display.paused:
            display.drawInterface(numbers, -1, -1, -1, -1)
        else:
            a_set = set(range(display.numBars))
            display.drawInterface(numbers, -1, -1, -1, -1, greenRows=a_set)

if __name__ == '__main__':
    main()
