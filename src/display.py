import pygame
from math import ceil
from time import time
from abc import ABC, abstractmethod

class Window:
    def __init__(self, screen):
        self.screen = screen
        self.widgets = {}

    def add_widget(self, widget_id, widget):
        self.widgets[widget_id] = widget

    def get_widget_value(self, widget_id):
        return self.widgets[widget_id].get_value()

    def set_widget_value(self, widget_id, value):
        return self.widgets[widget_id].set_value(value)
        
    def render(self):
        for widget in self.widgets.values():
            widget.render(self.screen)

    def update(self, event):
        for widget in self.widgets.values():
            widget.update(event)
        

class Box:
    def __init__(self, rect):
        self.isActive = False
        self.rect     = pygame.Rect(rect)
    
    def update(self, event):
        self.mousePos = pygame.mouse.get_pos()
        self.clicked  = event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(self.mousePos)
        self.hovered = self.rect.collidepoint(self.mousePos)


class InputBox(ABC, Box):
    def __init__(self, rect, label, color, font):
        super().__init__(rect)
        self.label  = label
        self.color = color
        self.font = font
        
    def render(self, screen):
        label = self.font.render(self.label, True, self.color)
        screen.blit(label, (self.rect.x + (self.rect.w - label.get_width()) / 2, self.rect.y - 32))
        pygame.draw.rect(screen, self.color, self.rect, 2)

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def set_value(self, value):
        pass


class TextBox(InputBox):
    def __init__(self, rect, label, color, font, text):
        super().__init__(rect, label, color, font)
        self.text = text
    
    def render(self, screen):
        super().render(screen)
        surface = self.font.render(self.text, True, self.color)
        screen.blit(surface, surface.get_rect(center=self.rect.center))

    def update(self, event):
        super().update(event)
        if self.hovered and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE: 
                self.text = self.text[:-1]
            elif event.unicode.isdigit(): 
                self.text += event.unicode
        
    def get_value(self):
        return self.text

    def set_value(self, value):
        self.text = value


class SlideBox(InputBox):
    def __init__(self, rect, label, color, font):
        super().__init__(rect, label, color, font)
        self.start = self.rect.x + 6
        self.end   = self.rect.x + self.rect.w - 6
        self.value = self.start
        self.dragging = False  # Track if the user is dragging the slider

    def render(self, screen):
        super().render(screen)
        pygame.draw.rect(screen, self.color, self.rect, 2)
        pygame.draw.line(screen, self.color, (self.start, self.rect.y + 25), (self.end, self.rect.y + 25), 2)
        pygame.draw.line(screen, self.color, (self.value, self.rect.y + 5), (self.value, self.rect.y + 45), 12)

    def update(self, event):
        super().update(event)
        self.start  = self.rect.x + 6
        self.end    = self.rect.x + self.rect.w - 6
        
        # Check if the mouse is clicking on the slider knob
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(self.mousePos):
            if self.start <= self.mousePos[0] <= self.end:
                self.dragging = True

        # Stop dragging when the mouse button is released
        if event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False

        # If dragging, move the slider with the mouse
        if self.dragging:
            self.value = min(max(self.mousePos[0], self.start), self.end)  # Restrict the slider's movement within bounds
        

    def get_value(self):
        # Normalize the value to a range between 0 and 1
        normalized_value = (self.value - self.start) / (self.end - self.start)
        return normalized_value

    def set_value(self, value):
        # Set the value within the range [start, end] based on a normalized input
        self.value = self.start + value * (self.end - self.start)

class ButtonBox(Box):
    def __init__(self, rect, inactive_img_path, active_img_path):
        super().__init__(rect)
        self.inactive_img = pygame.image.load(inactive_img_path)
        self.inactive_img = pygame.transform.scale(self.inactive_img, (rect[2], rect[3]))
        self.active_img = pygame.image.load(active_img_path)
        self.active_img = pygame.transform.scale(self.active_img, (rect[2], rect[3]))
        self.active = False
    
    def render(self, screen):
        img = self.active_img if self.active else self.inactive_img
        screen.blit(img, (self.rect.x, self.rect.y))

    def update(self, event):
        super().update(event)
        if self.clicked:
            self.active = not self.active

    def get_value(self):
        return self.active

    def set_value(self, value):
        self.active = value


class DropdownBox(InputBox):

    VISIBLE_OPTIONS = 8

    def __init__(self, rect, label, color, font, options, options_background_color):
        super().__init__(rect, label, color, font)
        self.openDropdown = False
        self.options = options
        self.options_background_color = options_background_color

        self.dropdown_rect = pygame.Rect(
            self.rect.x, 
            self.rect.y - self.rect.height * self.VISIBLE_OPTIONS,
            self.rect.width, 
            self.rect.height * self.VISIBLE_OPTIONS
        )
        self.scroll_offset = 0  # Current scroll position
        self.scrollbar_width = 5  # Width of the scrollbar
        self.selected_option = 0  # Index of the selected option

    def render(self, screen):
        super().render(screen)

        # Render the selected option in the input box
        option_text = self.font.render(self.options[self.selected_option], 1, self.color)
        screen.blit(option_text, option_text.get_rect(center=self.rect.center))

        if self.openDropdown:
            # Render the dropdown background
            pygame.draw.rect(screen, self.options_background_color, self.dropdown_rect)
            pygame.draw.rect(screen, self.color, self.dropdown_rect, 2)

            # Render visible options with scrolling
            start_index = self.scroll_offset
            end_index = min(start_index + self.VISIBLE_OPTIONS, len(self.options))

            for index in range(start_index, end_index):
                rect = self.rect.copy()
                rect.y = self.rect.y - (index - start_index + 1) * self.rect.height

                pygame.draw.rect(screen, self.options_background_color, rect)
                pygame.draw.rect(screen, self.color, rect, 1)
                option_text = self.font.render(self.options[index], 1, self.color)
                screen.blit(option_text, option_text.get_rect(center=rect.center))

            # Render the scrollbar
            self.render_scrollbar(screen)

    def render_scrollbar(self, screen):
        total_options = len(self.options)
        if total_options > self.VISIBLE_OPTIONS:
            proportion_visible = self.VISIBLE_OPTIONS / total_options
            scrollbar_height = int(self.dropdown_rect.height * proportion_visible)

            max_scroll = total_options - self.VISIBLE_OPTIONS
            proportion_scrolled = self.scroll_offset / max_scroll if max_scroll > 0 else 0
            scrollbar_rect = pygame.Rect(self.dropdown_rect.right - self.scrollbar_width,
                                         self.dropdown_rect.y + proportion_scrolled * (self.dropdown_rect.height - scrollbar_height),
                                         self.scrollbar_width, scrollbar_height)

            # Draw the scrollbar (visual only)
            pygame.draw.rect(screen, self.color, scrollbar_rect)

    def update(self, event):
        super().update(event)

        # Toggle the dropdown when the input box is clicked
        if self.clicked:
            self.openDropdown = not self.openDropdown

        if self.openDropdown:
            # Handle mouse wheel scrolling
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    self.scroll_offset = max(self.scroll_offset - 1, 0)
                elif event.button == 5:  # Scroll down
                    self.scroll_offset = min(self.scroll_offset + 1, len(self.options) - self.VISIBLE_OPTIONS)

            # Handle option selection
            self.handle_option_selection(event)

    def handle_option_selection(self, event):
        start_index = self.scroll_offset
        for index in range(start_index, start_index + self.VISIBLE_OPTIONS):
            rect = self.rect.copy()
            rect.y = self.rect.y - (index - start_index + 1) * self.rect.height

            if rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.selected_option = index
                self.openDropdown = False  # Close dropdown after selecting

    def get_value(self):
        return self.options[self.selected_option]

    def set_value(self, value):
        self.selected_option = value
