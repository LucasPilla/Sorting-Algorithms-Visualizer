import pygame
import display
from algs import algorithmsDict
from random import randint
from time import time


# Global variables
# Other global variables needed for the interface were declared in display.py
numbers = [randint(10, 400) for i in range(display.numBars)] # array to be sorted
alg_iterator = None # used to pause the sorting functions during their execution


# Actions performed by widgets when receiving user input
# They were declared in display.py
def action_change_size():
    global numbers
    display.numBars = display.size_box.value
    numbers = [randint(10, 400) for i in range(display.numBars)]

def action_change_delay():
    display.delay = display.delay_slider.value
    display.delay_label.text = str(display.delay)[:4]

def action_play():
    global numbers, alg_iterator
    display.do_sorting = True
    numbers = [randint(10, 400) for i in range(display.numBars)]
    alg_iterator = algorithmsDict[display.current_alg](numbers, 0, display.numBars-1)

def action_stop():
    display.do_sorting = False

def action_choose_alg(alg_name):
    def wrapper_action_choose_alg():
        display.current_alg = alg_name
        display.alg_label.text = display.current_alg
    return wrapper_action_choose_alg

def action_choose_theme(theme_name):
    def wrapper_action_choose_theme():
        display.current_theme = theme_name
    return wrapper_action_choose_theme


def main():
    # Set actions to be performed by widgets when receiving user input
    display.size_box.on_change = action_change_size
    display.delay_slider.on_change = action_change_delay
    display.play_button.on_click = action_play
    display.stop_button.on_click = action_stop
    for alg_name, alg_button in display.alg_buttons.items():
        alg_button.on_click = (action_choose_alg(alg_name))
    for theme_name, theme_button in display.theme_buttons.items():
        theme_button.on_click = (action_choose_theme(theme_name))

    # Initial drawing
    display.drawInterface(numbers, -1, -1, -1, -1)
    
    # Program loop
    running = True
    mouse_dragging = False
    timer = time()
    while running:
        # Parse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.__dict__['pos']
                display.handle_mouse_pressed(mouse_pos)
                mouse_dragging = True

            elif event.type == pygame.MOUSEMOTION and mouse_dragging:
                mouse_pos = event.__dict__['pos']
                display.handle_mouse_dragged(mouse_pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = event.__dict__['pos']
                display.handle_mouse_released(mouse_pos)
                mouse_dragging = False

            elif event.type == pygame.KEYDOWN:
                key = event.__dict__['unicode']
                display.handle_key_pressed(key)

        if display.do_sorting:
            try:
                if time()-timer >= display.delay:
                    array, redBar1, redBar2, blueBar1, blueBar2 = next(alg_iterator)
                    display.drawInterface(array, redBar1, redBar2, blueBar1, blueBar2)
                    timer = time()
            except StopIteration:
                display.do_sorting = False
        else:
            a_set = set(range(display.numBars))
            display.drawInterface(numbers, -1, -1, -1, -1, greenRows=a_set)


if __name__ == '__main__':
    main()
