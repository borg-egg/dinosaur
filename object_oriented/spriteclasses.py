import pygame
import random

class Dinosaur(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		image = pygame.image.load('artwork/dino1.png')
		image2 = pygame.image.load('artwork/dino2.png')
		self.images = [image, image2]
		self.image = self.images[0]
		self.index = 0
		self.rect = self.image.get_rect()
		self.rect.center = [100, 100]
		self.speed = random.randint(1, 10)
	
	def get_current_image(self):
		return self.image
	
	def process_event(self, event):
		if event.type == pygame.USEREVENT:
			self.next_image()
			
	def next_image(self):
		self.index += 1
		self.index = self.index % len(self.images)
		self.image = self.images[self.index]
	def moveleft(self):
		self.rect.center = (self.rect.center[0] - self.speed, self.rect.center[1])
	def moveright(self):
		self.rect.center = (self.rect.center[0] + self.speed, self.rect.center[1])
	def moveup(self):
		self.rect.center = (self.rect.center[0] , self.rect.center[1] - self.speed)
	def movedown(self):
		self.rect.center = (self.rect.center[0] , self.rect.center[1] + self.speed)	
		
class Enemy (pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.picture = pygame.image.load('artwork/Esteban3.png')
		self.rect = self.picture.get_rect()
		self.rect.center = [100, 500]
		self.speed = random.randint(1, 10)
		
	def move(self):
		self.rect.center = (self.rect.center[0] - self.speed, self.rect.center[1])
	
		
