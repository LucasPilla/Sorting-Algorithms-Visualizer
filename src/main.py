import pygame
from random import randint
from time import time
from algs import algorithmsDict
import display as display
import os
import imageio.v3
import gc

# Declared in display.py
# 1. global variables : numBars, delay, do_sorting, paused, timer_space_bar
# 2. widgets : sizeBox, delayBox, algorithmBox, playButton, stopButton



#Generating gifs requires placing files in subfolder and then loading them.
#This deletes everything except gif
def deleteTempFiles():
    try:
        myFiles = []
        myDir = []
        for pathnames,dirnames,filenames in os.walk("pictures"):
            myFiles.extend(filenames)
            myDir.extend(dirnames)
        for files in myFiles:
            os.remove("pictures/" + files)
        for directories in myDir:
            os.rmdir("pictures/" + directories)
    except:
        raise EIO("Could not delete files in subfolder!")

def CreateGIF(counter,SCREENSHOT_FILENAME):
    #Idea is that pictures are generated with numbers 0 to some MAX
    print("Trying to generate GIF, this may freeze the program and take a while")
    #Find max
    fileNames = [] #Okay, let's start preparing for GIF
    for i in range(0,counter):
        fileNames.append(SCREENSHOT_FILENAME + str(i) + ".jpg")
    images = []
    #This will start to load in individual pictures into gif engine
    #In theory, an optimization is possible here by streaming the data in smaller batches
    #This would save alot of memory
    try:
        for filename in fileNames:
            images.append(imageio.v2.imread(filename))
    except:
        raise EIO("Tried to create GIF, did not find sample pictures")
    #Output gif
    imageio.mimsave('sorting.gif', images, format = 'GIF-PIL', fps = 100)
    #Del latest list, this does NOT decrease current RAM usage, 
    #but makes next round use the same memory area instead
    del fileNames
    for item in images:
        del item
    del images
    gc.collect()
    print("GIF generated as sorting.gif folder")
    #Delete all files in folder
    deleteTempFiles()
    
    
def getMaxNumber(files):
    currentMax  = -1
    for item in files:
        myNumber = int(item[len(SCREENSHOT_FILENAME):len(item)-4])
        if myNumber > currentMax:
            currentMax = myNumber
    return currentMax

def takePicture(SCREENSHOT_FILENAME,GIF_picture_counter,screenshot):
    pygame.image.save(screenshot, "pictures/screenshot" + str(GIF_picture_counter) + ".jpg")

def main():
    SCREENSHOT_FILENAME = "pictures/screenshot" #+ a counter number + JPG
    GIF_WINDOW_SIZE = (900, 400)
    
    numbers = []
    running = True
    display.algorithmBox.add_options(list(algorithmsDict.keys()))

    current_alg = None
    alg_iterator = None

    timer_delay = time()
    
    #One keeps track of how many files have been created, the other how many total images
    GIF_picture_counter = 0
    GIF_skip_image_counter = 0
    
    #Just to make sure nothing from prev runs is left
    deleteTempFiles()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and display.do_sorting:
                display.paused = not display.paused
                display.timer_space_bar = time()

            display.updateWidgets(event)

        display.delay = (display.delayBox.value-display.delayBox.rect.x-6)/1000 # delay is in ms
        
        #Check if user pressed button, if so then active GIF output
        if display.gifCheckBox.isActive and not display.do_sorting:
            try:
                if int(display.sizeBox.text) > 1000:
                    #This is limitation because of RAM. size = 100 needs 2GB of RAM, so 120 is for some reason significantly higher
                    print("GIF cannot be created for size > 1000")
                else:
                    if int(display.sizeBox.text) > 500:
                        print("Warning: Creating a GIF for array > 500 will require more than 8GB of memory")
                    display.gifCheckBox.switch()
            except:
                raise ValueError("Text in size field is not a number")
            display.gifCheckBox.isActive = False
            
        
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
            #Check if user wants GIF, then delete temp files. No gif is possible becuase early stop
            if display.gifCheckBox.checked:
                deleteTempFiles()
                GIF_picture_counter = 0
                GIF_skip_image_counter = 0
                
        #GIF needs it's own thing
        if display.gifCheckBox.checked:
            screenshot = pygame.Surface(GIF_WINDOW_SIZE)
            screenshot.blit(display.screen, (0,0))
        
        if display.do_sorting and not display.paused: # sorting animation
            try:
                if time()-timer_delay >= display.delay:
                    numbers, redBar1, redBar2, blueBar1, blueBar2 = next(alg_iterator)
                    display.drawInterface(numbers, redBar1, redBar2, blueBar1, blueBar2)
                    #If GIF is to be output, a picture needs to be generated and saved temporarily
                    if display.gifCheckBox.checked:
                        #If less then 300, take every size/100 picture
                        #ergo size = 100 => every picture, size = 300 => every third picture
                        if int(display.sizeBox.text) <= 300:
                            if GIF_skip_image_counter % int(int(display.sizeBox.text)/100) == 0 or int(display.sizeBox.text) < 100:
                                takePicture(SCREENSHOT_FILENAME,GIF_picture_counter,screenshot)
                                GIF_picture_counter +=1
                            GIF_skip_image_counter +=1
                        #If size > 300, then we need to take draastically less pictures
                        else:
                            if int(GIF_skip_image_counter) % int(int(display.sizeBox.text)/20) == 0:
                                takePicture(SCREENSHOT_FILENAME,GIF_picture_counter,screenshot)
                                GIF_picture_counter +=1
                            GIF_skip_image_counter +=1
                    timer_delay = time()
                    
            except StopIteration:
                display.do_sorting = False
                #If program stops because end of sorting, gif needs to be created if selected
                if display.gifCheckBox.checked: #Check if GIF was requested
                    #Call function for GIF
                    CreateGIF(GIF_picture_counter,SCREENSHOT_FILENAME)
                    #Reset counter
                    GIF_picture_counter = 0
                    GIF_skip_image_counter = 0
                
        elif display.do_sorting and display.paused: # animation paused
            display.drawInterface(numbers, -1, -1, -1, -1)
        else: # no animation
            a_set = set(range(display.numBars))
            display.drawInterface(numbers, -1, -1, -1, -1, greenRows=a_set)

if __name__ == '__main__':
    main()
