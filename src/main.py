import pygame
from random import randint
from time import time
from algs import algorithmsDict
import display as display
import os
import imageio.v3

# Declared in display.py
# 1. global variables : numBars, delay, do_sorting, paused, timer_space_bar
# 2. widgets : sizeBox, delayBox, algorithmBox, playButton, stopButton


SCREENSHOT_FILENAME = "screenshot" #+ a counter number
GIF_WINDOW_SIZE = (900, 420)

def getMaxNumber(files):
    currentMax  = -1
    for item in files:
        myNumber = int(item[len(SCREENSHOT_FILENAME):len(item)-4])
        if myNumber > currentMax:
            currentMax = myNumber
    return currentMax

def main():
    numbers = []
    running = True
    display.algorithmBox.add_options(list(algorithmsDict.keys()))

    current_alg = None
    alg_iterator = None

    timer_delay = time()
    counter = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and display.do_sorting:
                display.paused = not display.paused
                display.timer_space_bar = time()

            display.updateWidgets(event)

        display.delay = (display.delayBox.value-display.delayBox.rect.x-6)/1000 # delay is in ms

        if display.playButton.isActive: # play button clicked
            display.playButton.isActive = False
            display.do_sorting = True
            current_alg = display.algorithmBox.get_active_option()
            display.numBars = int(display.sizeBox.text)
            numbers = [randint(10, 400) for i in range(display.numBars)] # random list to be sorted
            alg_iterator = algorithmsDict[current_alg](numbers, 0, display.numBars-1) # initialize iterator

        if display.stopButton.isActive: # stop button clicked
            display.stopButton.isActive = False
            display.do_sorting = False
            display.paused = False
            try: # deplete generator to display sorted numbers
                while True:
                    numbers, redBar1, redBar2, blueBar1, blueBar2 = next(alg_iterator)
            except StopIteration:
                pass
            #Check if pictures are there, and if so then output gif
            #Check if user wants GIF
            print("No gif check, that's not good!")
            if True: #ADD SOME KIND OF GIF CHECK
                #Idea is that pictures are generated with numbers 0 to some MAX
                maxNumber = counter#So find MAX
                print(str(maxNumber))
                fileNames = [] #Okay, let's start preparing for GIF
                for i in range(0,maxNumber):
                    fileNames.append(SCREENSHOT_FILENAME + str(i) + ".jpg")
                images = []
                #This will start to load in individual pictures into gif engine
                for filename in fileNames:
                    images.append(imageio.v2.imread(filename))
                #Output gif!
                #imageio.mimsave("test", images)
                imageio.mimsave('sorting.gif', images, format = 'GIF-PIL', fps = 100)
                #Delete all files in folder
                print("Attempting to delete temporary files!")
                for i in range(0,maxNumber):
                    try:
                        os.remove(SCREENSHOT_FILENAME + str(i) + ".jpg")
                    except:
                        print("IO error, will attempt to continue!")
            counter = 0
        #Initialize screenshot area        
        screenshot = pygame.Surface(GIF_WINDOW_SIZE)
        screenshot.blit(display.screen, (0,0))
        if display.do_sorting and not display.paused: # sorting animation
            try:
                if time()-timer_delay >= display.delay:
                    numbers, redBar1, redBar2, blueBar1, blueBar2 = next(alg_iterator)
                    display.drawInterface(numbers, redBar1, redBar2, blueBar1, blueBar2)
                    pygame.image.save(screenshot, "screenshot" + str(counter) + ".jpg")
                    timer_delay = time()
                    counter += 1
            except StopIteration:
                display.do_sorting = False
        elif display.do_sorting and display.paused: # animation paused
            display.drawInterface(numbers, -1, -1, -1, -1)
        else: # no animation
            a_set = set(range(display.numBars))
            display.drawInterface(numbers, -1, -1, -1, -1, greenRows=a_set)

if __name__ == '__main__':
    main()
