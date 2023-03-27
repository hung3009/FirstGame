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
root = Tk ()
root.geometry ("350x250")
root.title ("Login")

fo = open("data.txt", "w")
def getvals():
    print("username entered: ", username.get(),"\npassword entered: ", password.get())
    print ("SUCCESS")
    fo = open("data.txt", "w")
    fo.write("username enterred: ")
    fo.write(username.get())
    fo.write("\npassword entered: ")
    fo.write(password.get())
    fo.close()
 
#Heading
Label (root, text = "Login here ", font =("Impact", 35, "bold"),fg="#6162FF").grid(row=0,column=4)
#Field Name
username = Label(root, text = "User Name")
password = Label(root, text = "Password")

#Packing Name
username.grid(row=10, column=3)
password.grid(row=12, column=3)

# Variable for storing data
username = StringVar()
password = StringVar()

#Creating entry field
checkvalue = IntVar
nameentry = Entry(root, textvariable=username)
passentry = Entry(root, textvariable=password, show="*")


# Packing entry field
nameentry.grid (row=10, column=4)
passentry.grid (row=12, column=4)

validateLogin = partial(getvals, username, password)

#Creating check box
checkbtn = Checkbutton(text = "remember me?", variable=checkvalue)
checkbtn.grid (row=20, column=4)

#Submit button
Button (text ="Submit", command=getvals).grid(row=25,column=4)

root.mainloop()
#######################################################################3
pygame.display.set_caption('Game Menu')

#test menu
class Menu(): #tạo biến chung
    def __init__(self,game):
        self.game = game
        self.mid_w, self.mid_h = self.game.SCREEN_W / 2, self.game.SCREEN_H / 2
        self.offset = -100
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.bg_menu = pygame.transform.scale(pygame.image.load('bg3.jpg'),(self.game.SCREEN_W,self.game.SCREEN_H))
class MainMenu(Menu): #tạo giao diện cho Main Menu
    def __init__(self, game): #tạo biến cho Main Menu
        super().__init__(game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 10
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90
        self.minigamesx, self.minigamesy = self.mid_w, self.mid_h + 130
        self.historyx, self.historyy = self.mid_w, self.mid_h + 170
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        self.BG = self.bg_menu
        self.BG_x = 0
        self.BG_y = 0
        self.frame = pygame.transform.scale(pygame.image.load('frame.png'),(600,430))
        mixer.music.load('spacerace.mp3')
        mixer.music.play(-1)  # load nhạc # vòng lặp chạy nhạc
    def displayMenu(self):
        t = pygame.time.Clock()
        self.run_playing = True
        while self.run_playing: #chạy main menu
            t.tick(60)
            self.game.check_event()
            self.checkInput()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.BG,(self.BG_x,self.BG_y))
            self.BG_rel_x = self.BG_x % self.BG.get_rect().width
            self.game.display.blit(self.BG,(self.BG_rel_x - self.BG.get_rect().width,0))
            if self.BG_rel_x < 1000:
               self.game.display.blit(self.BG,(self.BG_rel_x,0))
            self.BG_x -= 1
            self.game.display.blit(self.frame,(175,125))
            self.game.drawText("Version 1.0",20,500,500)
            self.game.drawText("Racing Game",50,self.mid_w, self.mid_h-30)
            self.game.drawText("Start",35,self.startx,self.starty)
            self.game.drawText("Option",35,self.optionsx,self.optionsy)
            self.game.drawText("Credit",35,self.creditsx,self.creditsy)
            self.game.drawText("Minigame",35,self.minigamesx,self.minigamesy)
            self.game.drawText("History",35,self.historyx,self.historyy)
            self.game.drawText('x', 15, self.cursor_rect.x, self.cursor_rect.y)
            self.move_Cursor_MainMenu()
            self.game.window.blit(self.game.display,(0,0))
            pygame.display.update()
            self.game.resetKeys()
    def move_Cursor_MainMenu(self):# tạo con trỏ để di chuyển tới các chữ start, option và credit
        if self.game.KEY_DOWN:# giúp click chuột di chuyển xuống
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.minigamesx + self.offset, self.minigamesy)
                self.state = 'Minigame'
            elif self.state == 'Minigame':
                self.cursor_rect.midtop = (self.historyx + self.offset, self.historyy)
                self.state = 'History'
            elif self.state == 'History':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.KEY_UP:#giúp con chuột di chuyển lên
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.historyx + self.offset, self.historyy)
                self.state = 'History'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Minigame':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'History':
                self.cursor_rect.midtop = (self.minigamesx + self.offset, self.minigamesy)
                self.state = 'Minigame'
    def checkInput(self):# giúp con chuột nhấn vào để qua giao diện mới
        if self.game.KEY_ENTER:
            if self.state == "Options":
               self.game.curr_menu = self.game.options
            elif self.state == "Start":
                self.game.run = True
            if self.game.KEY_BACK:
                self.game.curr_menu = self.game.main_menu
            elif self.state == "Credits":
                self.game.curr_menu = self.game.credit
            self.run_playing = False
          
class OptionsMenu(Menu): # tạo giao diện trong Option Menu
    def __init__(self, game):
        super().__init__(game)
        self.state = "Volume"
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.colx, self.coly = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly) 
        self.bg_optionmenu = pygame.transform.scale(pygame.image.load('bg3.jpg'),(self.game.SCREEN_W,self.game.SCREEN_H))
        self.BGOP = self.bg_optionmenu
        self.BGOP_x = 0
        self.BGOP_y = 0
        self.frame1 = pygame.transform.scale(pygame.image.load('frame.png'),(600,300))
    def displayMenu(self): # chạy Option Menu
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
            self.move_Cursor_OptionsMenu()
            self.game.window.blit(self.game.display,(0,0))
            pygame.display.update()
            self.game.resetKeys()
    def move_Cursor_OptionsMenu(self):# tạo con trỏ di chuyển trong giao diện Option menu
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
    def checkInput(self):# tạo con trỏ giúp thoát giao diện Option Menu
        if self.game.KEY_BACK:
            self.game.curr_menu = self.game.main_menu
        self.run_playing = False
        

class CreditMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self,game)
        self.back = pygame.image.load('l.png')
        self.bg_creditmenu = pygame.transform.scale(pygame.image.load('bg3.jpg'),(self.game.SCREEN_W,self.game.SCREEN_H))
        self.bgwooden = pygame.transform.scale(pygame.image.load('border2.png'),(800,400))
        self.BGCR = self.bg_creditmenu
        self.BGCR_x = 0
        self.BGCR_y = 0
    def displayMenu(self):
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
                self.game.curr_menu = self.game.credit
                self.run_playing = False 
    def creditMember(self,text,font_size,y,w,h):
        rect = pygame.Rect(self.game.SCREEN_W/2- w/2,y,w,h)
        font = pygame.font.Font(self.game.font_name,font_size)
        font_text= font.render(text,True,(255,255,255))
        text_surface = font_text.get_rect(center = rect.center)
        pygame.draw.rect(self.game.display,(0,0,0),rect)
        self.game.display.blit(font_text,text_surface)
    def checkInput(self):# tạo con trỏ giúp thoát giao diện Credits Menu
        if self.game.KEY_BACK:
            self.game.curr_menu = self.game.main_menu
        self.run_playing = False

###Test again
class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.img = pygame.transform.scale(pygame.image.load('bg3.jpg'),(1000,800))
        self.img_x = 0
        self.img_y = 0
        self.run  = True
        self.font_name = 'Quantum.otf'
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.SCREEN_W, self.SCREEN_H = 960,540
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

    ##########################################################################
            
###############################################################################            
            
    def resetKeys(self):
            self.KEY_DOWN = False
            self.KEY_UP = False
            self.KEY_ENTER = False
            self.KEY_BACK = False
            self.KEY_START = False
            self.KEY_MOUSE = False
        
g = Game()

while True:
    g.curr_menu.displayMenu()
   # g.game_loop()
