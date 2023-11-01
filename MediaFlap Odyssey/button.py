class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color, interaction_image):
		self.interaction = False
		self.image = image
		self.interaction_image = interaction_image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		if self.interaction_image is None:
			self.interaction_image = self.image
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None and self.interaction == False:
			screen.blit(self.image, self.rect)
		elif self.interaction_image is not None and self.interaction == True:
			screen.blit(self.interaction_image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def buttonInteraction(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
			self.rect = self.interaction_image.get_rect(center=(self.x_pos, self.y_pos))
			self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
			self.interaction = True
			return True
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
			self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
"""
	def changeImage(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.rect = self.interaction_image.get_rect(center=(self.x_pos, self.y_pos))
			self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
			self.interaction = True
		else:
			self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
"""
