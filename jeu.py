#!/usr/bin/python

import time 
import pygame, sys, random
from sys import exit

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
SelecObject = 0
menu_item = ()
valueMouse = 0
premiereMain = False



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
		pygame.mouse.set_visible(True)
		self.screen = screen
		self.backgroundDark = pygame.image.load('backgroundDark.jpg')
		screen.blit(self.backgroundDark, (0, 0))
		self.sound400 = pygame.mixer.Sound("pierre/sounds/400.wav")
		self.sound600 = pygame.mixer.Sound("pierre/sounds/600.wav")
		self.sound800 = pygame.mixer.Sound("pierre/sounds/800.wav")
		self.sound1000 = pygame.mixer.Sound("pierre/sounds/1000.wav")
		self.Events()
		pygame.mixer.pre_init(44100,-50,128)

	def ResetColors(self):
		red = pygame.image.load("pierre/colors/normal/red.png")
		self.screen.blit(red, (pygame.display.Info().current_w/3.5, pygame.display.Info().current_h/14))
		yellow = pygame.image.load("pierre/colors/normal/yellow.png")
		self.screen.blit(yellow, (pygame.display.Info().current_w/1.8, pygame.display.Info().current_h/14))
		blue = pygame.image.load("pierre/colors/normal/blue.png")
		self.screen.blit(blue, (pygame.display.Info().current_w/3.5, pygame.display.Info().current_h/2))
		green = pygame.image.load("pierre/colors/normal/green.png")
		self.screen.blit(green, (pygame.display.Info().current_w/1.8, pygame.display.Info().current_h/2))
		pygame.display.flip()

	def LightRed(self):
		red = pygame.image.load("pierre/colors/light/red.png")
		self.screen.blit(red, (pygame.display.Info().current_w/3.5, pygame.display.Info().current_h/14))

	def LightYellow(self):
		yellow = pygame.image.load("pierre/colors/light/yellow.png")
		self.screen.blit(yellow, (pygame.display.Info().current_w/1.8, pygame.display.Info().current_h/14))

	def LightBlue(self):
		blue = pygame.image.load("pierre/colors/light/blue.png")
		self.screen.blit(blue, (pygame.display.Info().current_w/3.5, pygame.display.Info().current_h/2))

	def LightGreen(self):
		green = pygame.image.load("pierre/colors/light/green.png")
		self.screen.blit(green, (pygame.display.Info().current_w/1.8, pygame.display.Info().current_h/2))

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
                score = 0
                letter = pygame.font.Font('Alphabet Souplings.ttf', 15)
		while 1:
                        screen.blit(self.backgroundDark, (0, 0))
                        text = letter.render(("Score: " + str(score)), 1, (255, 255, 255))
                        textpos = text.get_rect()
                        textpos.right = screen.get_width() - 120
                        textpos.top = screen.get_height()/14
                        screen.blit(text, textpos)
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
				score += 1
			else:
				print "USER FAIL"
				quit()
            
            
class MenuItem(pygame.font.Font):
    def __init__(self, text, font='Alphabet Souplings.ttf', font_size=35,
                font_color=WHITE, (pos_x, pos_y)=(0, 0)):

        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height + 60
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
        self.is_selected = False

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)

    def is_mouse_selection(self, (posx, posy)):
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
            (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False
        


class GameSettings():
    def __init__(self, screen, items, font='Alphabet Souplings.ttf', font_size=35,
                    font_color=WHITE):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.clock = pygame.time.Clock()

        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item, font, font_size, font_color)

            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            
            pos_y = (self.scr_height / 2) - (t_h-150) + ((index*2) + index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)

        self.mouse_is_visible = True
        self.cur_item = None

    def set_mouse_visibility(self):
        if self.mouse_is_visible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)

    def set_item_selection(self, key):
        """
        Marks the MenuItem chosen via up and down keys.
        """
        for item in self.items:
            # Return all to neutral
            item.set_italic(False)
            item.set_font_color(WHITE)

        if self.cur_item is None:
            self.cur_item = 0
        else:
            # Find the chosen item
            if key == pygame.K_UP and \
                    self.cur_item > 0:
                self.cur_item -= 1
            elif key == pygame.K_UP and \
                    self.cur_item == 0:
                self.cur_item = len(self.items) - 1
            elif key == pygame.K_DOWN and \
                    self.cur_item < len(self.items) - 1:
                self.cur_item += 1
            elif key == pygame.K_DOWN and \
                    self.cur_item == len(self.items) - 1:
                self.cur_item = 0       
        self.items[self.cur_item].set_italic(True)
        self.items[self.cur_item].set_font_color(YELLOW)
        
        #print(self.cur_item) 
        global SelecObject
        SelecObject = self.cur_item
    
    def set_mouse_selection(self, item, mpos):
        
        """Marks the MenuItem the mouse cursor hovers on."""
        if item.is_mouse_selection(mpos):
            
            item.set_font_color(YELLOW)
            item.set_italic(True)
            global valueMouse
            valueMouse = item.text  
        else:
            item.set_font_color(WHITE)
            item.set_italic(False)
        
    
    
    def run(self):
        activeSound = True
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    mainloop = False
                    break
                elif event.type == pygame.KEYDOWN:
                    self.mouse_is_visible = False
                    self.set_item_selection(event.key)
                    if event.key == pygame.K_RETURN:
                        if settings_items[SelecObject] == 'Son':
                            if activeSound:
                                activeSound = False
                            else:
                                activeSound = True
                        elif settings_items[SelecObject] == 'Essai':
                            print()
                        elif settings_items[SelecObject] == 'Back':
                            mainloop = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if valueMouse == 'Son':
                            if activeSound:
                                activeSound = False
                            else:
                                activeSound = True
                        elif valueMouse == 'Essai':
                            print()
                        elif valueMouse == 'Back':
                            mainloop = False
                            break
                elif event.type == pygame.MOUSEMOTION:
                    if event.rel != (0, 0):
                        self.mouse_is_visible = True
                        self.cur_item = None

                    self.set_mouse_visibility()

            if not mainloop:
                break

            # Redraw the background
            screen.blit(background, (0, 0))
            
            actualHour = time.strftime('%d/%m/%y %H:%M:%S',time.localtime()) 
            letter = pygame.font.Font('Alphabet Souplings.ttf', 15)
            text = letter.render(actualHour, 1, (255, 255, 255))
            textpos = text.get_rect()
            textpos.right = screen.get_width() - 120
            textpos.top = screen.get_height()/14
            screen.blit(text, textpos)

            hand = pygame.image.load("main.png").convert_alpha()
            
            if activeSound:
                sound = pygame.image.load("sonactif.png").convert_alpha()
            else:
                sound = pygame.image.load("soninactif.png").convert_alpha()
            
                
            for item in self.items:
                if self.mouse_is_visible:
                    mpos = pygame.mouse.get_pos()
                    self.set_mouse_selection(item, mpos)
                    #print(valueMouse)
                    if valueMouse == 'Son':                       
                        position_sound = (810,120)
                        screen.blit(sound,position_sound)
                    elif valueMouse == 'Essai':
                        position_handSettings = (320,270)
                        screen.blit(hand, position_handSettings)
                    elif valueMouse == 'Back':
                        position_handQuit = (420,410)
                        screen.blit(hand, position_handQuit)		
                self.screen.blit(item.label, item.position)

            #probleme resolu
            if self.items[SelecObject].get_italic():
                if settings_items[SelecObject] == 'Son':
                    position_sound = (810,120)
                    screen.blit(sound,position_sound)
                elif settings_items[SelecObject] == 'Essai':
                    position_handSettings = (320,270)
                    screen.blit(hand, position_handSettings)
                elif settings_items[SelecObject] == 'Back':    	
                    position_handQuit = (420,410)
                    screen.blit(hand, position_handQuit)	
                    
            pygame.display.flip()


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class GameMenu():
    def __init__(self, screen, items, font='Alphabet Souplings.ttf', font_size=35,
                    font_color=WHITE):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height


        self.clock = pygame.time.Clock()
        

    
        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item, font, font_size, font_color)

            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            
            pos_y = (self.scr_height / 2) - (t_h-150) + ((index*2) + index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)

        self.mouse_is_visible = True
        self.cur_item = None

    def set_mouse_visibility(self):
        if self.mouse_is_visible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)

    def set_item_selection(self, key):
        """
        Marks the MenuItem chosen via up and down keys.
        """
        for item in self.items:
            # Return all to neutral
            item.set_italic(False)
            item.set_font_color(WHITE)

        if self.cur_item is None:
            self.cur_item = 0
        else:
            # Find the chosen item
            if key == pygame.K_UP and \
                    self.cur_item > 0:
                self.cur_item -= 1
            elif key == pygame.K_UP and \
                    self.cur_item == 0:
                self.cur_item = len(self.items) - 1
            elif key == pygame.K_DOWN and \
                    self.cur_item < len(self.items) - 1:
                self.cur_item += 1
            elif key == pygame.K_DOWN and \
                    self.cur_item == len(self.items) - 1:
                self.cur_item = 0       
        self.items[self.cur_item].set_italic(True)
        self.items[self.cur_item].set_font_color(YELLOW)
        
        #print(self.cur_item) 
        global SelecObject
        SelecObject = self.cur_item
    
    def set_mouse_selection(self, item, mpos):
        
        """Marks the MenuItem the mouse cursor hovers on."""
        if item.is_mouse_selection(mpos):
            
            item.set_font_color(YELLOW)
            item.set_italic(True)
            global valueMouse
            valueMouse = item.text  
        else:
            item.set_font_color(WHITE)
            item.set_italic(False)
        
    
    
    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                    break
                elif event.type == pygame.KEYDOWN:
                    self.mouse_is_visible = False
                    self.set_item_selection(event.key)
                    if event.key == pygame.K_RETURN:
                        if menu_items[SelecObject] == 'Play':
                            game = Game()
                        elif menu_items[SelecObject] == 'Settings':
                            global settings_items
                            settings_items = ('Son','Essai','Back')
                            settings = GameSettings(screen, settings_items)
                            settings.run()    
                        elif menu_items[SelecObject] == 'Quit':
                            mainloop = False
                            break
                    """
                    if mouse click or press enter on the quit button, the program quits
                    """
                    #print(menu_items[SelecObject])
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if valueMouse == 'Play':
                            game = Game()
                        elif valueMouse == 'Quit':
                            mainloop = False
                            break
                        elif valueMouse == 'Settings':
                            settings_items = ('Son','Essai','Back')
                            settings = GameSettings(screen, settings_items)
                            settings.run()
                elif event.type == pygame.MOUSEMOTION:
                    if event.rel != (0, 0):
                        self.mouse_is_visible = True
                        self.cur_item = None

                    self.set_mouse_visibility()

            if not mainloop:
                break

            # Redraw the background
            screen.blit(background, (0, 0))
            
            actualHour = time.strftime('%d/%m/%y %H:%M:%S',time.localtime()) 
            letter = pygame.font.Font('Alphabet Souplings.ttf', 15)
            text = letter.render(actualHour, 1, (255, 255, 255))
            textpos = text.get_rect()
            textpos.right = screen.get_width() - 120
            textpos.top = screen.get_height()/14
            screen.blit(text, textpos)

            hand = pygame.image.load("main.png").convert_alpha()
        
                
            for item in self.items:
                if self.mouse_is_visible:
                    mpos = pygame.mouse.get_pos()
                    self.set_mouse_selection(item, mpos)
                    #print(valueMouse)
                    if valueMouse == 'Play':
                        position_handPlay = (430,140)
                        screen.blit(hand, position_handPlay)
                    elif valueMouse == 'Settings':
                        position_handSettings = (320,270)
                        screen.blit(hand, position_handSettings)
                    elif valueMouse == 'Quit':
                        position_handQuit = (420,410)
                        screen.blit(hand, position_handQuit)		
                self.screen.blit(item.label, item.position)
                    
            #probleme resolu
            if self.items[SelecObject].get_italic():
                if menu_items[SelecObject] == 'Play':
                    position_perso = (430,140)
                    screen.blit(hand, position_perso)
                elif menu_items[SelecObject] == 'Settings':
                    position_handSettings = (320,270)
                    screen.blit(hand, position_handSettings)
                elif menu_items[SelecObject] == 'Quit':    	
                    position_handQuit = (420,410)
                    screen.blit(hand, position_handQuit)	
            
            pygame.display.flip()


if __name__ == "__main__":
    # Creating the screen
    screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h))
    
    global menu_items	
    menu_items = ('Play', 'Settings', 'Quit')

    pygame.display.set_caption('SiMon\'s')
    background = pygame.Surface(screen.get_size()).convert()
    background = pygame.image.load('background.jpg')
    screen.blit(background, (0, 0))
    gm = GameMenu(screen, menu_items)
    gm.run()
