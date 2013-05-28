import pygame
from levels import WoodLevel
from spriteclasses import Dinosaur, Enemy
import random

class Game(object):
    '''
    manager of the levels, handles all the movement, collision detection etc.
    '''	
    
    def __init__(self, screen):
        self.screen = screen
        self.level_classes = [WoodLevel]
        self.current_level_index = 0
        self.level = None
        self.next_level()
        self.dinosaur = Dinosaur()
        self.ran_distance = 0
        
        self.enemy = Enemy()
    def draw(self):
        '''
        paint the whole level, with moving background, dinosaur and enemies
        '''
        
        self.screen.blit(self.level.background_img, (self.background_img_x,0))
        if abs(self.background_img_x) > self.level.background_img.get_width() - self.screen.get_width():
			self.screen.blit(self.level.background_img, (self.background_img_x + self.level.background_img.get_width(),0))
			
        # TO-DO: make sure that -if necessary- the background is stitched!
        
        self.screen.blit(self.dinosaur.get_current_image(), self.dinosaur.rect)
        #self.screen.blit(self.enemy.picture, self.enemy.rect)
        
        fontObj = pygame.font.Font('CHERC___.TTF', 32)
        TEXT=(250,69,19)
        textSurfaceObj = fontObj.render('Gelaufene Meter:  ' + str(int(self.ran_distance)) , True, TEXT)
        self.screen.blit(textSurfaceObj, (self.screen.get_width()/2 - textSurfaceObj.get_width()/2, 0))
        self.screen.blit(self.enemy.picture, self.enemy.rect)
            
    def next_step(self):
        #self.erase_all()
        self.scroll_background()
        self.move_enemy()
        
    def move_enemy(self):
		self.enemy.move()
		
    def erase_all(self):
        self.screen.fill( (0, 0, 0) )
        
    def scroll_background(self):
        BACKGROUND_IMAGE_SPEED = 9  # in pixel
        self.background_img_x -= BACKGROUND_IMAGE_SPEED
        if self.background_img_x < -self.level.background_img.get_width():
            self.background_img_x = 0
	
    def next_level(self):
        self.level = self.level_classes[self.current_level_index]()
        self.current_level_index += 1
        self.background_img_x = 0

if __name__ == "__main__" :
    screen = pygame.display.set_mode((200, 200))
    game = Game(screen)
