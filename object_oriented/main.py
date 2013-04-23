import pygame
from pygame.locals import *
import cevent
from spriteclasses import Dinosaur

class App(cevent.CEvent):
    def __init__(self):
        cevent.CEvent.__init__(self)
        self._running = True
        self._display_surf = None
        self._image_surf = None
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((350,350), pygame.HWSURFACE)
        self._running = True
        self._image_surf = pygame.image.load("myimage.jpg").convert()
        self.dinosaur = Dinosaur()
    
    def on_loop(self):
        pass
    def on_render(self):
        self._display_surf.blit(self._image_surf,(0,0))
        self._display_surf.blit(self.dinosaur.get_current_image(), self.dinosaur.rect)
        pygame.display.flip()
    
    def on_exit(self):
        self._running = False

    def on_cleanup(self):
        pygame.quit()
     
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
		
        pygame.time.set_timer(pygame.USEREVENT, 100)
        self.register_listener(pygame.USEREVENT, self.dinosaur)
        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
