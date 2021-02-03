import display
import pygame
from algs import algorithmsDict, runAlgorithm, algorithmsVarDict
from random import randint

# Global Variables: numBars, delay, toDraw, button
# They were declared in display.py


def main():
    
    numbers = []
    running = True
    # Add default values
    display.sizeBox.text = '100'
    display.algorithmBox.add_options(list(algorithmsVarDict.keys()))
    display.variantBox.add_options(["variant"])
    # display.algorithmBox.text = 'mergesort'
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            display.variantBox.add_options(algorithmsVarDict[display.algorithmBox.get_active_option()])
            
            display.sizeBox.update(event)
            display.delayBox.update()
            display.algorithmBox.update()
            display.variantBox.update()
            display.startButton.update()
            a_list = list(range(0, display.numBars))

            if display.startButton.active:
                # Set the values given by the user
                display.numBars = int(display.sizeBox.text)
                display.delay =\
                    display.delayBox.value - display.delayBox.rect.x - 6
                algorithm = display.variantBox.get_active_option()
                # Generates a random list
                numbers = randomList()
                # Executes the chosen algorithm
                runAlgorithm(algorithm.lower(), numbers)
                display.toDraw = True
        display.drawInterface(numbers, -1, -1, -1, -1, greenRows = a_list)
    #When no longer running quit (on windows would just freeze up otherwise)
    pygame.quit()


def randomList():
    """Generate a random sequence of <numBars> numbers"""
    array = []
    for i in range(display.numBars):
        array.append(randint(10, 400))
    return array

if __name__ == '__main__':
    main()
