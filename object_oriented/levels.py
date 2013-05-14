import pygame
import random
pygame.init()

class Level(object):
	'''
	all necessary data for representing a level.
	'''
	
	def __init__(self):
		self.background_img = None
		self.enemy_images = []
		self.music = None
		self.set_up()
		
	def set_up(self):
		'''
		to be implemented by derived classes!
		'''
		pass
		
	def get_random_enemy_cls(self):
		return random.choice(enemy_classes)
	
	def set_background_img(self, filepath):
		self.background_img = pygame.image.load(filepath).convert()
				
			
class WoodLevel(Level):
	def set_up(self):
		self.set_background_img('../artwork/Level_1_used/wood1.png')


# for testing stuff
if __name__ == '__main__':
	display_surf = pygame.display.set_mode((500,550), pygame.HWSURFACE)
	level = WoodLevel()
	print level.background_img
