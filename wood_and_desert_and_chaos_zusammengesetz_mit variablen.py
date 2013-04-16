# -*- coding: utf-8 -*-
#Autor: Programmierer: Julian Schmelzinger, Gabriel Felder, Linus Heimböck, Valentin Nussbaumer, Tim Feldmann; Grafiker: Oskar Riedmann, Niklas Schwärzler
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
TEXT=(250,69,19)

#Directory
IMG_DIR_LEVEL_WOOD = "artwork/Level_1_used/"
IMG_DIR_LEVEL_DESERT= "artwork/Level_2_used/"
IMG_DIR_LEVEL_CHAOS= "artwork/Level_3_used/"

USER_VENT = pygame.USEREVENT + 1
pygame.time.set_timer(USER_VENT, 5*1000)
USER_VENT1 = pygame.USEREVENT + 2
pygame.time.set_timer(USER_VENT1, 10*1000)

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
	global img_list_wood
	global img_list_desert
	global walkers
	
	
init_game()	
#Writing
fontObj = pygame.font.Font('CHERC___.TTF', 32)

#Variablen
background_x = 0
#walker1_x = 0
walker1_movement = 0
		
y_offset = 0
x_offset=0
y_downset = 0
#switch = 0
textx = 0
texty = 0
	


intro_running = True

#Img load
backgroundIMG = pygame.image.load(IMG_DIR_LEVEL_WOOD + "wood1.png").convert()
backgroundIMG_desert = pygame.image.load(IMG_DIR_LEVEL_DESERT + "desert.png").convert()
backgroundIMG_chaos = pygame.image.load(IMG_DIR_LEVEL_CHAOS + "Flippyworld.png").convert()

img_flying_esteban = pygame.image.load(IMG_DIR_LEVEL_CHAOS + 'Esteban1.png').convert_alpha()
img_flying_esteban = pygame.transform.scale(img_flying_esteban, (int(img_flying_esteban.get_width()/2), int(img_flying_esteban.get_height()/2)))

img_theodor = pygame.image.load(IMG_DIR_LEVEL_CHAOS + 'Theodor.png').convert_alpha()
img_theodor = pygame.transform.scale(img_theodor, (int(img_theodor.get_width()/4), int(img_theodor.get_height()/4)))

img_flying_chip = pygame.image.load(IMG_DIR_LEVEL_DESERT + 'chip.png').convert_alpha()
img_flying_chip = pygame.transform.scale(img_flying_chip, (int(img_flying_chip.get_width()/10), int(img_flying_chip.get_height()/10)))

img_chap = pygame.image.load(IMG_DIR_LEVEL_DESERT + 'chap.png').convert_alpha()
img_chap = pygame.transform.scale(img_chap, (int(img_chap.get_width()/10), int(img_chap.get_height()/10)))

img_intro = pygame.image.load(IMG_DIR_LEVEL_WOOD + 'intro.png').convert()

img_flying_saurian = pygame.image.load(IMG_DIR_LEVEL_WOOD + 'flying_saurian.png').convert_alpha()
img_flying_saurian = pygame.transform.scale(img_flying_saurian, (int(img_flying_saurian.get_width()/8), int(img_flying_saurian.get_height()/8)))

img_crash=pygame.image.load(IMG_DIR_LEVEL_WOOD + 'crash.png').convert_alpha()
img_crash=pygame.transform.scale(img_crash, (img_crash.get_width()*1, img_crash.get_height()*1))

img_stone=pygame.image.load(IMG_DIR_LEVEL_WOOD + 'rollingstone.png').convert_alpha()
img_stone=pygame.transform.scale(img_stone, (int(img_stone.get_width()/2), int(img_stone.get_height()/2)))

img_game_over= pygame.image.load(IMG_DIR_LEVEL_WOOD + 'end.png').convert_alpha()
img_game_over=pygame.transform.scale(img_game_over, (int(img_game_over.get_width()*1), int(img_game_over.get_height()*1)))

img_list_wood = [(img_stone, 360, True), (img_flying_saurian, 290, False)] # (image, y, rotate)
img_list_desert =[(img_chap, 360, False), (img_flying_chip, 290, False)]
img_list_chaos = [(img_theodor, 360, False), (img_flying_esteban, 290, False)]
walkers = []

#sounds
pygame.mixer.music.load('sounds/spiel.mp3')
pygame.mixer.music.play(-1)
game_end=pygame.mixer.Sound('sounds/gameover.ogg')
snd_crash = pygame.mixer.Sound('sounds/crash.ogg')
snd_jump = pygame.mixer.Sound('sounds/jump.ogg')

for filename in ( 'dino1.png', 'dino2.png'):
	new_walker = pygame.image.load(IMG_DIR_LEVEL_WOOD + filename).convert_alpha()
	new_walker = pygame.transform.scale (new_walker, (new_walker.get_width() /5  , new_walker.get_height() /5))
	new_walker = pygame.transform.flip(new_walker, True, False)
	walkers.append(new_walker) 
direction = 'right'




object, object_y, rotate_obj = random.choice(img_list_wood)
object_x= DISPLAYSURF.get_width() 

snd_running = False

def process_and_execute_quit_event(event):
	if event.type == QUIT:										
		pygame.quit()													
		sys.exit()

def check_for_start():
	for event in pygame.event.get():
		process_and_execute_quit_event(event)	 
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = event.pos
			x = pos[0]
			y = pos[1]
			if x in range(397, 600) and y in range(510, 589):
				return True
	
	return False
	
def show_intro():
		DISPLAYSURF.blit(img_intro, (0,0))
		pygame.display.flip()

def set_walker_y_offset(offset):
	y_offset = offset
	global y_offset
	
def set_walker_x_offset(offset):
	x_offset = offset
	global x_offset

def process_event(event):
	process_and_execute_quit_event(event)
	               
	if event.type == pygame.USEREVENT:
		set_walker_y_offset(0)
		pygame.time.set_timer(pygame.USEREVENT, 0) # disable event timer
		
	if event.type == USER_VENT:
		global backgroundIMG
		backgroundIMG = backgroundIMG_desert
		global img_list_wood
		img_list_wood = img_list_desert
		global walkers
		walkers = []
		for filename in ( 'aladino1.png', 'aladino2.png','aladino3.png','aladino4.png','aladino5.png'):
			new_walker = pygame.image.load(IMG_DIR_LEVEL_DESERT + filename).convert_alpha()
			new_walker = pygame.transform.scale (new_walker, (new_walker.get_width() /6  , new_walker.get_height() /6))
			walkers.append(new_walker) 
		pygame.time.set_timer(USER_VENT, 0)
		
	if event.type == USER_VENT1:
		global backgroundIMG
		backgroundIMG = backgroundIMG_chaos
		global img_list_desert
		img_list_wood = img_list_chaos
		global walkers
		walkers = []
		for filename in ( 'psychohaesslich.png', 'psychohaesslich.png'):
			new_walker = pygame.image.load(IMG_DIR_LEVEL_CHAOS + filename).convert_alpha()
			new_walker = pygame.transform.scale (new_walker, (new_walker.get_width() /6  , new_walker.get_height() /6))
			new_walker = pygame.transform.flip(new_walker, True, False)
			walkers.append(new_walker) 
			
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_UP:
			snd_jump.play()
			y_offset = (current_walker.get_height() + current_walker.get_height()/20)
			set_walker_y_offset(y_offset)
			pygame.time.set_timer(pygame.USEREVENT, 1000)
			
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_UP:
			set_walker_y_offset(0)
			
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_DOWN:
			y_offset =  - current_walker.get_height()/2
			set_walker_y_offset(y_offset)
			pygame.time.set_timer(pygame.USEREVENT, 1000) 
			
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_DOWN:
			set_walker_y_offset(0)
			
			
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			print "key down"
			walker1_movement = 5
			global walker1_movement
					
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_RIGHT:
			walker1_movement = -5
			
			
			
			
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_RIGHT:
			#walker1_x = 0
			walker1_movement = -5
		
		
		
	
while True: # the main game loop
	
	if intro_running == True:
		show_intro()
		start_program = check_for_start()
		intro_running = not start_program
		
				
		
	elif life_x >= 1:		
	
		DISPLAYSURF.fill(WHITE)
		
		
		DISPLAYSURF.blit(backgroundIMG, (background_x,0))
		DISPLAYSURF.blit(backgroundIMG, (backgroundIMG.get_width()  + background_x,0))
		textSurfaceObj = fontObj.render('Gelaufene Meter:  ' + str(int(switch)) , True, TEXT)
		
		counter += 1
		delayer = 5
		index = (counter % (len(walkers)*delayer)) / delayer
		current_walker = walkers[index]
		r_walker = DISPLAYSURF.blit(current_walker, (walker1_x, DISPLAYSURF.get_height() -115 - current_walker.get_height() - y_offset))
		
		img_life= pygame.draw.rect(DISPLAYSURF,(255, 0, 0 ), (10, 10, life_x ,25))
		
		print "walker1", walker1_movement
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
			
			snd_crash.play()
			DISPLAYSURF.blit(img_crash,(100,60))
			life_x-= 3.5                 
			if life_x < 10:					
				print("Game Over!")			
												
				
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
			object, object_y,rotate_obj = random.choice(img_list_wood)
			object_x = 890
			speed = random.randint(5, 25)
		
		
		pygame.display.flip ()
		background_x -= 2 # background_x = background_x -1
		
		for event in pygame.event.get():
			process_event(event)
			
				
		pygame.display.update()
		fpsClock.tick(FPS)
		
		
	else:																		
		DISPLAYSURF.blit(img_game_over, (0,0))
		DISPLAYSURF.blit(textSurfaceObj,(320,150))
		
		for event in pygame.event.get():										 
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
				pygame.quit()													
				sys.exit()														
				        
		game_end.play()																		
		pygame.display.flip()													
				
