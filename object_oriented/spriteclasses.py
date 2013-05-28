import pygame
import random

class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image_1 = pygame.image.load('artwork/dino1.png').convert_alpha()
        image_2 = pygame.image.load('artwork/dino2.png').convert_alpha()
        
        self.original_images = [image_1, image_2]
        
        self.images = [image_1, image_2]
        self.image = self.images[0]
        self.index = 0
        self.rect = self.image.get_rect()
        self.rect.center = [400, 400]
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

    def increase_size(self):
        center = self.rect.center
        resized_images = []
        for image in self.original_images:
            resized_image = pygame.transform.smoothscale(image, (image.get_width() *2, image.get_height() *2))
            resized_images.append(resized_image)
        self.images = resized_images
        image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        
        
        
        
        pass

    def decrease_size(self):
        center = self.rect.center
        print("kleiner")
        print "before", center
        resized_images = []
        for image in self.images:
            resized_image = pygame.transform.smoothscale(image, (image.get_width() / 2, image.get_height() / 2))
            resized_images.append(resized_image)
        self.images = resized_images
        image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        print "after", center
        
        
class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.picture= pygame.image.load('artwork/Esteban3.png')
		self.rect = self.picture.get_rect()
		self.rect.center = [900, 300]
		self.speed = random.randint(1, 10)
		
		
	def move(self):
		self.rect.center = (self.rect.center[0] - self.speed, self.rect.center[1])
	
		
