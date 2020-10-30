import display
import pygame
from algs import *
from random import randint

# Global Variables: numBars, delay, toDraw, button
# They were declared in display.py


def main():
    numbers = []
    running = True
    # Add default values
    display.sizeBox.text = '100'
    display.algorithmBox.text = 'mergesort'
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            display.sizeBox.update(event)
            display.delayBox.update()
            display.algorithmBox.update(event)
            display.startButton.update()

            if display.startButton.active and not error_checking():
                # Set the values given by the user
                display.numBars = int(display.sizeBox.text)
                display.delay = display.delayBox.value - display.delayBox.rect.x - 6
                algorithm = display.algorithmBox.text
                # Generates a random list
                numbers = randomList()
                # Executes the chosen algorithm
                runAlgorithm(algorithm.lower(), numbers)
                display.toDraw = True
        display.drawInterface(numbers, -1, -1, -1, -1)


def randomList():
    """Generate a random sequence of <numBars> numbers"""
    array = []
    for i in range(display.numBars):
        array.append(randint(10, 400))
    return array


def error_checking():
    size = display.sizeBox.text
    algorithm = display.algorithmBox.text
    error = False
    if not size.isdigit():
        display.sizeBox.color = display.red
        error = True
    if algorithm not in list(algorithmsDict):
        display.algorithmBox.color = display.red
        error = True
    if error: return True
    display.sizeBox.color = display.grey
    display.algorithmBox.color = display.grey
    return False


if __name__ == '__main__':
    main()
