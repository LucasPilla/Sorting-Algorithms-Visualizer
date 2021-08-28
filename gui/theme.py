# Encaplulates the idea of theme to make it easier to define different themes (e.g. light and dark)
# and switch between them at run time
# Instances of this class are called in the draw method of item objects (see item.py) 
class Theme:

	def __init__(self, font, color_default, color_active):
		self.font = font # for widgets with text (Label, TextButton, DigitInputBox)
		self.color_default = color_default # used for inactive widgets
		self.color_active = color_active # used to highlight an active widget (e.g. a button being clicked)
		self.background = {'is_active': False, 'color': None} # no background by default

	def fill_background(self, color):
		self.background['is_active'] = True
		self.background['color'] = color

	def no_fill(self):
		self.background['is_active'] = False
