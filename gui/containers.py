import pygame
from gui.item import Item


# Base class for containers
# A container can contain other items (see item.py)
# and therefore perform recursive method calling
# in order to diffuse informations such as "the user clicked here" in the entire GUI structure
class Container(Item):

	def __init__(self, dim):
		super().__init__(dim)
		self.items = []

	def move_to(self, x, y):
		for item in self.items:
			dx = item.rect.x-self.rect.x
			dy = item.rect.y-self.rect.y
			item.move_to(x+dx, y+dy)
		super().move_to(x, y)

	def draw(self, surface, theme):
		if theme.background['is_active']:
			pygame.draw.rect(surface, theme.background['color'], self.rect)
		for item in self.items:
			item.draw(surface, theme)

	def mouse_pressed(self, mouse_pos):
		for item in self.items:
			item.mouse_pressed(mouse_pos)

	def mouse_dragged(self, mouse_pos):
		for item in self.items:
			item.mouse_dragged(mouse_pos)

	def mouse_released(self, mouse_pos):
		for item in self.items:
			item.mouse_released(mouse_pos)

	def key_pressed(self, key):
		for item in self.items:
			item.key_pressed(key)


# This class defines a container in which items are added one at a time on the x-axis (hence forming a row)
# The padding corresponds to the extra space between the items and the container's bounding box
# The spacing corresponds to the distance between two consecutive items
# Dimensions are updated dynamically as items are added
class RowContainer(Container):

	def __init__(self, padding=(0, 0), spacing=0):
		super().__init__((2*padding[0], 2*padding[1]))
		self.padding = padding
		self.spacing = spacing

	def add_item(self, item):
		self.items.append(item)
		item.move_to(self.rect.x+self.rect.w-self.padding[0]+self.spacing, self.rect.y+self.padding[1])
		if len(self.items) > 1:
			self.rect.w += self.spacing
		self.rect.w += item.rect.w
		self.rect.h = max(self.rect.h, item.rect.h+2*self.padding[1])


# Same as RowContainer but here items are added on the y-axis (hence forming a column)
class ColContainer(Container):

	def __init__(self, padding=(0, 0), spacing=0):
		super().__init__((2*padding[0], 2*padding[1]))
		self.padding = padding
		self.spacing = spacing

	def add_item(self, item):
		self.items.append(item)
		item.move_to(self.rect.x+self.padding[0], self.rect.y+self.rect.h-self.padding[1]+self.spacing)
		self.rect.w = max(self.rect.w, item.rect.w)
		if len(self.items) > 1:
			self.rect.h += self.spacing
		self.rect.h += item.rect.h


# This class defines a container that only contains one item (passed as a constructor parameter), 
# clips it into the container's area 
# and provides scroll bars to navigate in that area
# The item's dimensions must not change after being added to that container
class ScrollContainer(Container):

	def __init__(self, dim, item, bar_thickness=10):
		super().__init__(dim)
		self.items.append(item)
		self.bar_thickness = bar_thickness
		self.clipping_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.w-self.bar_thickness, self.rect.h-self.bar_thickness)
		self.bar_x = {'value': 0, 'length': int(self.clipping_rect.w*self.clipping_rect.w/item.rect.w), 'rect': None, 'is_active': False, 'contact': {'mouse': None, 'value': None}}
		self.bar_y = {'value': 0, 'length': int(self.clipping_rect.h*self.clipping_rect.h/item.rect.h), 'rect': None, 'is_active': False, 'contact': {'mouse': None, 'value': None}}

	def move_to(self, x, y):
		super().move_to(x, y)
		self.clipping_rect.x = x
		self.clipping_rect.y = y

	def update_item_pos(self):
		self.items[0].move_to(self.clipping_rect.x-int(self.bar_x['value']*self.items[0].rect.w/self.clipping_rect.w), 
			self.clipping_rect.y-int(self.bar_y['value']*self.items[0].rect.h/self.clipping_rect.h))

	def draw(self, surface, theme):
		# draw child item in clipped area
		surface.set_clip(self.clipping_rect)
		super().draw(surface, theme)
		# draw scrolling bars
		surface.set_clip(None)
		if self.bar_x['length'] < self.clipping_rect.w:
			self.bar_x['rect'] = pygame.Rect(self.rect.x+self.bar_x['value'], self.rect.y+self.rect.h-self.bar_thickness, self.bar_x['length'], self.bar_thickness)
			pygame.draw.rect(surface, theme.color_default, self.bar_x['rect'])
		if self.bar_y['length'] < self.clipping_rect.h:
			self.bar_y['rect'] = pygame.Rect(self.rect.x+self.rect.w-self.bar_thickness, self.rect.y+self.bar_y['value'], self.bar_thickness, self.bar_y['length'])
			pygame.draw.rect(surface, theme.color_default, self.bar_y['rect'])

	def mouse_pressed(self, mouse_pos):
		if self.clipping_rect.collidepoint(mouse_pos):
			super().mouse_pressed(mouse_pos)
		elif self.bar_x['length'] < self.clipping_rect.w and self.bar_x['rect'].collidepoint(mouse_pos):
			self.bar_x['is_active'] = True
			self.bar_x['contact']['mouse'] = mouse_pos[0]
			self.bar_x['contact']['value'] = self.bar_x['value']
		elif self.bar_y['length'] < self.clipping_rect.h and self.bar_y['rect'].collidepoint(mouse_pos):
			self.bar_y['is_active'] = True
			self.bar_y['contact']['mouse'] = mouse_pos[1]
			self.bar_y['contact']['value'] = self.bar_y['value']

	def mouse_dragged(self, mouse_pos):
		if self.bar_x['is_active']:
			delta = mouse_pos[0]-self.bar_x['contact']['mouse']
			self.bar_x['value'] = min(max(self.bar_x['contact']['value']+delta, 0), self.clipping_rect.w-self.bar_x['length'])
			self.update_item_pos()
		elif self.bar_y['is_active']:
			delta = mouse_pos[1]-self.bar_y['contact']['mouse']
			self.bar_y['value'] = min(max(self.bar_y['contact']['value']+delta, 0), self.clipping_rect.h-self.bar_y['length'])
			self.update_item_pos()
		super().mouse_dragged(mouse_pos)

	def mouse_released(self, mouse_pos):
		self.bar_x['is_active'] = False
		self.bar_y['is_active'] = False
		super().mouse_released(mouse_pos)
