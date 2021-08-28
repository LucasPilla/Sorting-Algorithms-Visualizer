import pygame
import os
from math import ceil
from algs import algorithmsDict
from gui import Label, TextButton, IconButton, Slider, DigitInputBox
from gui import RowContainer, ColContainer, ScrollContainer
from gui import Theme

# Global Variables
numBars = 100
delay   = 0
do_sorting = False
current_theme = 'light'
current_alg = 'bubble'

# Initialize pygame modules
pygame.init()

# Display settings
windowSize = (900, 500)
canvasSize = (700, 400)
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Sorting Algorithms Visualizer')

# Font
baseFont = pygame.font.SysFont('Arial', 16)

# Used Colors
colors = {}
colors['grey_dark'] = pygame.Color(100, 100, 100)
colors['grey_light'] = pygame.Color(200, 200, 200)
colors['green'] = pygame.Color(125, 240, 125)
colors['white'] = pygame.Color(250, 250, 250)
colors['red'] = pygame.Color(255, 50, 50)
colors['black'] = pygame.Color(0, 0, 0)
colors['blue'] = pygame.Color(50, 50, 255)

# Themes
themes = {}
themes['light'] = Theme(baseFont, colors['grey_dark'], colors['black'])
themes['light'].fill_background(colors['white'])
themes['dark'] = Theme(baseFont, colors['grey_light'], colors['red'])
themes['dark'].fill_background(colors['grey_dark'])

# Size container
size_container = RowContainer(padding=(0, 0), spacing=0)
size_name_label = Label((80, 60), "Size")
size_container.add_item(size_name_label)
size_box = DigitInputBox((80, 60), default_value=numBars)
size_container.add_item(size_box)

# Delay container
delay_container = RowContainer(padding=(0, 0), spacing=0)
delay_name_label = Label((80, 60), "Delay")
delay_container.add_item(delay_name_label)
delay_slider = Slider((100, 60))
delay_container.add_item(delay_slider)
delay_label = Label((60, 60), str(delay))
delay_container.add_item(delay_label)

# Run container
play_button = IconButton((60, 60), pygame.image.load(os.path.join('images', 'playButton.png')))
stop_button = IconButton((60, 60), pygame.image.load(os.path.join('images', 'stopButton.png')))
run_container = RowContainer()
run_container.add_item(play_button)
run_container.add_item(stop_button)

# Algorithms container
alg_container = ColContainer(padding=(0, 0), spacing=0)
alg_name_label = Label((100, 60), "Algorithms")
alg_container.add_item(alg_name_label)
alg_buttons = {}
for alg_name in algorithmsDict.keys():
    alg_buttons[alg_name] = TextButton((100, 60), alg_name)
    alg_container.add_item(alg_buttons[alg_name])
alg_label = Label((100, 60), current_alg)
alg_container.add_item(alg_label)

# Themes container
theme_container = RowContainer(padding=(0, 0), spacing=0)
theme_name_label = Label((80, 60), "Theme")
theme_container.add_item(theme_name_label)
theme_buttons = {}
for theme_name in themes.keys():
    theme_buttons[theme_name] = TextButton((80, 60), theme_name)
    theme_container.add_item(theme_buttons[theme_name])

# Side panel
side_container = ColContainer(padding=(20, 20), spacing=20)
side_container.add_item(alg_container)
side_panel = ScrollContainer((windowSize[0]-canvasSize[0], windowSize[1]), side_container)

# Bottom panel
bottom_container = RowContainer(padding=(20, 20), spacing=20)
bottom_container.add_item(size_container)
bottom_container.add_item(delay_container)
bottom_container.add_item(run_container)
bottom_container.add_item(theme_container)
bottom_panel = ScrollContainer((canvasSize[0], windowSize[1]-canvasSize[1]), bottom_container)
bottom_panel.move_to(windowSize[0]-canvasSize[0], canvasSize[1])

# Called in main.py when an event is detected
def handle_mouse_pressed(mouse_pos):
    side_panel.mouse_pressed(mouse_pos)
    bottom_panel.mouse_pressed(mouse_pos)

def handle_mouse_dragged(mouse_pos):
    side_panel.mouse_dragged(mouse_pos)
    bottom_panel.mouse_dragged(mouse_pos)

def handle_mouse_released(mouse_pos):
    side_panel.mouse_released(mouse_pos)
    bottom_panel.mouse_released(mouse_pos)

def handle_key_pressed(key):
    side_panel.key_pressed(key)
    bottom_panel.key_pressed(key)

# Drawing on canvas
def drawBars(array, redBar1, redBar2, blueBar1, blueBar2, greenRows = {}, **kwargs):
    '''Draw the bars and control their colors'''
    if numBars != 0:
        bar_width  = canvasSize[0] / numBars
        ceil_width = ceil(bar_width)

    for num in range(numBars):
        if   num in (redBar1, redBar2)  : color = colors['red']
        elif num in (blueBar1, blueBar2): color = colors['blue']
        elif num in greenRows           : color = colors['green']        
        else                            : color = colors['grey_dark']
        pygame.draw.rect(screen, color, (num*bar_width+(windowSize[0]-canvasSize[0]), canvasSize[1]-array[num], ceil_width, array[num]))

# Called in main.py when updating the interface
def drawInterface(array, redBar1, redBar2, blueBar1, blueBar2, **kwargs):
    '''Draw all the interface'''
    screen.fill(colors['white'])
    drawBars(array, redBar1, redBar2, blueBar1, blueBar2, **kwargs)
    side_panel.draw(screen, themes[current_theme])
    bottom_panel.draw(screen, themes[current_theme])
    pygame.display.update()
