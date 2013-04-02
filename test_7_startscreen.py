# -*- coding: utf-8 -*-
#Autor: Programmer: Julian Schmelzinger, Gabriel Felder, Linus Heimböck, Valentin Nussbaumer, Tim Feldmann; Grafiker: Oskar Riedmann, Niklas Schwärzler
#Programmname: Jump'n'Run
import random
import time
import pygame, sys
from pygame.locals import* #Import pygame bibliothek

pygame.init() #Start from pygame
pygame.mixer.init()

FPS = 35 # frames per second setting
speed=random.randint(4,5)
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((1000,600), 0, 32) #draw a new window
pygame.display.set_caption('Animation')    

#color definition:
WHITE = (255, 255, 255)
BLACK=(0,0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
RED = (255, 0, 0)
MEDIUMBLUE= ( 0, 0, 205)
TEXT_COLOR=(250,69,19)

IMG_DIR = "artwork/Level_1_used/"

def init_game():
	'''
	initalize game and set all necessary variables
	'''
	
	global lifelevel
	lifelevel = 100
	global intro_running
	intro_running = True
	global counter
	counter = 0 
	global life_x
	life_x = 200
	global walker1_x
	walker1_x = 80
	global walker1_movement
	walker1_movement = 0
	global switch
	switch = 0
	global object_x
	object_x = -200
	
init_game()	
#Screen_text
fontObj = pygame.font.Font('CHERC___.TTF', 32)

#Variablen
background_x = 0
#walker1_x = 0
#walker1_movement = 0
		
y_offset = 0
y_downset = 0
#switch = 0
textx = 0
texty = 0
	

intro_running = True

#Img load
backgroundIMG = pygame.image.load(IMG_DIR + "wood1.png").convert()

img_intro = pygame.image.load(IMG_DIR + 'intro.png').convert()

img_duck = pygame.image.load(IMG_DIR + 'flying_saurian.png').convert_alpha()
img_explosion=pygame.image.load(IMG_DIR + 'crash.png').convert_alpha()
img_explosion=pygame.transform.scale(img_explosion, (img_explosion.get_width()*1, img_explosion.get_height()*1))
img_stone=pygame.image.load(IMG_DIR + 'rollingstone.png').convert_alpha()
img_stone=pygame.transform.scale(img_stone, (int(img_stone.get_width()/2), int(img_stone.get_height()/2)))
img_duck=pygame.transform.scale(img_duck, (int(img_duck.get_width()/8), int(img_duck.get_height()/8)))
img_list = [(img_stone, 360, True), (img_duck, 290, False)] # (image, y, rotate)
walkers = []
img_game_over= pygame.image.load(IMG_DIR + 'end.png').convert_alpha()
img_game_over=pygame.transform.scale(img_game_over, (int(img_game_over.get_width()*1), int(img_game_over.get_height()*1)))
pygame.mixer.music.load('sounds/spiel.mp3')
pygame.mixer.music.play(-1)
game_end=pygame.mixer.Sound('sounds/gameover.ogg')
snd_crash = pygame.mixer.Sound('sounds/crash.ogg')
snd_jump = pygame.mixer.Sound('sounds/jump.ogg')

for filename in (IMG_DIR + 'dino1.png', IMG_DIR + 'dino2.png'):
	new_walker = pygame.image.load(filename).convert_alpha()
	new_walker = pygame.transform.scale (new_walker, (new_walker.get_width() /5  , new_walker.get_height() /5))
	new_walker = pygame.transform.flip(new_walker, True, False)
	walkers.append(new_walker)



direction = 'right'


object, object_y, rotate_obj = random.choice(img_list)
object_x= DISPLAYSURF.get_width() 

snd_running = False
	
while True: # the main game loop
	
	if intro_running == True:
		# blit intro
		#intro_running = Fal
		DISPLAYSURF.blit(img_intro, (0,0))
		pygame.display.flip ()
		for event in pygame.event.get():										### neu ### 
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = event.pos
				x = pos[0]
				y = pos[1]
				if x in range(397, 600) and y in range(510, 589):
					intro_running = False
				#(397, 510)
				#(600, 589)
				print pos
			elif event.type == QUIT:												### neu ###
				pygame.quit()													### neu ###
				sys.exit()		
		
	elif life_x >= 1:		
	
		DISPLAYSURF.fill(WHITE)
		
		
		DISPLAYSURF.blit(backgroundIMG, (background_x,0))
		DISPLAYSURF.blit(backgroundIMG, (backgroundIMG.get_width()  + background_x,0))
		textSurfaceObj = fontObj.render('Gelaufene Meter:  ' + str(int(switch)) , True, TEXT_COLOR)
		
		counter += 1
		delayer = 5
		index = (counter % (len(walkers)*delayer)) / delayer
		current_walker = walkers[index]
		r_walker = DISPLAYSURF.blit(current_walker, (walker1_x, DISPLAYSURF.get_height() -115 - current_walker.get_height() - y_offset))
		
		img_life= pygame.draw.rect(DISPLAYSURF,(255, 0, 0 ), (10, 10, life_x ,25))
		
		if walker1_x < 80 and walker1_movement < 0:
			pass
		elif walker1_x >= DISPLAYSURF.get_width() - current_walker.get_width() and walker1_movement > 0:
			pass
		else:
			walker1_x += walker1_movement 
			
		if background_x == -backgroundIMG.get_width() :
			background_x = 0
		
		# draw moving object
		object_x-= speed
		object_draw = object
		if counter % 4 == 0 and rotate_obj == True:
			#print "rotate!!!!"
			object_draw = pygame.transform.rotate(object, -180) 	
		
		r_moving_object = DISPLAYSURF.blit(object_draw,(object_x,object_y))
		switch +=0.1
		if r_moving_object.colliderect(r_walker) == True:
			#if snd_running == False or (getattr(snd_running, 'get_busy') and snd_running.get_busy()):
			snd_crash.play()
			DISPLAYSURF.blit(img_explosion,(100,60))
			life_x-= 3.5                 ### neu ###
			if life_x < 10:					### neu ###
				print("Game Over!")			### neu ###
												### neu ###
				
		pygame.display.flip ()
		background_x -= 2 # background_x = background_x -1
		
		DISPLAYSURF.blit(textSurfaceObj, (DISPLAYSURF.get_width()/2 - textSurfaceObj.get_width()/2, 0))
		
		if direction == 'left':
			textx -= 10
			if textx <= 0:
				direction = 'right'
		
		
		if background_x == -backgroundIMG.get_width() :
			background_x = 0
			
		object_x-= speed	
		switch +=0.1
			
		
		if object_x < -100:
			object, object_y,rotate_obj = random.choice(img_list)
			object_x = 890
			speed = random.randint(5, 25)
		
		
		pygame.display.flip ()
		background_x -= 2 # background_x = background_x -1
		
		
		for event in pygame.event.get():
			
			if event.type == pygame.USEREVENT:
				y_offset = 0
				pygame.time.set_timer(pygame.USEREVENT, 0)
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					snd_jump.play()
					y_offset = (current_walker.get_height() + current_walker.get_height()/20)
					pygame.time.set_timer(pygame.USEREVENT, 1000)
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					y_offset = 0
					
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					y_offset =  - current_walker.get_height()/2
					pygame.time.set_timer(pygame.USEREVENT, 1000) 
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_DOWN:
					y_offset = 0
					
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					walker1_movement = 5
					#walker1_x = walker1_x + 20
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					#walker1_x = 0
					walker1_movement = -5
					
				
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				455
		pygame.display.update()
		fpsClock.tick(FPS)
		
		
	else:																		### neu ###
		DISPLAYSURF.blit(img_game_over, (0,0))
		DISPLAYSURF.blit(textSurfaceObj,(320,150))
		
		for event in pygame.event.get():										### neu ### 
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = event.pos
				x = pos[0]
				y = pos[1]
				if x in range(32,244) and y in range(429, 567):
					init_game()
				elif x in range (755,941) and y in range (488,574):
					pygame.quit()
					sys.exit()
					
				print pos		
			elif event.type == QUIT:
				pygame.quit()													### neu ###
				sys.exit()														### neu ###
				        
		game_end.play()																		### neu ###
		pygame.display.flip()													### neu ###
				
