import pygame
from sys import exit
from math import ceil

# Initialize pygame modules
pygame.init()

# Display settings
windowSize = (900, 500)
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Sorting Algorithms Visualizer')

# Font
baseFont = pygame.font.SysFont('Arial', 24)
# Used Colors
grey = (100, 100, 100)
green = (150, 255, 150)
white = (250, 250, 250)
red = (255, 50, 50)
black = (0, 0, 0)
blue = (50, 50, 255)


class InputBox:
    class TextBox:
        def __init__(self, label, color, rect):
            self.isActive = False
            self.text = ''
            self.rect = pygame.Rect(rect)
            self.label = baseFont.render(label, True, color)

        def draw(self, color, width):
            xPos = self.rect.x
            yPos = self.rect.y
            surface = baseFont.render(self.text, True, color)
            screen.blit(self.label, (xPos+(self.rect.w - self.label.get_width())/2, yPos - 32))
            pygame.draw.rect(screen, color, self.rect, 3)
            screen.blit(surface, (xPos + 10, yPos + 10))
            self.rect.w = max(surface.get_width() + 20, width)

        def write(self, wEvent):
            if wEvent.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += wEvent.unicode

    class SliderBox:
        def __init__(self, name, rect):
            self.isActive = False
            self.rect = pygame.Rect(rect)
            self.name = name
            self.value = self.rect.x+6

        def draw(self, color):
            xPos = self.rect.x
            yPos = self.rect.y
            # Draw the label
            label = baseFont.render(self.name + ' (%dms)' % (self.value - xPos - 6), True, color)
            screen.blit(label, (xPos+(self.rect.w - label.get_width())/2, yPos - 32))
            # Draw the rect button
            pygame.draw.rect(screen, color, self.rect, 3)
            # Draw central line
            pygame.draw.line(screen, color, (xPos+6, yPos+25), (xPos+self.rect.w-6, yPos+25), 2)
            # Draw bar control
            pygame.draw.line(screen, color, (self.value, yPos+5), (self.value, yPos+45), 12)

        def write(self):
            x = pygame.mouse.get_pos()[0]
            if x <= self.rect.x+6:
                self.value = self.rect.x+6
            elif x >= self.rect.w+self.rect.x-6:
                self.value = self.rect.w+self.rect.x-6
            else:
                self.value = x


# Input Boxes
sizeBox = InputBox.TextBox("Size", grey, (30, 440, 50, 50))
delayBox = InputBox.SliderBox("Delay", (105, 440, 112, 50))
algorithmBox = InputBox.TextBox("Algorithm", grey, (242, 440, 112, 50))
# Button
playButton = pygame.image.load('data/playButton.png')
stopButton = pygame.image.load('data/stopButton.png')
button_rect = playButton.get_rect()
button_rect.center = (415, 460)

# Global Variables
numBars = 0
delay = 0
toDraw = True
button = playButton


def drawBars(array, redBar1, redBar2, blueBar1, blueBar2):
    """Draw the bars and control their colors"""
    for num in range(numBars):
        if num in [redBar1, redBar2]:
            color = red
        elif num in [blueBar1, blueBar2]:
            color = blue
        else:
            color = grey
        bar_width = 900/numBars
        pygame.draw.rect(screen, color, [num * bar_width, 400 - array[num], ceil(bar_width), array[num]])


def drawBottomMenu():
    """Draw the menu below the bars"""
    sizeBox.draw(grey, 50)
    delayBox.draw(grey)
    algorithmBox.draw(grey, 100)
    screen.blit(button, (390, 435))


def drawInterface(array, redBar1, redBar2, blueBar1, blueBar2):
    """Draw all the interface"""
    screen.fill(white)
    drawBars(array, redBar1, redBar2, blueBar1, blueBar2)
    drawBottomMenu()
    pygame.display.update()


def handleDrawing(array, redBar1, redBar2, blueBar1, blueBar2):
    global toDraw
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                toDraw = False
    if toDraw:
        drawInterface(array, redBar1, redBar2, blueBar1, blueBar2)
        pygame.time.wait(delay)
