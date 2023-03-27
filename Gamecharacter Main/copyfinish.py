import pygame, sys
import time
import random
from pygame import image
from pygame import mixer
from pygame.locals import*
from tkinter import*
from tkinter import ttk
from functools import partial
from tkinter.messagebox import showinfo
##############################################################
#######################################################################3
pygame.display.set_caption('Game Map')

#test Map
class Map(): #tạo biến chung
    def __init__(self,game):
        self.game = game
        self.mid_w, self.mid_h = self.game.SCREEN_W / 2, self.game.SCREEN_H / 2
        self.offset = -100
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.bg_Map = pygame.transform.scale(pygame.image.load('choosemap.png'),(self.game.SCREEN_W,self.game.SCREEN_H))
class MainMap(Map): #tạo giao diện cho Main Map
    def __init__(self, game): #tạo biến cho Main Map
        super().__init__(game)
        self.state = "Map 1"
        self.Map1x, self.Map1y = self.mid_w, self.mid_h + 10
        self.Map2x, self.Map2y = self.mid_w, self.mid_h + 50
        self.Map3x, self.Map3y = self.mid_w, self.mid_h + 90
        self.Map4x, self.Map4y = self.mid_w, self.mid_h + 130
        self.Map5x, self.Map5y = self.mid_w, self.mid_h + 170
        self.cursor_rect.midtop = (self.Map1x + self.offset, self.Map1y)
        self.BG = self.bg_Map
        self.BG_x = 0
        self.BG_y = 0
        self.frame = pygame.transform.scale(pygame.image.load('mapchoose.png'),(625,460))
        mixer.music.load('spacerace.mp3')
        mixer.music.play(-1)  # load nhạc # vòng lặp chạy nhạc
    def displayMap(self):
        t = pygame.time.Clock()
        self.run_playing = True
        while self.run_playing: #chạy main Map
            t.tick(60)
            self.game.check_event()
            self.checkInput()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.BG,(self.BG_x,self.BG_y))
            self.BG_rel_x = self.BG_x % self.BG.get_rect().width
            self.game.display.blit(self.BG,(self.BG_rel_x - self.BG.get_rect().width,0))
            if self.BG_rel_x < 1000:
               self.game.display.blit(self.BG,(self.BG_rel_x,0))
            self.BG_x = 0
            self.game.display.blit(self.frame,(175,125))
            self.game.drawText("Version 1.0",20,500,500)
            self.game.drawText("Choose Map",50,self.mid_w, self.mid_h-30)
            self.game.drawText("Map 1",35,self.Map1x,self.Map1y)
            self.game.drawText("Map 2",35,self.Map2x,self.Map2y)
            self.game.drawText("Map 3",35,self.Map3x,self.Map3y)
            self.game.drawText("Map 4",35,self.Map4x,self.Map4y)
            self.game.drawText("Map 5",35,self.Map5x,self.Map5y)
            self.game.drawText('x', 15, self.cursor_rect.x, self.cursor_rect.y)
            self.move_Cursor_MainMap()
            self.game.window.blit(self.game.display,(0,0))
            pygame.display.update()
            self.game.resetKeys()
    def move_Cursor_MainMap(self):# tạo con trỏ để di chuyển tới các chữ Map 1, Map 2 và Map 3
        if self.game.KEY_DOWN:# giúp click chuột di chuyển xuống
            if self.state == 'Map 1':
                self.cursor_rect.midtop = (self.Map2x + self.offset, self.Map2y)
                self.state = 'Map 2'
            elif self.state == 'Map 2':
                self.cursor_rect.midtop = (self.Map3x + self.offset, self.Map3y)
                self.state = 'Map 3'
            elif self.state == 'Map 3':
                self.cursor_rect.midtop = (self.Map4x + self.offset, self.Map4y)
                self.state = 'Map 4'
            elif self.state == 'Map 4':
                self.cursor_rect.midtop = (self.Map5x + self.offset, self.Map5y)
                self.state = 'Map 5'
            elif self.state == 'Map 5':
                self.cursor_rect.midtop = (self.Map1x + self.offset, self.Map1y)
                self.state = 'Map 1'
        elif self.game.KEY_UP:#giúp con chuột di chuyển lên
            if self.state == 'Map 1':
                self.cursor_rect.midtop = (self.Map5x + self.offset, self.Map5y)
                self.state = 'Map 5'
            elif self.state == 'Map 2':
                self.cursor_rect.midtop = (self.Map1x + self.offset, self.Map1y)
                self.state = 'Map 1'
            elif self.state == 'Map 3':
                self.cursor_rect.midtop = (self.Map2x + self.offset, self.Map2y)
                self.state = 'Map 2'
            elif self.state == 'Map 4':
                self.cursor_rect.midtop = (self.Map3x + self.offset, self.Map3y)
                self.state = 'Map 3'
            elif self.state == 'Map 5':
                self.cursor_rect.midtop = (self.Map4x + self.offset, self.Map4y)
                self.state = 'Map 4'
    def checkInput(self):# giúp con chuột nhấn vào để qua giao diện mới
        if self.game.KEY_ENTER:
            if self.state == "Map 2":
               self.game.curr_Map = self.game.map2
            elif self.state == "Map 3":
                self.game.curr_Map = self.game.map3
            elif self.state == "Map 1":
                self.game.curr_Map = self.game.map1
            elif self.state == "Map 4":
                self.game.curr_Map = self.game.map4
            elif self.state == "Map 5":
                self.game.curr_Map = self.game.map5
            self.run_playing = False    
class Map1Map(Map):
    def __init__(self, game):
        Map.__init__(self,game)
        self.back = pygame.image.load('l.png')
        self.bg_Map1Map = pygame.transform.scale(pygame.image.load('choosemap.png'),(self.game.SCREEN_W,self.game.SCREEN_H))
        self.bgwooden = pygame.transform.scale(pygame.image.load('border2.png'),(800,400))
        self.BGCR = self.bg_Map1Map
        self.BGCR_x = 0
        self.BGCR_y = 0
    def displayMap(self):
        self.run_playing = True
        while self.run_playing:
            self.game.check_event()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.BGCR,(self.BGCR_x,self.BGCR_y))
            self.BGCR_rel_x = self.BGCR_x % self.BGCR.get_rect().width
            self.game.display.blit(self.BGCR,(self.BGCR_rel_x - self.BGCR.get_rect().width,0))
            if self.BGCR_rel_x < 1000:
               self.game.display.blit(self.BGCR,(self.BGCR_rel_x,0))
            self.BGCR_x -= 1
            self.game.display.blit(self.bgwooden,(90,155))
            self.createButtonBack(0,0)
            self.checkInput()
            self.game.drawText("Version 1.0",20,930,750)
            self.creditMember("CREDIT BY NHOM 7",50,self.back.get_height() + 140,0,50)
            self.creditMember("GAME DESIGNER : HO NGUYEN MINH THU",25,self.back.get_height() + 200,0,50)
            self.creditMember("GAME DESIGNER : NGUYEN TRAN TRUNG HAU",25,self.back.get_height() + 240,0,50)
            self.creditMember("GAME PROGRAMMER : THAI VAN VINH",25,self.back.get_height() + 280,0,50)
            self.creditMember("GAME PROGRAMMER : NGUYEN BAO DUY",25,self.back.get_height() + 320,0,50)
            self.creditMember("BUSINESS ANALYST : NGUYEN TRAN TRUNG HAU",25,self.back.get_height() + 360,0,50)
            self.creditMember("PROJECT MANAGER : NGUYEN VU HUNG ",25,self.back.get_height() + 400,0,50)
            self.game.window.blit(self.game.display,(0,0))
            pygame.display.update()
            self.game.resetKeys()
    def createButtonBack(self,posx,posy):
        rect = pygame.Rect(posx,posy,self.back.get_width(),self.back.get_height())
        surface_img = self.back.get_rect(center = rect.center)
        self.game.display.blit(self.back,surface_img)
        if self.game.KEY_MOUSE:
            if rect.collidepoint(pygame.mouse.get_pos()):
                self.game.back_clickSound.play()
                self.game.curr_Map = self.game.map1
                self.run_playing = False 
    def creditMember(self,text,font_size,y,w,h):
        rect = pygame.Rect(self.game.SCREEN_W/2- w/2,y,w,h)
        font = pygame.font.Font(self.game.font_name,font_size)
        font_text= font.render(text,True,(255,255,255))
        text_surface = font_text.get_rect(center = rect.center)
        pygame.draw.rect(self.game.display,(0,0,0),rect)
        self.game.display.blit(font_text,text_surface)
    def checkInput(self):# tạo con trỏ giúp thoát giao diện Credits Map
        if self.game.KEY_BACK:
            self.game.curr_Map = self.game.main_Map
        self.run_playing = False
      
class Map2Map(Map): # tạo giao diện trong Option Map
    def __init__(self, game):
        super().__init__(game)
        self.state = "Volume"
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.colx, self.coly = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly) 
        self.bg_Map2Map = pygame.transform.scale(pygame.image.load('bg3.jpg'),(self.game.SCREEN_W,self.game.SCREEN_H))
        self.BGOP = self.bg_Map2Map
        self.BGOP_x = 0
        self.BGOP_y = 0
        self.frame1 = pygame.transform.scale(pygame.image.load('frame.png'),(600,300))
    def displayMap(self): # chạy Option Map
        t = pygame.time.Clock()
        self.run_playing = True
        while self.run_playing:
            self.game.check_event()
            self.checkInput()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.BGOP,(self.BGOP_x,self.BGOP_y))
            self.BGOP_rel_x = self.BGOP_x % self.BGOP.get_rect().width
            self.game.display.blit(self.BGOP,(self.BGOP_rel_x - self.BGOP.get_rect().width,0))
            if self.BGOP_rel_x < 1000:
               self.game.display.blit(self.BGOP,(self.BGOP_rel_x,0))
            self.BGOP_x -= 1
            self.game.display.blit(self.frame1,(175,150))
            self.game.drawText("Version 1.0",20,930,750)
            self.game.drawText("Option",50,self.mid_w, self.mid_h-30)
            self.game.drawText("Volume",35,self.volx,self.voly)
            self.game.drawText("Controls",35,self.colx,self.coly)
            self.game.drawText("x",15,self.cursor_rect.x,self.cursor_rect.y)
            self.move_Cursor_Map2Map()
            self.game.window.blit(self.game.display,(0,0))
            pygame.display.update()
            self.game.resetKeys()
    def move_Cursor_Map2Map(self):# tạo con trỏ di chuyển trong giao diện Option Map
        if self.game.KEY_DOWN:
            if self.state == "Volume":
                self.cursor_rect.midtop = (self.colx + self.offset, self.coly)
                self.state = "Controls"
            elif self.state == "Controls":
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
                self.state = "Volume"
        elif self.game.KEY_UP:
            if self.state == "Volume":
                self.cursor_rect.midtop = (self.colx + self.offset, self.coly)
                self.state = "Controls"
            elif self.state == "Controls":
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
                self.state = "Volume"
    def checkInput(self):# tạo con trỏ giúp thoát giao diện Option Map
        if self.game.KEY_BACK:
            self.game.curr_Map = self.game.main_Map
        self.run_playing = False
        
        
        

class Map3Map(Map):
    def __init__(self, game):
        Map.__init__(self,game)
        self.back = pygame.image.load('l.png')
        self.bg_Map3Map = pygame.transform.scale(pygame.image.load('choosemap.png'),(self.game.SCREEN_W,self.game.SCREEN_H))
        self.bgwooden = pygame.transform.scale(pygame.image.load('border2.png'),(800,400))
        self.BGCR = self.bg_Map3Map
        self.BGCR_x = 0
        self.BGCR_y = 0
    def displayMap(self):
        self.run_playing = True
        while self.run_playing:
            self.game.check_event()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.BGCR,(self.BGCR_x,self.BGCR_y))
            self.BGCR_rel_x = self.BGCR_x % self.BGCR.get_rect().width
            self.game.display.blit(self.BGCR,(self.BGCR_rel_x - self.BGCR.get_rect().width,0))
            if self.BGCR_rel_x < 1000:
               self.game.display.blit(self.BGCR,(self.BGCR_rel_x,0))
            self.BGCR_x -= 1
            self.game.display.blit(self.bgwooden,(90,155))
            self.createButtonBack(0,0)
            self.checkInput()
            self.game.drawText("Version 1.0",20,930,750)
            self.creditMember("CREDIT BY NHOM 7",50,self.back.get_height() + 140,0,50)
            self.creditMember("GAME DESIGNER : HO NGUYEN MINH THU",25,self.back.get_height() + 200,0,50)
            self.creditMember("GAME DESIGNER : NGUYEN TRAN TRUNG HAU",25,self.back.get_height() + 240,0,50)
            self.creditMember("GAME PROGRAMMER : THAI VAN VINH",25,self.back.get_height() + 280,0,50)
            self.creditMember("GAME PROGRAMMER : NGUYEN BAO DUY",25,self.back.get_height() + 320,0,50)
            self.creditMember("BUSINESS ANALYST : NGUYEN TRAN TRUNG HAU",25,self.back.get_height() + 360,0,50)
            self.creditMember("PROJECT MANAGER : NGUYEN VU HUNG ",25,self.back.get_height() + 400,0,50)
            self.game.window.blit(self.game.display,(0,0))
            pygame.display.update()
            self.game.resetKeys()
    def createButtonBack(self,posx,posy):
        rect = pygame.Rect(posx,posy,self.back.get_width(),self.back.get_height())
        surface_img = self.back.get_rect(center = rect.center)
        self.game.display.blit(self.back,surface_img)
        if self.game.KEY_MOUSE:
            if rect.collidepoint(pygame.mouse.get_pos()):
                self.game.back_clickSound.play()
                self.game.curr_Map = self.game.map3
                self.run_playing = False 
    def creditMember(self,text,font_size,y,w,h):
        rect = pygame.Rect(self.game.SCREEN_W/2- w/2,y,w,h)
        font = pygame.font.Font(self.game.font_name,font_size)
        font_text= font.render(text,True,(255,255,255))
        text_surface = font_text.get_rect(center = rect.center)
        pygame.draw.rect(self.game.display,(0,0,0),rect)
        self.game.display.blit(font_text,text_surface)
    def checkInput(self):# tạo con trỏ giúp thoát giao diện Credits Map
        if self.game.KEY_BACK:
            self.game.curr_Map = self.game.main_Map
        self.run_playing = False
class Map4Map(Map):
    def __init__(self, game):
        Map.__init__(self,game)
        self.back = pygame.image.load('l.png')
        self.bg_Map4Map = pygame.transform.scale(pygame.image.load('choosemap.png'),(self.game.SCREEN_W,self.game.SCREEN_H))
        self.bgwooden = pygame.transform.scale(pygame.image.load('border2.png'),(800,400))
        self.BGCR = self.bg_Map4Map
        self.BGCR_x = 0
        self.BGCR_y = 0
    def displayMap(self):
        self.run_playing = True
        while self.run_playing:
            self.game.check_event()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.BGCR,(self.BGCR_x,self.BGCR_y))
            self.BGCR_rel_x = self.BGCR_x % self.BGCR.get_rect().width
            self.game.display.blit(self.BGCR,(self.BGCR_rel_x - self.BGCR.get_rect().width,0))
            if self.BGCR_rel_x < 1000:
               self.game.display.blit(self.BGCR,(self.BGCR_rel_x,0))
            self.BGCR_x -= 1
            self.game.display.blit(self.bgwooden,(90,155))
            self.createButtonBack(0,0)
            self.checkInput()
            self.game.drawText("Version 1.0",20,930,750)
            self.creditMember("CREDIT BY NHOM 7",50,self.back.get_height() + 140,0,50)
            self.creditMember("GAME DESIGNER : HO NGUYEN MINH THU",25,self.back.get_height() + 200,0,50)
            self.creditMember("GAME DESIGNER : NGUYEN TRAN TRUNG HAU",25,self.back.get_height() + 240,0,50)
            self.creditMember("GAME PROGRAMMER : THAI VAN VINH",25,self.back.get_height() + 280,0,50)
            self.creditMember("GAME PROGRAMMER : NGUYEN BAO DUY",25,self.back.get_height() + 320,0,50)
            self.creditMember("BUSINESS ANALYST : NGUYEN TRAN TRUNG HAU",25,self.back.get_height() + 360,0,50)
            self.creditMember("PROJECT MANAGER : NGUYEN VU HUNG ",25,self.back.get_height() + 400,0,50)
            self.game.window.blit(self.game.display,(0,0))
            pygame.display.update()
            self.game.resetKeys()
    def createButtonBack(self,posx,posy):
        rect = pygame.Rect(posx,posy,self.back.get_width(),self.back.get_height())
        surface_img = self.back.get_rect(center = rect.center)
        self.game.display.blit(self.back,surface_img)
        if self.game.KEY_MOUSE:
            if rect.collidepoint(pygame.mouse.get_pos()):
                self.game.back_clickSound.play()
                self.game.curr_Map = self.game.map4
                self.run_playing = False 
    def creditMember(self,text,font_size,y,w,h):
        rect = pygame.Rect(self.game.SCREEN_W/2- w/2,y,w,h)
        font = pygame.font.Font(self.game.font_name,font_size)
        font_text= font.render(text,True,(255,255,255))
        text_surface = font_text.get_rect(center = rect.center)
        pygame.draw.rect(self.game.display,(0,0,0),rect)
        self.game.display.blit(font_text,text_surface)
    def checkInput(self):# tạo con trỏ giúp thoát giao diện Credits Map
        if self.game.KEY_BACK:
            self.game.curr_Map = self.game.main_Map
        self.run_playing = False
        

class Map5Map(Map):
    def __init__(self, game):
        Map.__init__(self,game)
        self.back = pygame.image.load('l.png')
        self.bg_Map5Map = pygame.transform.scale(pygame.image.load('choosemap.png'),(self.game.SCREEN_W,self.game.SCREEN_H))
        self.bgwooden = pygame.transform.scale(pygame.image.load('border2.png'),(800,400))
        self.BGCR = self.bg_Map5Map
        self.BGCR_x = 0
        self.BGCR_y = 0
    def displayMap(self):
        self.run_playing = True
        while self.run_playing:
            self.game.check_event()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.BGCR,(self.BGCR_x,self.BGCR_y))
            self.BGCR_rel_x = self.BGCR_x % self.BGCR.get_rect().width
            self.game.display.blit(self.BGCR,(self.BGCR_rel_x - self.BGCR.get_rect().width,0))
            if self.BGCR_rel_x < 1000:
               self.game.display.blit(self.BGCR,(self.BGCR_rel_x,0))
            self.BGCR_x -= 1
            self.game.display.blit(self.bgwooden,(90,155))
            self.createButtonBack(0,0)
            self.checkInput()
            self.game.drawText("Version 1.0",20,930,750)
            self.creditMember("CREDIT BY NHOM 7",50,self.back.get_height() + 140,0,50)
            self.creditMember("GAME DESIGNER : HO NGUYEN MINH THU",25,self.back.get_height() + 200,0,50)
            self.creditMember("GAME DESIGNER : NGUYEN TRAN TRUNG HAU",25,self.back.get_height() + 240,0,50)
            self.creditMember("GAME PROGRAMMER : THAI VAN VINH",25,self.back.get_height() + 280,0,50)
            self.creditMember("GAME PROGRAMMER : NGUYEN BAO DUY",25,self.back.get_height() + 320,0,50)
            self.creditMember("BUSINESS ANALYST : NGUYEN TRAN TRUNG HAU",25,self.back.get_height() + 360,0,50)
            self.creditMember("PROJECT MANAGER : NGUYEN VU HUNG ",25,self.back.get_height() + 400,0,50)
            self.game.window.blit(self.game.display,(0,0))
            pygame.display.update()
            self.game.resetKeys()
    def createButtonBack(self,posx,posy):
        rect = pygame.Rect(posx,posy,self.back.get_width(),self.back.get_height())
        surface_img = self.back.get_rect(center = rect.center)
        self.game.display.blit(self.back,surface_img)
        if self.game.KEY_MOUSE:
            if rect.collidepoint(pygame.mouse.get_pos()):
                self.game.back_clickSound.play()
                self.game.curr_Map = self.game.map5
                self.run_playing = False 
    def creditMember(self,text,font_size,y,w,h):
        rect = pygame.Rect(self.game.SCREEN_W/2- w/2,y,w,h)
        font = pygame.font.Font(self.game.font_name,font_size)
        font_text= font.render(text,True,(255,255,255))
        text_surface = font_text.get_rect(center = rect.center)
        pygame.draw.rect(self.game.display,(0,0,0),rect)
        self.game.display.blit(font_text,text_surface)
    def checkInput(self):# tạo con trỏ giúp thoát giao diện Credits Map
        if self.game.KEY_BACK:
            self.game.curr_Map = self.game.main_Map
        self.run_playing = False

###Test again
class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.img = pygame.transform.scale(pygame.image.load('choosemap.png'),(960,540))
        self.img_x = 0
        self.img_y = 0
        self.run  = True
        self.font_name = 'Quantum.otf'
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.SCREEN_W, self.SCREEN_H = 960,540
        self.display = pygame.Surface((self.SCREEN_W,self.SCREEN_H))
        self.window = pygame.display.set_mode((self.SCREEN_W,self.SCREEN_H),RESIZABLE)
        self.main_Map = MainMap(self)
        self.map1 = Map1Map(self)
        self.map4 = Map4Map(self)
        self.map2 = Map2Map(self)
        self.map3 = Map3Map(self)
        self.map5 = Map5Map(self)
        self.curr_Map = self.main_Map
        self.KEY_DOWN = False
        self.KEY_UP = False
        self.KEY_ENTER = False
        self.KEY_BACK = False
        self.KEY_Map1 = False
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

    ##########################################################################
            
###############################################################################            
            
    def resetKeys(self):
            self.KEY_DOWN = False
            self.KEY_UP = False
            self.KEY_ENTER = False
            self.KEY_BACK = False
            self.KEY_Map1 = False
            self.KEY_MOUSE = False
        
g = Game()

while True:
    g.curr_Map.displayMap()
    #g.game_loop()
