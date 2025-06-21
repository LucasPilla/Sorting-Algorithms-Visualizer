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

# Theme system
class Theme:
    def __init__(self):
        self.is_dark_mode = False
        self.light_theme = {
            'background': (250, 250, 250),
            'widget_border': (100, 100, 100),
            'widget_background': (250, 250, 250),
            'text': (0, 0, 0),
            'bar_default': (100, 100, 100),
            'bar_comparing': (255, 50, 50),
            'bar_pivot': (50, 50, 255),
            'bar_sorted': (125, 240, 125)
        }
        self.dark_theme = {
            'background': (30, 30, 30),
            'widget_border': (150, 150, 150),
            'widget_background': (50, 50, 50),
            'text': (255, 255, 255),
            'bar_default': (120, 120, 120),
            'bar_comparing': (255, 100, 100),
            'bar_pivot': (100, 100, 255),
            'bar_sorted': (100, 200, 100)
        }
    
    def get_color(self, color_name):
        theme = self.dark_theme if self.is_dark_mode else self.light_theme
        return theme.get(color_name, (255, 255, 255))
    
    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode

# Global theme instance
theme = Theme()

# Legacy color variables for compatibility (will be updated dynamically)
grey = theme.get_color('widget_border')
green = theme.get_color('bar_sorted')
white = theme.get_color('background')
red = theme.get_color('bar_comparing')
black = theme.get_color('text')
blue = theme.get_color('bar_pivot')

pygame.display.set_caption('Sorting Algorithms Visualizer')
screen = pygame.display.set_mode((900, 500))
window = Window(screen)

def update_colors():
    """Update color variables based on current theme"""
    global grey, green, white, red, black, blue
    grey = theme.get_color('widget_border')
    green = theme.get_color('bar_sorted')
    white = theme.get_color('background')
    red = theme.get_color('bar_comparing')
    black = theme.get_color('text')
    blue = theme.get_color('bar_pivot')

def create_widgets():
    """Create or recreate widgets with current theme colors"""
    window.clear_widgets()
    
    window.add_widget(
        widget_id = 'size_input',
        widget = TextBox((30, 440, 100, 50), 'Size', theme.get_color('widget_border'), baseFont, '100', theme)
    )
    window.add_widget(
        widget_id='delay_slider',
        widget=SlideBox((140, 440, 150, 50), 'Delay', theme.get_color('widget_border'), baseFont, theme)
    )
    window.add_widget(
        widget_id = 'algorithm_input',
        widget = DropdownBox((300, 440, 200, 50), 'Algorithm', theme.get_color('widget_border'), baseFont, list(algorithmsDict.keys()), theme.get_color('widget_background'), theme)
    )
    window.add_widget(
        widget_id = 'play_button',
        widget = ButtonBox((510, 445, 40, 40), 'res/playButton.png', 'res/stopButton.png', theme)    )
    dark_mode_text = 'Dark Mode: ON' if theme.is_dark_mode else 'Dark Mode: OFF'
    window.add_widget(
        widget_id = 'theme_toggle',
        widget = ButtonBox((560, 445, 120, 40), None, None, theme, text=dark_mode_text)
    )

# Initialize widgets
create_widgets()

def drawBars(screen, array, redBar1, redBar2, blueBar1, blueBar2, greenRows = {}):
    '''Draw the bars and control their colors'''
    numBars = len(array)
    if numBars != 0:
        bar_width  = 900 / numBars
        ceil_width = math.ceil(bar_width)

    for num in range(numBars):
        if   num in (redBar1, redBar2)  : color = theme.get_color('bar_comparing')
        elif num in (blueBar1, blueBar2): color = theme.get_color('bar_pivot')
        elif num in greenRows           : color = theme.get_color('bar_sorted')        
        else                            : color = theme.get_color('bar_default')
        pygame.draw.rect(screen, color, (num * bar_width, 400 - array[num], ceil_width, array[num]))

def main():
    numbers = []
    running = True
    isPlaying = False
    isSorting = False
    sortingIterator = None
    last_iteration = 0

    while running:
        screen.fill(theme.get_color('background'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            window.update(event)        # Check for theme toggle
        if window.get_widget_value('theme_toggle'):
            theme.toggle_theme()
            update_colors()
            create_widgets()
            window.set_widget_value('theme_toggle', False)  # Reset toggle button

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
