import pygame
from sys import exit
from math import ceil
from time import time

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
green = (125, 240, 125)
white = (250, 250, 250)
red = (255, 50, 50)
black = (0, 0, 0)
blue = (50, 50, 255)


# THE CODE BELOW IS A MODULE FOR TAKING USER INPUT WITH PYGAME #
class InputBox:
    def __init__(self, name, color, rect):
        self.isActive = False
        self.name = name
        self.color = color
        self.rect = pygame.Rect(rect)

    def draw(self):
        label = baseFont.render(self.name, True, self.color)
        screen.blit(label, (self.rect.x + (self.rect.w - label.get_width()) / 2, self.rect.y - 32))
        pygame.draw.rect(screen, self.color, self.rect, 3)

    def update(self):
        mousePos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() != (0, 0, 0):
            if self.rect.collidepoint(mousePos):
                self.isActive = True
            else:
                self.isActive = False


class TextBox(InputBox):
    def __init__(self, name, color, rect):
        super().__init__(name, color, rect)
        self.text = ''

    def draw(self):
        super().draw()
        surface = baseFont.render(self.text, True, self.color)
        screen.blit(surface, (self.rect.x + 10, self.rect.y + 10))
        self.rect.w = max(surface.get_width() + 20, 50)

    def update(self, wEvent):
        super().update()
        if self.isActive and wEvent.type == pygame.KEYDOWN:
            if wEvent.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += wEvent.unicode


class SliderBox(InputBox):
    def __init__(self, name, color, rect):
        super().__init__(name, color, rect)
        self.value = self.rect.x+6

    def draw(self):
        super().draw()
        pygame.draw.line(screen, self.color, (self.rect.x+6, self.rect.y+25), (self.rect.x+self.rect.w-6, self.rect.y+25), 2)
        pygame.draw.line(screen, self.color, (self.value, self.rect.y+5), (self.value, self.rect.y+45), 12)

    def update(self):
        super().update()
        if self.isActive and pygame.mouse.get_pressed() != (0, 0, 0):
            x = pygame.mouse.get_pos()[0]
            if x <= self.rect.x+6:
                self.value = self.rect.x+6
            elif x >= self.rect.w+self.rect.x-6:
                self.value = self.rect.w+self.rect.x-6
            else:
                self.value = x


class ButtonBox:
    def __init__(self, stateFalse, stateTrue, rect):
        self.stateFalse = pygame.image.load(stateFalse)
        self.stateTrue = pygame.image.load(stateTrue)
        self.active = False
        self.rect = pygame.Rect(rect)

    def draw(self):
        self.rect.x = algorithmBox.rect.x+algorithmBox.rect.w+20
        pos = (self.rect.x, self.rect.y)
        if self.active:
            screen.blit(self.stateTrue, pos)
        else:
            screen.blit(self.stateFalse, pos)

    def update(self):
        if self.active:
            self.active = False
        mousePos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() != (0, 0, 0) and self.rect.collidepoint(mousePos):
            self.active = True

class DropdownBox():
    DEFAUTL_OPTION = 0

    def __init__(self, name, rect, font):
        self.isActive = False
        self.name = name
        self.color = grey
        self.options_color = white
        self.rect = pygame.Rect(rect)
        self.active_option = -1
        self.font = font

    def add_options(self, options):
        self.options = options
        dropdown_width = ceil((len(self.options)-1) * self.rect.height / self.rect.y) * self.rect.width
        self.dropdown_rect = pygame.Rect((self.rect.x, 0, dropdown_width, self.rect.y))


    def get_active_option(self):
        return self.options[self.DEFAUTL_OPTION]

    def draw(self):
        label = baseFont.render(self.name, True, self.color)
        screen.blit(label, (self.rect.x + (self.rect.w - label.get_width()) / 2, self.rect.y - 32))
        pygame.draw.rect(screen, self.color, self.rect, 3)
        option_text = self.font.render(self.options[self.DEFAUTL_OPTION], 1, grey)
        screen.blit(option_text, option_text.get_rect(center=self.rect.center))

        if self.isActive:
            column = 0
            index = 0
            rect_start = self.rect.y - self.rect.height
            for i in range(self.DEFAUTL_OPTION+1, len(self.options)):
                rect = self.rect.copy()
                rect.y -= (index + 1) * self.rect.height
                if rect.y <= self.dropdown_rect.y:
                    column += 1
                    index = 0
                    rect.y = rect_start
                index += 1
                rect.x = self.rect.x + column * self.rect.width
                
                options_color = black if i - 1 == self.active_option else grey
                pygame.draw.rect(screen, self.options_color, rect, 0)
                pygame.draw.rect(screen, self.color, rect, 3) # draw border
                option_text = self.font.render(self.options[i][:12], 1, options_color)
                screen.blit(option_text, option_text.get_rect(center=rect.center))

    def update(self):
        mouse_position = pygame.mouse.get_pos()
        column = 0
        index = 0
        rect_start = self.rect.y - self.rect.height
        for i in range(len(self.options)-1):
            rect = self.rect.copy()
            rect.y -= (index + 1) * self.rect.height
            if rect.y <= self.dropdown_rect.y:
                column += 1
                index = 0
                rect.y = rect_start
            index += 1
            rect.x = self.rect.x + column * self.rect.width

            if rect.collidepoint(mouse_position):
                self.active_option = i
        
        if pygame.mouse.get_pressed() != (0, 0, 0):
            if self.isActive and self.dropdown_rect.collidepoint(mouse_position):
                self.options[self.DEFAUTL_OPTION], self.options[self.active_option+1] =\
                     self.options[self.active_option+1], self.options[self.DEFAUTL_OPTION]
                self.active_option = -1
            self.isActive = self.rect.collidepoint(mouse_position)
        if not self.isActive:
            self.active_option = -1

# END OF MODULE #


# Input Boxes
sizeBox = TextBox("Size", grey, (30, 440, 50, 50))
delayBox = SliderBox("Delay", grey, (105, 440, 112, 50))
algorithmBox = DropdownBox("Algorithm", (242, 440, 140, 50), baseFont)
startButton = ButtonBox('images/playButton.png', 'images/stopButton.png', (390, 435, 50, 50))

# Global Variables
numBars = 0
delay = 0
toDraw = True
paused = False
timer = 0

def drawBars(array, redBar1, redBar2, blueBar1, blueBar2, **kwargs):
    """Draw the bars and control their colors"""    
    for num in range(numBars):
        if num in [redBar1, redBar2]:
            color = red
        elif num in [blueBar1, blueBar2]:            
            color = blue
        
        elif "greenRows" in kwargs and (num in (kwargs['greenRows'])):      
            color = green        
        else:
            color = grey
        bar_width = 900/numBars
        pygame.draw.rect(screen, color, [num * bar_width, 400 - array[num], ceil(bar_width), array[num]])


def drawBottomMenu():
    """Draw the menu below the bars"""
    sizeBox.draw()
    delayBox.draw()
    algorithmBox.draw()
    startButton.draw()

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)

def draw_polygon_alpha(surface, color, points):
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
    surface.blit(shape_surf, target_rect)

def drawInterface(array, redBar1, redBar2, blueBar1, blueBar2, **kwargs):
    """Draw all the interface"""
    global paused,timer
    screen.fill(white)
    drawBars(array, redBar1, redBar2, blueBar1, blueBar2, **kwargs)
    if paused and (time()-timer)<0.5:
        draw_rect_alpha(screen,(255, 255, 0, 127),[(850/2)+10, 150+10, 10, 50])
        draw_rect_alpha(screen,(255, 255, 0, 127),[(850/2)+40, 150+10, 10, 50])
    elif not paused and (time()-timer)<0.5:
        x,y = (850/2),150
        draw_polygon_alpha(screen, (150, 255, 150, 127), ((x+10,y+10),(x+10,y+50+10),(x+50,y+25+10))) 
    drawBottomMenu()
    pygame.display.update()


def handleDrawing(array, redBar1, redBar2, blueBar1, blueBar2, **kwargs):
    global toDraw,paused,timer
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if startButton.rect.collidepoint(event.pos):
                toDraw = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = True
                timer = time()
    if toDraw:
        while paused:
            drawInterface(array, redBar1, redBar2, blueBar1, blueBar2, **kwargs)
            for event in pygame.event.get():
                delayBox.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        paused = False
                        timer = time()
        drawInterface(array, redBar1, redBar2, blueBar1, blueBar2, **kwargs)
        delay = delayBox.value - delayBox.rect.x - 6
        pygame.time.wait(delay)
