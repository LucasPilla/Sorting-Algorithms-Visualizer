import pygame
from random import randint
from time import time
from algs import algorithmsDict
import display

# Global Variables: numBars, delay, toDraw, button
# They were declared in display.py


def main():
    numbers = [randint(10, 400) for i in range(display.numBars)]
    running = True
    display.algorithmBox.add_options(list(algorithmsDict.keys()))

    current_alg = None
    alg_iterator = None
    do_sorting = False
    
    timer = time()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            display.sizeBox.update(event)
            display.delayBox.update(event)
            display.algorithmBox.update()
            display.startButton.update()

            display.numBars = int(display.sizeBox.text)
            display.delay = (display.delayBox.value-display.delayBox.rect.x-6)/1000

        if display.startButton.isActive:
            display.startButton.isActive = False
            display.startButton.is_playing = not display.startButton.is_playing
            if do_sorting:
                do_sorting = False
            else:
                do_sorting = True
                current_alg = display.algorithmBox.get_active_option()
                numbers = [randint(10, 400) for i in range(display.numBars)] # random list to be sorted
                alg_iterator = algorithmsDict[current_alg](numbers, 0, display.numBars-1) # initialize iterator

        if do_sorting:
            try:
                if time()-timer >= display.delay:
                    numbers, redBar1, redBar2, blueBar1, blueBar2 = next(alg_iterator)
                    display.drawInterface(numbers, redBar1, redBar2, blueBar1, blueBar2)
                    timer = time()
            except StopIteration:
                do_sorting = False
        else:
            a_set = set(range(display.numBars))
            display.drawInterface(numbers, -1, -1, -1, -1, greenRows=a_set)

if __name__ == '__main__':
    main()
