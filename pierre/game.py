#!/usr/bin/env python2

import pygame, random

from pygame.locals import *

def compareSequences(list1, list2):
	for i in range(0, len(list1)-1):
		if list1[i] != list2[i]:
			return False
	return True

class Game:
	def __init__(self):
		self.limit = 3
		self.sequence = []
		self.usersequence = []
		
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
		pygame.display.flip()
	
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

	def Buzz(self, color):
		pygame.mixer.stop()
		if color == 0:
			self.sound400.play()
			self.LightRed()
		elif color == 1:
			self.sound600.play()
			self.LightYellow()
		elif color == 2:
			self.sound800.play()
			self.LightBlue()
		elif color == 3:
			self.sound1000.play()
			self.LightGreen()
		pygame.display.flip()

	def Events(self):
		while 1:
			while len(self.sequence) < self.limit:
				self.ResetColors()
				pygame.time.delay(100)
				color = random.randint(0,3)
				self.sequence.append(color)
				self.Buzz(color)
				pygame.time.delay(500)
				
			while len(self.usersequence) < self.limit:
				for event in pygame.event.get():
					self.ResetColors()
					keys = pygame.key.get_pressed()
				
					if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
						quit()

					if keys[pygame.K_a]:
						self.Buzz(0)
						self.usersequence.append(0)
					if keys[pygame.K_z]:
						self.Buzz(1)
						self.usersequence.append(1)
					if keys[pygame.K_q]:
						self.Buzz(2)
						self.usersequence.append(2)
					if keys[pygame.K_s]:
						self.Buzz(3)
						self.usersequence.append(3)
			
			if compareSequences(self.sequence, self.usersequence):
				pygame.time.delay(1000)
				self.sequence = []
				self.usersequence = []
				self.limit = self.limit+1
			else:
				print "USER FAIL"
				quit()
				

game = Game()


