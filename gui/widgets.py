import pygame
from gui.item import Item


# The dimensions of a widget (width and height) are given at construction time
# and should not be changed afterward


# Default action
def action_default():
	pass


# This class defines a simple label in order to display text to the user
# It is not interactive, however the text attribute can be accessed and modified at run time
class Label(Item):

	def __init__(self, dim, text):
		super().__init__(dim)
		self.text = text

	def draw(self, surface, theme):
		surface_text = theme.font.render(self.text, True, theme.color_default)
		dx = (self.rect.w-surface_text.get_width())/2
		dy = (self.rect.h-surface_text.get_height())/2
		surface.blit(surface_text, (self.rect.x+dx, self.rect.y+dy))


# This class defines a basic button
# It reacts to clicks by calling the on_click function (passed as a constructor parameter)
class Button(Item):

	def __init__(self, dim, on_click=action_default, border_thickness=3):
		super().__init__(dim)
		self.on_click = on_click
		self.is_active = False
		self.border_thickness = border_thickness

	def draw(self, surface, theme):
		color = theme.color_default
		if self.is_active:
			color = theme.color_active
		pygame.draw.rect(surface, color, self.rect, self.border_thickness)

	def mouse_pressed(self, mouse_pos):
		if self.rect.collidepoint(mouse_pos):
			self.is_active = True

	def mouse_released(self, mouse_pos):
		if self.is_active:
			self.on_click()
			self.is_active = False


# Same as Button but with text written inside it
# The text attribute can be accessed and modified at run time
class TextButton(Button):

	def __init__(self, dim, text, on_click=action_default, border_thickness=3):
		super().__init__(dim, on_click, border_thickness)
		self.text = text

	def draw(self, surface, theme):
		super().draw(surface, theme)
		color = theme.color_default
		if self.is_active:
			color = theme.color_active
		surface_text = theme.font.render(self.text, True, color)
		dx = (self.rect.w-surface_text.get_width())/2
		dy = (self.rect.h-surface_text.get_height())/2
		surface.blit(surface_text, (self.rect.x+dx, self.rect.y+dy))


# Same as Button but with an icon drawn inside it
# The icon attribute can be accessed and modified at run time
# All icons used must be pygame surfaces
class IconButton(Button):

	def __init__(self, dim, icon, on_click=action_default, border_thickness=3):
		super().__init__(dim, on_click, border_thickness)
		self.icon = icon

	def draw(self, surface, theme):
		super().draw(surface, theme)
		dx = (self.rect.w-self.icon.get_width())/2
		dy = (self.rect.h-self.icon.get_height())/2
		surface.blit(self.icon, (self.rect.x+dx, self.rect.y+dy))


# This class defines an horizontal slider
# It reacts to dragging the cursor with the mouse by changing its value attribute (between 0 and 1)
# and to releasing the cursor by calling the on_change function (passed as a constructor parameter)
class Slider(Item):

	def __init__(self, dim, on_change=action_default, default_value=0, line_thickness=2, cursor_size=6):
		super().__init__(dim)
		self.on_change = on_change
		self.is_active = False
		self.value = default_value
		self.cursor_rect = None
		self.line_thickness = line_thickness
		self.cursor_size = cursor_size

	def line_at(self, v):
		return ((self.rect.x+self.cursor_size) + v*(self.rect.w-2*self.cursor_size), self.rect.y + (self.rect.h/2))

	def cursor_pos(self):
		return self.line_at(self.value)

	def draw(self, surface, theme):
		pygame.draw.line(surface, theme.color_default, self.line_at(0), self.line_at(1), self.line_thickness)
		color = theme.color_default
		if self.is_active:
			color = theme.color_active
		self.cursor_rect = pygame.draw.circle(surface, color, self.cursor_pos(), self.cursor_size)

	def mouse_pressed(self, mouse_pos):
		if self.cursor_rect.collidepoint(mouse_pos):
			self.is_active = True

	def mouse_dragged(self, mouse_pos):
		if self.is_active:
			x_min = self.line_at(0)[0]
			x_max = self.line_at(1)[0]
			x = min(max(mouse_pos[0], x_min), x_max)
			self.value = (x-x_min)/(x_max-x_min)
			self.on_change()

	def mouse_released(self, mouse_pos):
		if self.is_active:
			self.is_active = False


# This class defines a text input box in which it is only possible to write digits
# The last digit can be removed by pressing the backspace key
# The box has to be clicked to get activated (and therefore become editable)
# Pressing the return key will unactivate the box and call the on_change function (passed as a constructor parameter)
class DigitInputBox(Item):

	def __init__(self, dim, on_change=action_default, default_value=100, border_thickness=3):
		super().__init__(dim)
		self.on_change = on_change
		self.is_active = False
		self.value = default_value
		self.border_thickness = border_thickness

	def draw(self, surface, theme):
		color = theme.color_default
		if self.is_active:
			color = theme.color_active
		pygame.draw.rect(surface, color, self.rect, self.border_thickness)
		surface_text = theme.font.render(str(self.value), True, color)
		dx = (self.rect.w-surface_text.get_width())/2
		dy = (self.rect.h-surface_text.get_height())/2
		surface.blit(surface_text, (self.rect.x+dx, self.rect.y+dy))

	def mouse_pressed(self, mouse_pos):
		if self.rect.collidepoint(mouse_pos) and not self.is_active:
			self.is_active = True

	def key_pressed(self, key):
		if self.is_active:
			if key == '\r':
				self.is_active = False
				self.on_change()
			elif key == '\b':
				text = str(self.value)
				text = text[:-1]
				if not text:
					self.value = 0
				else:
					self.value = int(text)
			elif key.isdigit():
				text = str(self.value)
				text = text + key
				self.value = int(text)
