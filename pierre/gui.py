#!/usr/bin/env python2

import pygame, sys
from pygame.locals import *

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode([630, 630])
		self.sound400 = pygame.mixer.Sound("sounds/400.wav")
		self.sound600 = pygame.mixer.Sound("sounds/600.wav")
		self.sound800 = pygame.mixer.Sound("sounds/800.wav")
		self.sound1000 = pygame.mixer.Sound("sounds/1000.wav")
		self.Events()
		pygame.mixer.pre_init(44100,-50,128)
								
	def ResetColors(self):
		red = pygame.image.load("colors/normal/red.png")
		self.screen.blit(red, (50, 50))
		yellow = pygame.image.load("colors/normal/yellow.png")
		self.screen.blit(yellow, (340, 50))
		blue = pygame.image.load("colors/normal/blue.png")
		self.screen.blit(blue, (50, 340))
		green = pygame.image.load("colors/normal/green.png")
		self.screen.blit(green, (340, 340))
	
	def LightRed(self):
		red = pygame.image.load("colors/light/red.png")
		self.screen.blit(red, (50, 50))
		
	def LightYellow(self):
		yellow = pygame.image.load("colors/light/yellow.png")
		self.screen.blit(yellow, (340, 50))
		
	def LightBlue(self):
		blue = pygame.image.load("colors/light/blue.png")
		self.screen.blit(blue, (50, 340))
		
	def LightGreen(self):
		green = pygame.image.load("colors/light/green.png")
		self.screen.blit(green, (340, 340))

	def Events(self):
		while 1:
			for event in pygame.event.get():
				self.ResetColors()
				pygame.mixer.stop()
				keys = pygame.key.get_pressed()
				
				if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
					sys.exit()

				if keys[pygame.K_a]:
					self.sound400.play()
					self.LightRed();
				if keys[pygame.K_z]:
					self.sound600.play()
					self.LightYellow();
				if keys[pygame.K_q]:
					self.sound800.play()
					self.LightBlue();
				if keys[pygame.K_s]:
					self.sound1000.play()
					self.LightGreen();
			pygame.display.flip()

game = Game()


