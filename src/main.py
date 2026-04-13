import os
import pygame
from display import Window, TextBox, SlideBox, DropdownBox, PlayStopButton
from algs import algorithmsDict
from random import randint
import time
import math

# Initialize pygame modules
pygame.init()

# Font
baseFont = pygame.font.Font("res/Ubuntu-Regular.ttf", 19)

# Colors
grey = (100, 100, 100)
white = (250, 250, 250)
red = (255, 50, 50)
black = (0, 0, 0)
blue = (50, 50, 255)

pygame.display.set_caption('Sorting Algorithms Visualizer')
screen = pygame.display.set_mode((900, 500))
window = Window(screen)

window.add_widget(
    widget_id = 'size_input',
    widget = TextBox((24, 447, 88, 36), 'Size', grey, baseFont, '100')
)
window.add_widget(
    widget_id='delay_slider',
    widget=SlideBox((124, 447, 128, 36), 'Delay', grey, baseFont)
)
window.add_widget(
    widget_id = 'algorithm_input',
    widget = DropdownBox((264, 447, 176, 36), 'Algorithm', grey, baseFont, list(algorithmsDict.keys()), white)
)
window.add_widget(
    widget_id = 'play_button',
    widget = PlayStopButton((452, 448, 34, 34), grey)
)

def drawBars(screen, array, redBars, blueBars):
    '''
    Draw the bars and control their colors.
    *redBars* and *blueBars* are tuples of bar indices to highlight.
    '''
    numBars = len(array)
    if numBars != 0:
        bar_width  = 900 / numBars
        ceil_width = math.ceil(bar_width)

    for num in range(numBars):
        if   num in redBars : color = red
        elif num in blueBars: color = blue
        else                 : color = grey
        pygame.draw.rect(screen, color, (num * bar_width, 400 - array[num], ceil_width, array[num]))

def main():
    numbers = []
    running = True
    isPlaying = False
    isSorting = False
    sortingIterator = None
    last_iteration = 0
    redBars, blueBars = (), ()

    while running:

        # Background
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            window.update(event)

        # Get delay in seconds
        delay = window.get_widget_value('delay_slider') / 10

        isPlaying = window.get_widget_value('play_button')

        if not isPlaying:
            isSorting = False

        if isPlaying and not isSorting:

            # Random list to be sorted
            numBars = int(window.get_widget_value('size_input'))
            numbers = [randint(10, 400) for i in range(numBars)]

            # Initialize sorting iterator
            sortingAlgorithm = window.get_widget_value('algorithm_input')
            sortingIterator = algorithmsDict[sortingAlgorithm](numbers, 0, numBars - 1)
            isSorting = True
            redBars, blueBars = (), ()
            last_iteration = 0

        if isPlaying and isSorting and time.time() - last_iteration >= delay:
            step = next(sortingIterator, None)
            if step is None:
                isSorting = False
                window.set_widget_value('play_button', False)
                redBars, blueBars = (), ()
            else:
                numbers, redBars, blueBars = step
                last_iteration = time.time()

        # Draw bars
        if len(numbers) > 0:
            drawBars(screen, numbers, redBars, blueBars)

        window.render()
        pygame.display.update()


if __name__ == '__main__':
    main()
