import pygame


# Base class for the GUI class hierarchy
# Defines the common attributes and methods for all items (see widgets.py and containers.py)
# Can be broken down into 3 parts : 
# 1. the space an item occupies (rect attribute and move_to methods)
# 2. how it is drawn (draw method)
# 3. how it reacts to user input (mouse_pressed/dragged/released and key_pressed methods)

class Item:

	def __init__(self, dim):
		self.rect = pygame.Rect((0, 0), dim)

	def move_to(self, x, y):
		self.rect.x = x
		self.rect.y = y

	def draw(self, surface, theme):
		pass

	def mouse_pressed(self, mouse_pos):
		pass

	def mouse_dragged(self, mouse_pos):
		pass

	def mouse_released(self, mouse_pos):
		pass

	def key_pressed(self, key):
		pass
