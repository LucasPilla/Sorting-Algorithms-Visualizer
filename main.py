import display
import pygame
from algs   import algorithmsDict, runAlgorithm
from random import randint, sample


# Global variables 'numBars', 'delay', 'toDraw', and 'button' were declared in display.py

def main():
    numbers = []
    display.algorithmBox.add_options(list(algorithmsDict.keys()))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return pygame.quit()

            display.sizeBox.update(event)
            display.delayBox.update()
            display.algorithmBox.update()
            display.startButton.update()

            if display.startButton.active:
                display.numBars = int(display.sizeBox.text)          # Set the values given by the user
                display.delay   = display.delayBox.value - display.delayBox.rect.x - 6
                algorithm = display.algorithmBox.get_active_option()
                numbers   = sample(range(10, 400), display.numBars)  # Generates a random list
                runAlgorithm(algorithm.lower(), numbers)             # Executes the chosen algorithm
                display.toDraw = True
                
        display.drawInterface(numbers, -1, -1, -1, -1, greenRows=set(range(display.numBars)))

if __name__ == '__main__':
    main()
