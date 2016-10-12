#!/usr/bin/python
 
import time 
import pygame
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
                if event.type == pygame.KEYDOWN:
                    self.mouse_is_visible = False
                    self.set_item_selection(event.key)
 
            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_is_visible = True
                self.cur_item = None
 
            self.set_mouse_visibility()
            
            
            
 
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
                    print(valueMouse)
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
 
            """
            if mouse click or press enter on the quit button, the program quits
            """
            

            if ((event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN)) and (menu_items[SelecObject] == 'Quit' or valueMouse == 'Quit'):
            	 mainloop = False
            	 
            if ((event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN)) and (menu_items[SelecObject] == 'Play' or valueMouse == 'Play'): 
            	"""pygame.display.flip()"""
	    
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

			    
