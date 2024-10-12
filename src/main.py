import pygame
from display import Window, TextBox, SlideBox, DropdownBox, ButtonBox
from algs import algorithmsDict
from random import randint
import time
import math

# Initialize pygame modules
pygame.init()

# Font
baseFont = pygame.font.SysFont('Arial', 24)

# Colors
grey = (100, 100, 100)
green = (125, 240, 125)
white = (250, 250, 250)
red = (255, 50, 50)
black = (0, 0, 0)
blue = (50, 50, 255)

pygame.display.set_caption('Sorting Algorithms Visualizer')
screen = pygame.display.set_mode((900, 500))
window = Window(screen)

window.add_widget(
    widget_id = 'size_input',
    widget = TextBox((30, 440, 100, 50), 'Size', grey, baseFont, '100')
)
window.add_widget(
    widget_id='delay_slider',
    widget=SlideBox((140, 440, 150, 50), 'Delay', grey, baseFont)
)
window.add_widget(
    widget_id = 'algorithm_input',
    widget = DropdownBox((300, 440, 200, 50), 'Algorithm', grey, baseFont, list(algorithmsDict.keys()), white)
)
window.add_widget(
    widget_id = 'play_button',
    widget = ButtonBox((510, 445, 40, 40), 'res/playButton.png', 'res/stopButton.png')
)

def drawBars(screen, array, redBar1, redBar2, blueBar1, blueBar2, greenRows = {}):
    '''Draw the bars and control their colors'''
    numBars = len(array)
    if numBars != 0:
        bar_width  = 900 / numBars
        ceil_width = math.ceil(bar_width)

    for num in range(numBars):
        if   num in (redBar1, redBar2)  : color = red
        elif num in (blueBar1, blueBar2): color = blue
        elif num in greenRows           : color = green        
        else                            : color = grey
        pygame.draw.rect(screen, color, (num * bar_width, 400 - array[num], ceil_width, array[num]))

def main():
    numbers = []
    running = True
    isPlaying = False
    isSorting = False
    sortingIterator = None
    last_iteration = 0

    while running:
        screen.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            window.update(event)

        # Get delay in seconds
        delay = window.get_widget_value('delay_slider') / 10

        isPlaying = window.get_widget_value('play_button')
        if isPlaying and not isSorting:
            # Random list to be sorted
            numBars = int(window.get_widget_value('size_input'))
            numbers = [randint(10, 400) for i in range(numBars)]

            # Initialize sorting iterator
            sortingAlgorithm = window.get_widget_value('algorithm_input')
            sortingIterator = algorithmsDict[sortingAlgorithm](numbers, 0, numBars - 1)
            isSorting = True

        if not isPlaying:
            isSorting = False

        if isSorting:
                try:
                    # Get the next state from the sorting iterator
                    if time.time() - last_iteration >= delay:  
                        numbers, redBar1, redBar2, blueBar1, blueBar2 = next(sortingIterator)
                        last_iteration = time.time()
                    
                    drawBars(screen, numbers, redBar1, redBar2, blueBar1, blueBar2)
                    window.render()
                    pygame.display.update()
                        
                except StopIteration:
                    isSorting = False
                    window.set_widget_value('play_button', False)
        else:
            drawBars(screen, numbers, -1, -1, -1, -1, greenRows=set(range(len(numbers))))

        window.render()
        pygame.display.update()


if __name__ == '__main__':
    main()
