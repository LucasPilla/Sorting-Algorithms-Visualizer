# main.py

import pygame
from display import Window, TextBox, SlideBox, DropdownBox, ButtonBox
from algs import algorithmsDict
from random import randint
import time
import math

# Initialize Pygame and set up a font
pygame.init()
baseFont = pygame.font.SysFont('Arial', 24)

# Light-mode colors
LIGHT_GREY   = (100, 100, 100)
LIGHT_GREEN  = (125, 240, 125)
LIGHT_WHITE  = (250, 250, 250)
LIGHT_RED    = (255, 50, 50)
LIGHT_BLACK  = (0, 0, 0)
LIGHT_BLUE   = (50, 50, 255)

# Dark-mode colors
DARK_GREY    = (50, 50, 50)
DARK_GREEN   = (80, 180, 80)
DARK_WHITE   = (30, 30, 30)    # Nearly black, used as background
DARK_RED     = (200, 30, 30)
DARK_BLACK   = (230, 230, 230) # Light gray for text/borders
DARK_BLUE    = (30, 30, 200)

# Flag to keep track of current theme: False = Light, True = Dark
dark_mode = False

# Window size constants
WINDOW_WIDTH  = 900
WINDOW_HEIGHT = 500

pygame.display.set_caption('Sorting Algorithms Visualizer')
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window = Window(screen)


# Add the UI widgets (size input box, delay slider, algorithm dropdown, play/stop button)
window.add_widget(
    widget_id = 'size_input',
    widget = TextBox((30, 440, 100, 50), 'Size', LIGHT_GREY, baseFont, '100')
)
window.add_widget(
    widget_id = 'delay_slider',
    widget = SlideBox((140, 440, 150, 50), 'Delay', LIGHT_GREY, baseFont)
)
window.add_widget(
    widget_id = 'algorithm_input',
    widget = DropdownBox(
        (300, 440, 200, 50),
        'Algorithm',
        LIGHT_GREY,
        baseFont,
        list(algorithmsDict.keys()),
        LIGHT_WHITE
    )
)
window.add_widget(
    widget_id = 'play_button',
    widget = ButtonBox((510, 445, 40, 40), 'res/playButton.png', 'res/stopButton.png')
)

# drawBars: draws the sorting bars on screen, using whichever
# color-palette is currently active
def drawBars(screen, array, redBar1, redBar2, blueBar1, blueBar2, greenRows = {}):
    numBars = len(array)
    if numBars != 0:
        bar_width  = WINDOW_WIDTH / numBars
        ceil_width = math.ceil(bar_width)
    else:
        return  # nothing to draw if array is empty

    # Choose the right set of colors based on dark_mode
    if dark_mode:
        grey_color  = DARK_GREY
        green_color = DARK_GREEN
        red_color   = DARK_RED
        blue_color  = DARK_BLUE
    else:
        grey_color  = LIGHT_GREY
        green_color = LIGHT_GREEN
        red_color   = LIGHT_RED
        blue_color  = LIGHT_BLUE

    # Loop over each bar index and draw it with the correct color
    for idx in range(numBars):
        if   idx in (redBar1, redBar2):
            color = red_color
        elif idx in (blueBar1, blueBar2):
            color = blue_color
        elif idx in greenRows:
            color = green_color
        else:
            color = grey_color

        pygame.draw.rect(
            screen,
            color,
            (
                idx * bar_width,
                400 - array[idx],
                ceil_width,
                array[idx]
            )
        )

# main loop: handles events, toggling dark_mode, starting/stopping sorting,
# drawing the bars, and rendering widgets each frame.
def main():
    global dark_mode  # so we can flip it on mouse clicks

    numbers = []
    running = True
    isPlaying = False
    isSorting = False
    sortingIterator = None
    last_iteration = 0

    # A small clickable rectangle in the top-right to toggle Light/Dark
    toggle_rect = pygame.Rect(WINDOW_WIDTH - 170, 10, 150, 30)

    while running:
        # Fill background each frame using the correct mode
        if dark_mode:
            screen.fill(DARK_WHITE)
        else:
            screen.fill(LIGHT_WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # If user left-clicks in our toggle_rect, flip dark_mode
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if toggle_rect.collidepoint(event.pos):
                    dark_mode = not dark_mode
                    # (Optional) If you want the widget colors to switch, you'd do it here.

            # Let the Window/UI system handle the event (text input, button press, etc.)
            window.update(event)

        # Get the delay value (slider output is 0.0 to 1.0) and divide by 10
        delay = window.get_widget_value('delay_slider') / 10
        isPlaying = window.get_widget_value('play_button')

        # If “Play” is pressed and we aren’t already sorting, start a new random array
        if isPlaying and not isSorting:
            numBars = int(window.get_widget_value('size_input'))
            numbers = [randint(10, 400) for _ in range(numBars)]
            sortingAlgorithm = window.get_widget_value('algorithm_input')
            sortingIterator = algorithmsDict[sortingAlgorithm](numbers, 0, numBars - 1)
            isSorting = True

        # If Play is off, make sure isSorting is False
        if not isPlaying:
            isSorting = False

        if isSorting:
            try:
                # Advance the sorting iterator once per 'delay' seconds
                if time.time() - last_iteration >= delay:
                    numbers, redBar1, redBar2, blueBar1, blueBar2 = next(sortingIterator)
                    last_iteration = time.time()

                drawBars(screen, numbers, redBar1, redBar2, blueBar1, blueBar2)
                window.render()
                pygame.display.update()

            except StopIteration:
                # Sorting is done
                isSorting = False
                window.set_widget_value('play_button', False)

        else:
            # If we're not actively sorting, draw bars as fully sorted (all green)
            drawBars(screen, numbers, -1, -1, -1, -1, greenRows=set(range(len(numbers))))

        # Draw the Dark/Light Mode toggle box and its label each frame
        if dark_mode:
            rect_fill   = DARK_GREY
            rect_border = DARK_BLACK
            text_color  = DARK_BLACK
            label       = "Light Mode"
        else:
            rect_fill   = LIGHT_GREY
            rect_border = LIGHT_BLACK
            text_color  = LIGHT_BLACK
            label       = "Dark Mode"

        # Draw a filled rectangle and a 2px border for the toggle
        pygame.draw.rect(screen, rect_fill, toggle_rect)
        pygame.draw.rect(screen, rect_border, toggle_rect, 2)

        # Center the label text in that rectangle
        label_surf = baseFont.render(label, True, text_color)
        label_rect = label_surf.get_rect(center=toggle_rect.center)
        screen.blit(label_surf, label_rect.topleft)

        # Finally, render all widgets again (so they appear on top)
        window.render()
        pygame.display.update()

if __name__ == '__main__':
    main()
