import pygame
from pygame.locals import *
from game import Game
import cevent

clock = pygame.time.Clock()

class App(cevent.CEvent):
    def __init__(self):
        cevent.CEvent.__init__(self)
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.game = None
       		
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((800,550), pygame.HWSURFACE)
        self._running = True
        self.game = Game(self._display_surf)
        self._image_surf = self.game.screen
    
    def on_loop(self):
        pass
    
    def on_render(self):
        if self.game:
            self.game.next_step()
            self.game.draw()
        pygame.display.flip()
    
    def on_exit(self):
        self._running = False

    def on_cleanup(self):
        pygame.quit()
    
    def on_key_down(self, event):
		if event.key == pygame.K_RIGHT:
			print "key right"
			self.game.dinosaur.moveright()
		if event.key == pygame.K_LEFT:
			print "key left"
			self.game.dinosaur.moveleft()
		if event.key == pygame.K_UP:
			self.game.dinosaur.moveup()
		if event.key == pygame.K_DOWN:
			self.game.dinosaur.movedown()
		if event.key in (pygame.K_KP_MINUS, pygame.K_MINUS):
			self.game.dinosaur.decrease_size()
		if event.key in (pygame.K_KP_PLUS, pygame.K_PLUS):
			self.game.dinosaur.increase_size()
		#self.enemy.move()
		
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
		
        pygame.time.set_timer(pygame.USEREVENT, 100)
        self.register_listener(pygame.USEREVENT, self.game.dinosaur)
        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            clock.tick(35)
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
