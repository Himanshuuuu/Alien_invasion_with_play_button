import pygame
from pygame.sprite import Sprite
 
class Bullet(Sprite):
 
	''' A class to manage bullets from ship '''
 
	def __init__(self, ai_Settings, screen, ship):
		''' Create a bullet object at ships current position '''
 
		super(Bullet, self).__init__()
		self.screen = screen
 
		# Create bullet at (0,0) and then set the correct position
 
		self.rect = pygame.Rect(0,0, ai_Settings.bullet_width, ai_Settings.bullet_height)
 
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
 
 
		# Store the bullets position as a decimal value
 
		self.y = float(self.rect.y)
 
		self.color = ai_Settings.bullet_color
		self.speed_factor = ai_Settings.bullet_speed_factor
 
 
 
	def update(self):
 
		''' Move the bullet on screen '''
		# Update the decimal position of the bullet
		self.y -= self.speed_factor
		# Update the rect position
		self.rect.y = self.y
 
 
	def draw_bullet(self):
		''' Draw bullet to the screen '''
 
		pygame.draw.rect(self.screen, self.color ,self.rect)