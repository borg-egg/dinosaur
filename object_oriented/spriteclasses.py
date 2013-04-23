import pygame

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
	
	def get_current_image(self):
		return self.image
	
	def process_event(self, event):
		if event.type == pygame.USEREVENT:
			self.next_image()
			
	def next_image(self):
		self.index += 1
		self.index = self.index % len(self.images)
		self.image = self.images[self.index]
