import display
import pygame
from algs import algorithmsDict, runAlgorithm, timeComplexityOpt, returnAlgoList
from random import randint


# Global Variables: numBars, delay, toDraw, button
# They were declared in display.py


def main():
    numbers = []
    running = True
    display.algorithmBox.add_options(returnAlgoList("All"))
    prev = "All"
    display.timeComplexityBox.add_options(list(timeComplexityOpt))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            display.sizeBox.update(event)
            display.delayBox.update()
            display.algorithmBox.update()
            display.startButton.update()
            display.timeComplexityBox.update()
            a_set = set(range(display.numBars))
            current_tc = display.timeComplexityBox.get_active_option()      # get current time complexity
            if current_tc != prev:                                          # if changed, update algo list
                prev = current_tc
                display.algorithmBox.add_options(returnAlgoList(current_tc))

            if display.startButton.active:
                # Set the values given by the user
                display.numBars = int(display.sizeBox.text)
                display.delay = \
                    display.delayBox.value - display.delayBox.rect.x - 6

                algorithm = display.algorithmBox.get_active_option()
                # Generates a random list
                numbers = [randint(10, 400) for i in range(display.numBars)]
                # Executes the chosen algorithm
                runAlgorithm(algorithm.lower(), numbers)
                display.toDraw = True
        display.drawInterface(numbers, -1, -1, -1, -1, greenRows=a_set)


if __name__ == '__main__':
    main()
