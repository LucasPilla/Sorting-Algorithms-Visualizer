import pygame
from random import randint
from sys import exit


# Initialize pygame modules
pygame.init()

# Display settings
windowSize = (900, 500)
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Sorting Algorithms Visualizer')

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

        def draw(self, color):
            xPos = self.rect.x
            yPos = self.rect.y
            surface = baseFont.render(self.text, True, color)
            screen.blit(self.label, (xPos+(self.rect.w - self.label.get_width())/2, yPos - 32))
            pygame.draw.rect(screen, color, self.rect, 3)
            screen.blit(surface, (xPos + 10, yPos + 10))
            self.rect.w = max(surface.get_width() + 20, self.rect.w)

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


# Font
baseFont = pygame.font.SysFont('Arial', 24)
# Buttons
sizeBox = InputBox.TextBox("Size", grey, (30, 440, 50, 50))
delayBox = InputBox.SliderBox("Delay", (105, 440, 112, 50))
algorithmBox = InputBox.TextBox("Algorithm", grey, (242, 440, 112, 50))
playButton = pygame.image.load('data/playButton.png')
playButton_rect = playButton.get_rect()
playButton_rect.center = (415, 460)
stopButton = pygame.image.load('data/stopButton.png')
stopButton_rect = stopButton.get_rect()
stopButton_rect.center = (415, 460)
button = playButton

numBars = 0
def randomList():
    """Generate a random sequence of <numBars> numbers"""
    for i in range(numBars):
        numbers.append(randint(10, 400))


def drawBars(redBar1, redBar2, blueBar1, blueBar2):
    """Draw the bars and control their colors"""
    for num in range(numBars):
        if num in [redBar1, redBar2]:
            color = red
        elif num in [blueBar1, blueBar2]:
            color = blue
        else:
            color = grey
        bar_width = 900/numBars
        pygame.draw.rect(screen, color, [num*bar_width, 400 - numbers[num], bar_width, numbers[num]])


def drawBottomMenu():
    """Draw the menu below the bars"""
    sizeBox.draw(grey)
    delayBox.draw(grey)
    algorithmBox.draw(grey)
    screen.blit(button, (390, 435))


def drawInterface(redBar1, redBar2, blueBar1, blueBar2):
    """Draw all the interface"""
    screen.fill(white)
    drawBars(redBar1, redBar2, blueBar1, blueBar2)
    drawBottomMenu()
    pygame.display.update()


def control():
    global draw
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if stopButton_rect.collidepoint(event.pos):
                draw = False


def bubblesort():
    global draw
    for i in range(numBars):
        for j in range(numBars - i - 1):
            # The three lines below are not part of the algorithm
            control()
            if draw:
                drawInterface(j, j+1, -1, -1)
                pygame.time.wait(speed)
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


def mergesort(left, right):
    if left < right:
        mid = int((left+right)/2)
        mergesort(left, mid)
        mergesort(mid+1, right)
        merge(left, mid, right)


def merge(left, mid, right):
    global draw
    L = numbers[left:mid+1]
    R = numbers[mid+1:right+1]
    i = 0
    j = 0
    k = left
    while i < len(L) and j < len(R):
        # The two lines below is not part of the algorithm
        control()
        if draw:
            drawInterface(left+i, mid+j, left, right)
            pygame.time.wait(speed)
        if L[i] < R[j]:
            numbers[k] = L[i]
            i += 1
        else:
            numbers[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        numbers[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        numbers[k] = R[j]
        j += 1
        k += 1


def quicksort(left, right):
    global draw
    if left >= right:
        return
    index = left
    for j in range(left, right):
        # The six lines below are not part of the algorithm
        control()
        if draw:
            drawInterface(j, right, index, -1)
            pygame.time.wait(speed)
        if numbers[j] < numbers[right]:
            numbers[j], numbers[index] = numbers[index], numbers[j]
            index += 1
    numbers[index], numbers[right] = numbers[right], numbers[index]
    quicksort(index + 1, right)
    quicksort(left, index - 1)


running = True
draw = True
while running:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed() != (0, 0, 0) and delayBox.rect.collidepoint(mouse):
            delayBox.write()
        # In case the mouse is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sizeBox.rect.collidepoint(mouse):
                sizeBox.isActive = True
                algorithmBox.isActive = False
            elif algorithmBox.rect.collidepoint(mouse):
                sizeBox.isActive = False
                algorithmBox.isActive = True
            elif playButton_rect.collidepoint(mouse):
                button = stopButton
                numBars = int(sizeBox.text)
                speed = delayBox.value - delayBox.rect.x - 6
                algorithm = algorithmBox.text
                numbers = []
                randomList()
                draw = True
                if algorithm == "Bubblesort":
                    bubblesort()
                elif algorithm == "Quicksort":
                    quicksort(0, numBars - 1)
                elif algorithm == "Mergesort":
                    mergesort(0, numBars - 1)
                button = playButton
        if event.type == pygame.KEYDOWN:
            if sizeBox.isActive:
                sizeBox.write(event)
            elif algorithmBox.isActive:
                algorithmBox.write(event)
    drawInterface(-1, -1, -1, -1)
