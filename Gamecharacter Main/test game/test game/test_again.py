import pygame
from pygame.locals import*
from test__menu import *
from test_again import *
from tkinter import*
from tkinter import ttk
from functools import partial
from tkinter.messagebox import showinfo

class Game():
    def __init__(self):
        pygame.init()
        self.img = pygame.transform.scale(pygame.image.load('bg3.jpg'),(1000,800))
        self.img_x = 0
        self.img_y = 0
        self.run  = True
        self.font_name = 'Quantum.otf'
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.SCREEN_W, self.SCREEN_H = 1000,800
        self.display = pygame.Surface((self.SCREEN_W,self.SCREEN_H))
        self.window = pygame.display.set_mode((self.SCREEN_W,self.SCREEN_H),RESIZABLE)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credit = CreditMenu(self)
        self.curr_menu = self.main_menu
        self.KEY_DOWN = False
        self.KEY_UP = False
        self.KEY_ENTER = False
        self.KEY_BACK = False
        self.KEY_START = False
        self.KEY_MOUSE = False
    def drawText(self,text,font_size,x,y):
        font = pygame.font.Font(self.font_name,font_size) # Create font text
        font_surface = font.render(text,True,self.WHITE)  # Create Text
        text_rect = font_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(font_surface,text_rect)
    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.KEY_UP = True
                elif event.key == pygame.K_DOWN:
                    self.KEY_DOWN = True
                elif event.key == pygame.K_RETURN:
                    self.KEY_ENTER = True
                elif event.key == pygame.K_ESCAPE:
                    self.KEY_BACK = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                    self.KEY_MOUSE = True
    def game_loop(self):
        while self.run:
            self.check_event()
            if self.KEY_BACK:
                self.run= False
            self.display.fill(self.BLACK)
            self.display.blit(self.img,(self.img_x,self.img_y))
            self.img_rel_x = self.img_x % self.img.get_rect().width
            self.display.blit(self.img,(self.img_rel_x - self.img.get_rect().width,0))
            if self.img_rel_x < 1000:
               self.display.blit(self.img,(self.img_rel_x,0))
            self.img_x -= 1
            self.drawText("Version 1.0",20,930,750)
            self.window.blit(self.display,(0,0))
            pygame.display.update()
            self.resetKeys()
    def resetKeys(self):
        self.KEY_DOWN = False
        self.KEY_UP = False
        self.KEY_ENTER = False
        self.KEY_BACK = False
        self.KEY_START = False
        self.KEY_MOUSE = False


