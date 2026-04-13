import pygame
import os
from abc import ABC, abstractmethod

class Window:
    def __init__(self, screen, font_path=None, font_size=18):
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


class InputBox(Box, ABC):
    def __init__(self, rect, label, color, font):
        super().__init__(rect)
        self.label  = label
        self.color = color
        self.font = font
        
    def render(self, screen):
        label = self.font.render(self.label, True, self.color)
        label_gap = max(6, self.font.get_height() // 3)
        screen.blit(
            label,
            (self.rect.x + (self.rect.w - label.get_width()) / 2, self.rect.y - self.font.get_height() - label_gap),
        )
        radius = min(8, min(self.rect.w, self.rect.h) // 2)
        pygame.draw.rect(screen, self.color, self.rect, 2, border_radius=radius)

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
        self.focused = False

    def render(self, screen):
        super().render(screen)
        surface = self.font.render(self.text, True, self.color)
        screen.blit(surface, surface.get_rect(center=self.rect.center))

    def update(self, event):
        super().update(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.focused = self.rect.collidepoint(self.mousePos)
        if self.focused and event.type == pygame.KEYDOWN:
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
        mid = self.rect.centery
        pygame.draw.line(screen, self.color, (self.start, mid), (self.end, mid), 1)
        # Radius matches horizontal inset from border to track; clamp so the circle fits vertically
        margin = self.start - self.rect.x
        r = max(1, min(margin, self.rect.h // 2 - 1))
        pygame.draw.circle(screen, self.color, (int(self.value), mid), r)

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
        span = self.end - self.start
        if span == 0:
            return 0.0
        return (self.value - self.start) / span

    def set_value(self, value):
        span = self.end - self.start
        if span == 0:
            self.value = self.start
        else:
            self.value = self.start + value * span

class PlayStopButton(Box):
    """Toggle control: play (triangle) when idle, stop (square) while active."""

    def __init__(self, rect, color, bg=(250, 250, 250)):
        super().__init__(rect)
        self.color = color
        self.bg = bg
        self.active = False

    def render(self, screen):
        radius = min(8, min(self.rect.w, self.rect.h) // 2)
        pygame.draw.rect(screen, self.bg, self.rect)
        pygame.draw.rect(screen, self.color, self.rect, 2, border_radius=radius)

        cx, cy = self.rect.centerx, self.rect.centery
        u = min(self.rect.w, self.rect.h)
        if self.active:
            # Stop button
            side = max(8, int(u * 0.32))
            r = pygame.Rect(0, 0, side, side)
            r.center = (cx, cy)
            pygame.draw.rect(screen, self.color, r)
        else:
            # Play button
            s = u * 0.36
            left = cx - int(s * 0.45)
            right = cx + int(s * 0.65)
            top = cy - int(s * 0.75)
            bot = cy + int(s * 0.75)
            pygame.draw.polygon(screen, self.color, [(left, top), (left, bot), (right, cy)])

    def update(self, event):
        super().update(event)
        if self.clicked:
            self.active = not self.active

    def get_value(self):
        return self.active

    def set_value(self, value):
        self.active = value


class DropdownBox(InputBox):

    VISIBLE_OPTIONS = 10

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
        self.scrollbar_width = 7  # Width of the scrollbar thumb
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
            pad = 2  # inset from dropdown right edge
            thumb_w = self.scrollbar_width
            scrollbar_rect = pygame.Rect(
                self.dropdown_rect.right - thumb_w - pad,
                self.dropdown_rect.y + proportion_scrolled * (self.dropdown_rect.height - scrollbar_height),
                thumb_w,
                scrollbar_height,
            )
            r = min(5, thumb_w // 2, max(1, scrollbar_height // 2))
            pygame.draw.rect(screen, self.color, scrollbar_rect, border_radius=r)

    def update(self, event):
        super().update(event)

        if self.openDropdown and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            panel = self.rect.union(self.dropdown_rect)
            if not panel.collidepoint(event.pos):
                self.openDropdown = False

        # Toggle the dropdown when the input box is clicked
        if self.clicked:
            self.openDropdown = not self.openDropdown

        if self.openDropdown:
            # Handle mouse wheel scrolling
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    self.scroll_offset = max(self.scroll_offset - 1, 0)
                elif event.button == 5:  # Scroll down
                    max_scroll = max(0, len(self.options) - self.VISIBLE_OPTIONS)
                    self.scroll_offset = min(self.scroll_offset + 1, max_scroll)

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
        if isinstance(value, str):
            self.selected_option = self.options.index(value)
        else:
            self.selected_option = max(0, min(int(value), len(self.options) - 1))
