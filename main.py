import display
import pygame
from algs import *
from random import randint

# Global Variables: numBars, delay, toDraw, button
# They were declared in display.py


def main():
    numbers = []
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # In case the mouse is pressed
            if pygame.mouse.get_pressed() != (0, 0, 0):
                if display.delayBox.rect.collidepoint(mouse):
                    display.delayBox.write()
                elif display.sizeBox.rect.collidepoint(mouse):
                    display.sizeBox.isActive = True
                    display.algorithmBox.isActive = False
                elif display.algorithmBox.rect.collidepoint(mouse):
                    display.sizeBox.isActive = False
                    display.algorithmBox.isActive = True
                # In case the start button is pressed
                elif display.button_rect.collidepoint(mouse):
                    # Set the values given by the user
                    display.button = display.stopButton
                    display.numBars = int(display.sizeBox.text)
                    display.delay = display.delayBox.value - display.delayBox.rect.x - 6
                    algorithm = display.algorithmBox.text
                    # Generates a random list
                    numbers = randomList()
                    # Executes the chosen algorithm
                    runAlgorithm(algorithm.lower(), numbers)
                    display.button = display.playButton
                    display.toDraw = True
            # In case any key is pressed
            if event.type == pygame.KEYDOWN:
                if display.sizeBox.isActive:
                    display.sizeBox.write(event)
                elif display.algorithmBox.isActive:
                    display.algorithmBox.write(event)
        display.drawInterface(numbers, -1, -1, -1, -1)


def randomList():
    """Generate a random sequence of <numBars> numbers"""
    array = []
    for i in range(display.numBars):
        array.append(randint(10, 400))
    return array


if __name__ == '__main__':
    main()