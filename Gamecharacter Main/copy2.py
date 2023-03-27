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
def background1():
    pygame.init()
    FPS = 60
    fpsClock = pygame.time.Clock()
    red = (255, 0, 0)
    WINDOWWIDTH = 960
    WINDOWHEIGHT = 540

    BG = pygame.image.load('bg3.png')
    BG = pygame.transform.scale(BG, (960, 540))
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('SCROLL')
    yrand =  [50, 150, 1000, 250, 1000 ,350, 1000 ,450, 1000, 1000]


    class Background(): ### vẽ background
        def __init__(self):
            
            self.x = 0
            self.y = 0
            self.img = BG
            self.width = self.img.get_width()
            self.height = self.img.get_height()
            self.speed = 4
        def draw(self): ### vẽ đè background lên nền mặc định
            DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
            DISPLAYSURF.blit(self.img, (int(self.x + self.width), int(self.y)))
        def update(self, player): ### tạo camera theo sát chuyển động của vật
        #  x_camera = player.x - (WINDOWWIDTH/2 - player.width/2)
        #  if x_camera < 0:
        #      x_camera = 0
        #  if x_camera + WINDOWWIDTH > self.width:
        #      x_camera = self.width - WINDOWWIDTH
        #  self.x = -x_camera
            self.x -= self.speed
            if self.x < -self.width:
                self.x += self.width
            
            
    class Player1():
        def __init__(self):
            self.width = 70
            self.height = 50
            self.x = 0
            self.y = 50
            #self.surface1 = pygame.image.load('7.png')
        # self.surface2 = pygame.image.load('7_1.png')
            self.speed = 1
            #self.surfacelist = [self.surface1,self.surface2]
            self.surface = pygame.image.load('7.png')
        def draw(self, bg):
            #self.surface = random.choice(self.surfacelist)
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
            #DISPLAYSURF.blit(self.surface, (int(self.x + bg.x), int(self.y + bg.y)))

        def update(self): # Hàm dùng để thay đổi vị trí xe
            self.x += self.speed
            if self.x < -self.width:
                self.x += self.width

    class Playered1():
        def __init__(self):
            self.width = 70
            self.height = 50
            self.x = 900
            self.y = 50
            self.surface1 = pygame.image.load('7.png')
            self.surface2 = pygame.image.load('7.1.png')
            self.speed = 0
            self.surfacelist = [self.surface1,self.surface2]
            self.surface = random.choice(self.surfacelist)
        def draw(self, bg):
            self.surface = random.choice(self.surfacelist)
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
            #DISPLAYSURF.blit(self.surface, (int(self.x + bg.x), int(self.y + bg.y)))
        def update(self): # Hàm dùng để thay đổi vị trí xe
            self.x += self.speed
            if self.x < -self.width:
                self.x += self.width      

    class Player2():
        def __init__(self):
            self.width = 70
            self.height = 50
            self.x = 0
            self.y = 150
            self.surface = pygame.image.load('8.png')
            
            self.speed = 1

        def draw(self, bg):
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
            #DISPLAYSURF.blit(self.surface, (int(self.x + bg.x), int(self.y + bg.y)))

        def update(self): # Hàm dùng để thay đổi vị trí xe
            self.x += self.speed
            if self.x < -self.width:
                self.x += self.width
    class Playered2():
        def __init__(self):
            self.width = 70
            self.height = 50
            self.x = 900
            self.y = 150
            self.surface1 = pygame.image.load('8.png')
            self.surface2 = pygame.image.load('8.1.png')
            self.speed = 0
            self.surfacelist = [self.surface1,self.surface2]
            self.surface = random.choice(self.surfacelist)
        def draw(self, bg):
            self.surface = random.choice(self.surfacelist)
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
            #DISPLAYSURF.blit(self.surface, (int(self.x + bg.x), int(self.y + bg.y)))
        def update(self): # Hàm dùng để thay đổi vị trí xe
            self.x += self.speed
            if self.x < -self.width:
                self.x += self.width 
    class Player3():
        def __init__(self):
            self.width = 70
            self.height = 50
            self.x = 0
            self.y = 250
            self.surface = pygame.image.load('9.png')
            self.speed = 1

        def draw(self, bg):
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
        # DISPLAYSURF.blit(self.surface, (int(self.x + bg.x), int(self.y + bg.y)))

        def update(self): # Hàm dùng để thay đổi vị trí xe
            self.x += self.speed
            if self.x < -self.width:
                self.x += self.width
    class Playered3():
        def __init__(self):
            self.width = 70
            self.height = 50
            self.x = 900
            self.y = 250
            self.surface1 = pygame.image.load('9.png')
            self.surface2 = pygame.image.load('9.1.png')
            self.speed = 0
            self.surfacelist = [self.surface1,self.surface2]
            self.surface = random.choice(self.surfacelist)
        def draw(self, bg):
            self.surface = random.choice(self.surfacelist)
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
            #DISPLAYSURF.blit(self.surface, (int(self.x + bg.x), int(self.y + bg.y)))
        def update(self): # Hàm dùng để thay đổi vị trí xe
            self.x += self.speed
            if self.x < -self.width:
                self.x += self.width
            
    class Player4():
        def __init__(self):
            self.width = 70
            self.height = 50
            self.x = 0
            self.y = 350
            self.surface = pygame.image.load('6.1.png')
            self.speed = 1

        def draw(self, bg):
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
        # DISPLAYSURF.blit(self.surface, (int(self.x + bg.x), int(self.y + bg.y)))

        def update(self): # Hàm dùng để thay đổi vị trí xe
            self.x += self.speed
            if self.x < -self.width:
                self.x += self.width
                
    class Playered4():
        def __init__(self):
            self.width = 70
            self.height = 50
            self.x = 900
            self.y = 350
            self.surface1 = pygame.image.load('6.png')
            self.surface2 = pygame.image.load('6.1.png')
            self.speed = 0
            self.surfacelist = [self.surface1,self.surface2]
            self.surface = random.choice(self.surfacelist)
        def draw(self, bg):
            self.surface = random.choice(self.surfacelist)
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
            #DISPLAYSURF.blit(self.surface, (int(self.x + bg.x), int(self.y + bg.y)))
        def update(self): # Hàm dùng để thay đổi vị trí xe
            self.x += self.speed
            if self.x < -self.width:
                self.x += self.width            
    class Player5():
        def __init__(self):
            self.width = 70
            self.height = 50
            self.x = 0
            self.y = 450
            self.surface = pygame.image.load('10.png')
            self.speed = 1

        def draw(self, bg):
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
        # DISPLAYSURF.blit(self.surface, (int(self.x + bg.x), int(self.y + bg.y)))

        def update(self): # Hàm dùng để thay đổi vị trí xe
            self.x += self.speed
            if self.x < -self.width:
                self.x += self.width

    class Playered5():
        def __init__(self):
            self.width = 70
            self.height = 50
            self.x = 900
            self.y = 450
            self.surface1 = pygame.image.load('10.png')
            self.surface2 = pygame.image.load('10.1.png')
            self.speed = 0
            self.surfacelist = [self.surface1,self.surface2]
            self.surface = random.choice(self.surfacelist)
        def draw(self, bg):
            self.surface = random.choice(self.surfacelist)
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
            #DISPLAYSURF.blit(self.surface, (int(self.x + bg.x), int(self.y + bg.y)))
        def update(self): # Hàm dùng để thay đổi vị trí xe
            self.x += self.speed
            if self.x < -self.width:
                self.x += self.width
            
    class Acceleration(): # bùa tăng tốc
        def __init__(self):
            self.width = 10
            self.height = 10
            self.x = random.randint(100,500)
            self.y = random.choice(yrand)
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill((255, 0, 255))
            self.speed = -5
            self.ls = []
        def draw(self, bg):
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
            #DISPLAYSURF.blit(self.surface, (int(self.x + bg.x), int(self.y + bg.y)))
        #def update(self): # Hàm dùng để thay đổi vị trí xe
        #   self.x += self.speed
        #   if self.x < -self.width:
        #      self.x += self.width
    def CollisionAcceleration(player,acceleration ): # va chạm bùa tăng tốc
        #player5 = Player1()
        #acceleration = Acceleration()
        rect1 = [player.x, player.y, player.x + player.width, player.y + player.height]
        rect2 = [acceleration.x, acceleration.y, acceleration.x + acceleration.width, acceleration.y + acceleration.height]
        if rect2[2] <= rect1[2] and rect1[0] <= rect2[0] and rect1[1] <= rect2[1] and rect1[3] >= rect2[3]:
            return True
        return False

    class Slowly(): # bùa chậm
        def __init__(self):
            self.width = 15
            self.height = 15
            self.x = random.randint(100,500)
            self.y = random.choice(yrand)
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill((0, 255, 0))
            self.speed = -5
            self.ls = []
        def draw(self, bg):
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
            
    def CollisionSlowly(player,slowly ): # va chạm bùa chậm
        rect1 = [player.x, player.y, player.x + player.width, player.y + player.height]
        rect2 = [slowly.x, slowly.y, slowly.x + slowly.width, slowly.y + slowly.height]
        if rect2[2] <= rect1[2] and rect1[0] <= rect2[0] and rect1[1] <= rect2[1] and rect1[3] >= rect2[3]:
            return True
        return False

    class Win(): # bùa Win
        def __init__(self):
            self.width = 15
            self.height = 15
            self.x = random.randint(100,500)
            self.y = 1000#random.choice(yrand)
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill((148, 0, 211))
            self.speed = -5
            self.ls = []
        def draw(self, bg):
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
            
    def CollisionWin(player,win): # va chạm bùa win
        rect1 = [player.x, player.y, player.x + player.width, player.y + player.height]
        rect2 = [win.x, win.y, win.x + win.width, win.y + win.height]
        if rect2[2] <= rect1[2] and rect1[0] <= rect2[0] and rect1[1] <= rect2[1] and rect1[3] >= rect2[3]:
            return True
        return False

    class Return(): # bùa Quay lại
        def __init__(self):
            self.width = 15
            self.height = 15
            self.x = random.randint(100,500)
            self.y = random.choice(yrand)
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill((0, 255, 255))
            self.speed = -5
            self.ls = []
        def draw(self, bg):
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
            
    def CollisionReturn(player,returnn): # va chạm bùa Quay lại
        rect1 = [player.x, player.y, player.x + player.width, player.y + player.height]
        rect2 = [returnn.x, returnn.y, returnn.x + returnn.width, returnn.y + returnn.height]
        if rect2[2] <= rect1[2] and rect1[0] <= rect2[0] and rect1[1] <= rect2[1] and rect1[3] >= rect2[3]:
            return True
        return False

    class Teleport(): # bùa dịch chuyển
        def __init__(self):
            self.width = 15
            self.height = 15
            self.x = random.randint(100,500)
            self.y = random.choice(yrand)
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill((160, 82, 45))
            self.speed = -5
            self.ls = []
        def draw(self, bg):
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
            
    def CollisionTeleport(player,teleport): # va chạm bùa dịch chuyển
        rect1 = [player.x, player.y, player.x + player.width, player.y + player.height]
        rect2 = [teleport.x, teleport.y, teleport.x + teleport.width, teleport.y + teleport.height]
        if rect2[2] <= rect1[2] and rect1[0] <= rect2[0] and rect1[1] <= rect2[1] and rect1[3] >= rect2[3]:
            return True
        return False

    class Pause(): # bùa dừng
        def __init__(self):
            self.width = 15
            self.height = 15
            self.x = random.randint(100,500)
            self.y = random.choice(yrand)
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill((255, 255, 0))
            self.speed = -5
            self.ls = []
        def draw(self, bg):
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
            
    def CollisionPause(player,pause): # va chạm bùa dừng
        rect1 = [player.x, player.y, player.x + player.width, player.y + player.height]
        rect2 = [pause.x, pause.y, pause.x + pause.width, pause.y + pause.height]
        if rect2[2] <= rect1[2] and rect1[0] <= rect2[0] and rect1[1] <= rect2[1] and rect1[3] >= rect2[3]:
            return True
        return False



    class Goback(): # bùa đi ngược
        def __init__(self):
            self.width = 15
            self.height = 15
            self.x = random.randint(100,500)
            self.y = random.choice(yrand)
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill((0, 0, 0))
            self.speed = -5
            self.ls = []
        def draw(self, bg):
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))
            
    def CollisionGoback(player,goback): # va chạm đi ngược
        rect1 = [player.x, player.y, player.x + player.width, player.y + player.height]
        rect2 = [goback.x, goback.y, goback.x + goback.width, goback.y + goback.height]
        if rect2[2] <= rect1[2] and rect1[0] <= rect2[0] and rect1[1] <= rect2[1] and rect1[3] >= rect2[3]:
            return True
        return False

    class Finish(): 
        def __init__(self):
            self.width = 30
            self.height = 600
            self.x = 900
            self.y = 0
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill((255, 255, 255))
            #self.surface = pygame.image.load('flag.png')
            self.ls = []
        def draw(self, bg):
            DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y )))

    def CollisionFinish(player,finish): # va chạm đi ngược
        rect1 = [player.x, player.y, player.x + player.width, player.y + player.height]
        rect2 = [finish.x, finish.y, finish.x + finish.width, finish.y + finish.height]
        if player.x == finish.x :
            return True
        return False

    def main():
        bg = Background()
        player1 = Player1()
        playered1 = Playered1()
        
        player2 = Player2()
        playered2 = Playered2()
        
        player3 = Player3()
        playered3 = Playered3()
        
        player4 = Player4()
        playered4 = Playered4()
        
        player5 = Player5()
        playered5 = Playered5()
        
        acceleration = Acceleration()
        yrand.remove(acceleration.y)
        slowly = Slowly()
        yrand.remove(slowly.y)
        teleport = Teleport()
        yrand.remove(teleport.y)
        pause = Pause()
        yrand.remove(pause.y)
        goback = Goback()
        yrand.remove(goback.y)
        returnn = Return()
        yrand.remove(returnn.y)
        win = Win()
        finish = Finish()
        
        exist_return = [0, 0, 0, 0, 0]
        exist_slow = [0, 0, 0, 0, 0]
        exist_acceleration = [0, 0, 0, 0, 0]
        exist_win = [0, 0, 0, 0, 0]
        exist_teleport = [0, 0, 0, 0, 0]
        exist_pause = [0, 0, 0, 0, 0]
        exist_goback = [0, 0, 0, 0, 0]
        meeting_finish = [0, 0, 0, 0, 0]
        
        meeting_return = 0
        meeting_slow = 0
        meeting_acceleration = 0
        meeting_win = 0
        meeting_teleport = 0
        meeting_pause = 0
        meeting_goback = 0
        
        effect_slow = 0
        effect_acceleration = 0
        effect_win = 0
        effect_teleport = 0
        effect_return = 0
        effect_pause = 0
        effect_goback = 0
        count = 0

        winner = 0
        
        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            bg.draw()
            
            if meeting_finish[0] != 1:
                player1.draw(bg)
            else:
                playered1.draw(bg)
                
            if meeting_finish[1] != 1:
                player2.draw(bg)
            else:
                playered2.draw(bg)
            
            if meeting_finish[2] != 1:
                player3.draw(bg)
            else:
                playered3.draw(bg)
            
            if meeting_finish[3] != 1:
                player4.draw(bg)
            else:
                playered4.draw(bg)
            
            if meeting_finish[4] != 1:
                player5.draw(bg)
            else:
                playered5.draw(bg)

            
            finish.draw(bg)
            # Hiệu ứng bùa tăng tốc( muốn tốc độ nhanh bao nhiu thì đổi lại số 3)
            # Bùa hồng đậm là bùa nhanh
            if meeting_acceleration == False:
                if CollisionAcceleration(player1,acceleration ) == True:
                    player1.speed = 2
                    meeting_acceleration = True
                    exist_acceleration[0] += 1 
                elif CollisionAcceleration(player2,acceleration ) == True:
                    player2.speed = 2
                    meeting_acceleration = True
                    exist_acceleration[1] += 1 
                elif CollisionAcceleration(player3,acceleration ) == True:
                    player3.speed = 2
                    meeting_acceleration = True
                    exist_acceleration[2] += 1 
                elif CollisionAcceleration(player4,acceleration ) == True:
                    player4.speed = 2
                    meeting_acceleration = True
                    exist_acceleration[3] += 1 
                elif CollisionAcceleration(player5,acceleration ) == True:
                    player5.speed = 2
                    meeting_acceleration = True
                    exist_acceleration[4] += 1 
                else:
                    if meeting_acceleration == False: #and exist_acceleration == 1:
                        acceleration.draw(bg)
                        
            #Thời gian hiệu lực bùa
            # muốn lâu hơn thì thay đổi số 100
            if meeting_acceleration == True:
                effect_slow += 1
                if effect_slow == 75:
                    if exist_acceleration[0] == 1: 
                        player1.speed = 1
                    elif exist_acceleration[1] == 1:
                        player2.speed = 1
                    elif exist_acceleration[2] == 1:
                        player3.speed = 1
                    elif exist_acceleration[3] == 1:   
                        player4.speed = 1
                    elif exist_acceleration[4] == 1:  
                        player5.speed = 1
            
                    
            # Hiệu ứng bùa chậm(muốn chậm hơn thì đổi lại số 0.005)
            # Bùa xanh là Bùa chậm
            if meeting_slow == False:
                if CollisionSlowly(player1,slowly) == True:
                    player1.speed = 0.5
                    meeting_slow = True
                    exist_slow[0] += 1
                elif CollisionSlowly(player2,slowly) == True:
                    player2.speed = 0.5
                    meeting_slow = True
                    exist_slow[1] += 1
                elif CollisionSlowly(player3,slowly) == True:
                    player3.speed = 0.5
                    meeting_slow = True
                    exist_slow[2] += 1
                elif CollisionSlowly(player4,slowly) == True:
                    player4.speed = 0.5
                    meeting_slow = True
                    exist_slow[3] += 1
                elif CollisionSlowly(player5,slowly) == True:
                    player5.speed = 0.5
                    meeting_slow = True
                    exist_slow[4] += 1
                else:
                    if meeting_slow == False: #and exist_slow == 1:
                        slowly.draw(bg)
            # thời gian hiệu lực bùa
            # mún lâu hơn thiwf thay đồi số 100
            if meeting_slow == True:
                effect_slow += 1
                if effect_slow == 75:
                    if exist_slow[0] == 1: 
                        player1.speed = 1
                    elif exist_slow[1] == 1:
                        player2.speed = 1
                    elif exist_slow[2] == 1:
                        player3.speed = 1
                    elif exist_slow[3] == 1:   
                        player4.speed = 1
                    elif exist_slow[4] == 1:  
                        player5.speed = 1
            

            # Hiệu ứng bùa Win
            # Bùa tím là Bùa Win
            if meeting_win == False:
                if CollisionWin(player1,win) == True:
                    player1.x = 960
                    meeting_win = True
                
                elif CollisionWin(player2,win) == True:
                    player2.x = 960
                    meeting_win = True
                
                elif CollisionWin(player3,win) == True:
                    player3.x = 960
                    meeting_win = True
                    
                elif CollisionWin(player4,win) == True:
                    player4.x = 960
                    meeting_win = True
                    
                elif CollisionWin(player5,win) == True:
                    player5.x = 960
                    meeting_win = True
                
                else:
                    if meeting_win == False: #and exist_win == 1:
                        win.draw(bg)

        
            # Hiệu ứng bùa quay lại
            # Bùa xanh sáng là Bùa quay lại
            if meeting_return == False:
                if CollisionReturn(player1,returnn) == True:
                    player1.x = 0
                    meeting_return = True
                    #yrand.remove(returnn.y)
                elif CollisionReturn(player2,returnn) == True:
                    player2.x = 0
                    meeting_return = True
                    #yrand.remove(returnn.y)
                elif CollisionReturn(player3,returnn) == True:
                    player3.x = 0
                    meeting_return = True
                    #yrand.remove(returnn.y)
                elif CollisionReturn(player4,returnn) == True:
                    player4.x = 0
                    meeting_return = True
                    #yrand.remove(returnn.y)
                elif CollisionReturn(player5,returnn) == True:
                    player5.x = 0
                    meeting_return = True
                    #yrand.remove(returnn.y)
                else:
                    if meeting_return == False: # and exist_return == 1:
                        returnn.draw(bg)
        
                # Hiệu ứng bùa dịch chuyển
                # Bùa màu nâu là Bùa dịch chuyển
                # Muốn thay đổi tọa độ dịch chuyển thì thay đôi số 100
            if CollisionTeleport(player1,teleport) == True:
                player1.x += 100
                meeting_teleport = True
                #yrand.remove(teleport.y)
            elif CollisionTeleport(player2,teleport) == True:
                player2.x += 100
                meeting_teleport = True
                #yrand.remove(teleport.y)
            elif CollisionTeleport(player3,teleport) == True:
                player3.x += 100
                meeting_teleport = True
                #yrand.remove(teleport.y)
            elif CollisionTeleport(player4,teleport) == True:
                player4.x += 100
                meeting_teleport = True
                #yrand.remove(teleport.y)
            elif CollisionTeleport(player5,teleport) == True:
                player5.x += 100
                meeting_teleport = True
                #yrand.remove(teleport.y)
            else:
                if meeting_teleport == False: #and exist_teleport == 1:
                        teleport.draw(bg)
                        
        
            # Hiệu ứng bùa đi đứng im
            # màu vàng là bùa đứng im
            if meeting_pause == False:
                if CollisionPause(player1,pause) == True:
                    player1.speed = 0 
                    meeting_pause = True
                    exist_pause[0] += 1 
                elif CollisionPause(player2,pause) == True:
                    player2.speed = 0
                    meeting_pause = True
                    exist_pause[1] += 1   
                elif CollisionPause(player3,pause) == True:
                    player3.speed = 0
                    meeting_pause = True
                    exist_pause[2] += 1
                elif CollisionPause(player4,pause) == True:
                    player4.speed = 0
                    meeting_pause = True
                    exist_pause[3] += 1
                elif CollisionPause(player5,pause) == True:
                    player5.speed = 0
                    meeting_pause = True
                    exist_pause[4] += 1
                else:
                    if meeting_pause == False: # exist_pause == 1:
                        pause.draw(bg)
            # thời gian hiệu lực bùa đứng im
            # muốn lâu hơn thì thay đôi số 75
            if meeting_pause == True:
                effect_pause += 1
                if effect_pause == 75:
                    if exist_pause[0] == 1: 
                        player1.speed = 1
                    elif exist_pause[1] == 1:
                        player2.speed = 1
                    elif exist_pause[2] == 1:
                        player3.speed = 1
                    elif exist_pause[3] == 1:   
                        player4.speed = 1
                    elif exist_pause[4] == 1:  
                        player5.speed = 1
                
            # Hiệu ứng bùa đi ngược
            # màu đen là buà đi ngược
            if meeting_goback == False:
                if CollisionGoback(player1,goback) == True:
                    player1.speed = -1 
                    meeting_goback = True
                    exist_goback[0] += 1
                elif CollisionGoback(player2,goback) == True:
                    player2.speed = -1 
                    meeting_goback = True
                    exist_goback[1] += 1
                elif CollisionGoback(player3,goback) == True:
                    player3.speed = -1 
                    meeting_goback = True
                    exist_goback[2] += 1
                elif CollisionGoback(player4,goback) == True:
                    player4.speed = -1 
                    meeting_goback = True
                    exist_goback[3] += 1
                elif CollisionGoback(player5,goback) == True:
                    player5.speed = -1 
                    meeting_goback = True
                    exist_goback[4] += 1
                else:
                    if meeting_goback == False: #and exist_goback == 1:
                        goback.draw(bg)
            # thời gian hiệu lực bùa đi ngược
            # muốn lâu hơn thì thay đôi số 75
            if meeting_goback == True:
                effect_goback += 1
                if effect_goback == 75:
                    if exist_goback[0] == 1: 
                        player1.speed = 1
                    elif exist_goback[1] == 1:
                        player2.speed = 1
                    elif exist_goback[2] == 1:
                        player3.speed = 1
                    elif exist_goback[3] == 1:   
                        player4.speed = 1
                    elif exist_goback[4] == 1:  
                        player5.speed = 1
                        
            if CollisionFinish(player1,finish) == True:
                    player1.speed = 0
                    meeting_finish[0] = 1
            
            if CollisionFinish(player2,finish) == True:
                    player2.speed = 0
                    meeting_finish[1] = 1
            
            if CollisionFinish(player3,finish) == True:
                    player3.speed = 0
                    meeting_finish[2] = 1
            
            if CollisionFinish(player4,finish) == True:
                    player4.speed = 0
                    meeting_finish[3] = 1
        
            if CollisionFinish(player5,finish) == True:
                    player5.speed = 0
                    meeting_finish[4] = 1

            if meeting_finish[0] == 1 and meeting_finish[1] == 1 and meeting_finish[2] == 1 and meeting_finish[3] == 1 and meeting_finish[4] == 1:
                count = count + 1
                if count == 100:
                    game_over = True
                
                
            player1.update()
            player2.update()
            player3.update() 
            player4.update()
            player5.update()
            
            bg.update(player1)
        
            
            pygame.display.update()
            fpsClock.tick(FPS)
            
            

    if __name__ == '__main__':
        main()

    font_style = pygame.font.SysFont(None, 50)
    def message(msg,color):
        mesg = font_style.render(msg, True, color)
        DISPLAYSURF.blit(mesg, [WINDOWWIDTH/2, WINDOWHEIGHT/2])
        
    message("Game Over",red)
    pygame.display.update()
    time.sleep(1)
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
                            if self.state == "Map 1":
                                self.game.run = True
                                pygame.display.set_caption('Game Character')

                                #test Character
                                class Character(): #tạo biến chung
                                    def __init__(self,game):
                                        self.game = game
                                        self.mid_w, self.mid_h = self.game.SCREEN_W / 2, self.game.SCREEN_H / 2
                                        self.offset = -100
                                        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
                                        self.bg_Character = pygame.transform.scale(pygame.image.load('chooseCharacter.jpg'),(self.game.SCREEN_W,self.game.SCREEN_H))
                                class MainCharacter(Character): #tạo giao diện cho Main Character
                                    def __init__(self, game): #tạo biến cho Main Character
                                        super().__init__(game)
                                        self.state = "Character 1"
                                        self.Character1x, self.Character1y = self.mid_w, self.mid_h + 10
                                        self.Character2x, self.Character2y = self.mid_w, self.mid_h + 50
                                        self.Character3x, self.Character3y = self.mid_w, self.mid_h + 90
                                        self.Character4x, self.Character4y = self.mid_w, self.mid_h + 130
                                        self.Character5x, self.Character5y = self.mid_w, self.mid_h + 170
                                        self.cursor_rect.midtop = (self.Character1x + self.offset, self.Character1y)
                                        self.BG = self.bg_Character
                                        self.BG_x = 0
                                        self.BG_y = 0
                                        self.frame = pygame.transform.scale(pygame.image.load('mapchoose.png'),(625,460))
                                        mixer.music.load('spacerace.mp3')
                                        mixer.music.play(-1)  # load nhạc # vòng lặp chạy nhạc
                                    def displayCharacter(self):
                                        t = pygame.time.Clock()
                                        self.run_playing = True
                                        while self.run_playing: #chạy main Character
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
                                            self.game.drawText("Choose Character",50,self.mid_w, self.mid_h-30)
                                            self.game.drawText("Character 1",35,self.Character1x,self.Character1y)
                                            self.game.drawText("Character 2",35,self.Character2x,self.Character2y)
                                            self.game.drawText("Character 3",35,self.Character3x,self.Character3y)
                                            self.game.drawText("Character 4",35,self.Character4x,self.Character4y)
                                            self.game.drawText("Character 5",35,self.Character5x,self.Character5y)
                                            self.game.drawText('x', 15, self.cursor_rect.x, self.cursor_rect.y)
                                            self.move_Cursor_MainCharacter()
                                            self.game.window.blit(self.game.display,(0,0))
                                            pygame.display.update()
                                            self.game.resetKeys()
                                    def move_Cursor_MainCharacter(self):# tạo con trỏ để di chuyển tới các chữ Character 1, Character 2 và Character 3
                                        if self.game.KEY_DOWN:# giúp click chuột di chuyển xuống
                                            if self.state == 'Character 1':
                                                self.cursor_rect.midtop = (self.Character2x + self.offset, self.Character2y)
                                                self.state = 'Character 2'
                                            elif self.state == 'Character 2':
                                                self.cursor_rect.midtop = (self.Character3x + self.offset, self.Character3y)
                                                self.state = 'Character 3'
                                            elif self.state == 'Character 3':
                                                self.cursor_rect.midtop = (self.Character4x + self.offset, self.Character4y)
                                                self.state = 'Character 4'
                                            elif self.state == 'Character 4':
                                                self.cursor_rect.midtop = (self.Character5x + self.offset, self.Character5y)
                                                self.state = 'Character 5'
                                            elif self.state == 'Character 5':
                                                self.cursor_rect.midtop = (self.Character1x + self.offset, self.Character1y)
                                                self.state = 'Character 1'
                                        elif self.game.KEY_UP:#giúp con chuột di chuyển lên
                                            if self.state == 'Character 1':
                                                self.cursor_rect.midtop = (self.Character5x + self.offset, self.Character5y)
                                                self.state = 'Character 5'
                                            elif self.state == 'Character 2':
                                                self.cursor_rect.midtop = (self.Character1x + self.offset, self.Character1y)
                                                self.state = 'Character 1'
                                            elif self.state == 'Character 3':
                                                self.cursor_rect.midtop = (self.Character2x + self.offset, self.Character2y)
                                                self.state = 'Character 2'
                                            elif self.state == 'Character 4':
                                                self.cursor_rect.midtop = (self.Character3x + self.offset, self.Character3y)
                                                self.state = 'Character 3'
                                            elif self.state == 'Character 5':
                                                self.cursor_rect.midtop = (self.Character4x + self.offset, self.Character4y)
                                                self.state = 'Character 4'
                                    def checkInput(self):# giúp con chuột nhấn vào để qua giao diện mới
                                        if self.game.KEY_ENTER:
                                            if self.state == "Character 1":
                                                self.game.run = True
                                                background1()
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
                                                def checkInput(self):# tạo con trỏ giúp thoát giao diện Option Menu
                                                    if self.game.KEY_BACK:
                                                        self.game.curr_menu = self.game.main_menu
                                                    self.run_playing = False
        
                                                
                                            elif self.state == "Character 2":
                                                self.game.curr_Character = self.game.Character2
                                            elif self.state == "Character 3":
                                                self.game.curr_Character = self.game.Character3   
                                            elif self.state == "Character 4":
                                                self.game.curr_Character = self.game.Character4
                                            elif self.state == "Character 5":
                                                self.game.curr_Character = self.game.Character5
                                            self.run_playing = False      
                                class Character1Character(Character):
                                    def __init__(self, game):
                                        Character.__init__(self,game)
                                        self.back = pygame.image.load('l.png')
                                        self.bg_Character1Character = pygame.transform.scale(pygame.image.load('chooseCharacter.png'),(self.game.SCREEN_W,self.game.SCREEN_H))
                                        self.bgwooden = pygame.transform.scale(pygame.image.load('border2.png'),(800,400))
                                        self.BGCR = self.bg_Character1Character
                                        self.BGCR_x = 0
                                        self.BGCR_y = 0
                                    def displayCharacter(self):
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
                                                self.game.curr_Character = self.game.Character1
                                                self.run_playing = False 
                                    def creditMember(self,text,font_size,y,w,h):
                                        rect = pygame.Rect(self.game.SCREEN_W/2- w/2,y,w,h)
                                        font = pygame.font.Font(self.game.font_name,font_size)
                                        font_text= font.render(text,True,(255,255,255))
                                        text_surface = font_text.get_rect(center = rect.center)
                                        pygame.draw.rect(self.game.display,(0,0,0),rect)
                                        self.game.display.blit(font_text,text_surface)
                                    def checkInput(self):# tạo con trỏ giúp thoát giao diện Credits Character
                                        if self.game.KEY_BACK:
                                            self.game.curr_Character = self.game.main_Character
                                        self.run_playing = False
                                        
                                class Character2Character(Character):
                                    def __init__(self, game):
                                        Character.__init__(self,game)
                                        self.back = pygame.image.load('l.png')
                                        self.bg_Character2Character = pygame.transform.scale(pygame.image.load('chooseCharacter.jpg'),(self.game.SCREEN_W,self.game.SCREEN_H))
                                        self.bgwooden = pygame.transform.scale(pygame.image.load('border2.png'),(800,400))
                                        self.BGCR = self.bg_Character2Character
                                        self.BGCR_x = 0
                                        self.BGCR_y = 0
                                    def displayCharacter(self):
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
                                                self.game.curr_Character = self.game.Character2
                                                self.run_playing = False 
                                    def creditMember(self,text,font_size,y,w,h):
                                        rect = pygame.Rect(self.game.SCREEN_W/2- w/2,y,w,h)
                                        font = pygame.font.Font(self.game.font_name,font_size)
                                        font_text= font.render(text,True,(255,255,255))
                                        text_surface = font_text.get_rect(center = rect.center)
                                        pygame.draw.rect(self.game.display,(0,0,0),rect)
                                        self.game.display.blit(font_text,text_surface)
                                    def checkInput(self):# tạo con trỏ giúp thoát giao diện Credits Character
                                        if self.game.KEY_BACK:
                                            self.game.curr_Character = self.game.main_Character
                                        self.run_playing = False
                                        

                                class Character3Character(Character):
                                    def __init__(self, game):
                                        Character.__init__(self,game)
                                        self.back = pygame.image.load('l.png')
                                        self.bg_Character3Character = pygame.transform.scale(pygame.image.load('chooseCharacter.jpg'),(self.game.SCREEN_W,self.game.SCREEN_H))
                                        self.bgwooden = pygame.transform.scale(pygame.image.load('border2.png'),(800,400))
                                        self.BGCR = self.bg_Character3Character
                                        self.BGCR_x = 0
                                        self.BGCR_y = 0
                                    def displayCharacter(self):
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
                                                self.game.curr_Character = self.game.Character3
                                                self.run_playing = False 
                                    def creditMember(self,text,font_size,y,w,h):
                                        rect = pygame.Rect(self.game.SCREEN_W/2- w/2,y,w,h)
                                        font = pygame.font.Font(self.game.font_name,font_size)
                                        font_text= font.render(text,True,(255,255,255))
                                        text_surface = font_text.get_rect(center = rect.center)
                                        pygame.draw.rect(self.game.display,(0,0,0),rect)
                                        self.game.display.blit(font_text,text_surface)
                                    def checkInput(self):# tạo con trỏ giúp thoát giao diện Credits Character
                                        if self.game.KEY_BACK:
                                            self.game.curr_Character = self.game.main_Character
                                        self.run_playing = False
                                class Character4Character(Character):
                                    def __init__(self, game):
                                        Character.__init__(self,game)
                                        self.back = pygame.image.load('l.png')
                                        self.bg_Character4Character = pygame.transform.scale(pygame.image.load('chooseCharacter.jpg'),(self.game.SCREEN_W,self.game.SCREEN_H))
                                        self.bgwooden = pygame.transform.scale(pygame.image.load('border2.png'),(800,400))
                                        self.BGCR = self.bg_Character4Character
                                        self.BGCR_x = 0
                                        self.BGCR_y = 0
                                    def displayCharacter(self):
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
                                                self.game.curr_Character = self.game.Character4
                                                self.run_playing = False 
                                    def creditMember(self,text,font_size,y,w,h):
                                        rect = pygame.Rect(self.game.SCREEN_W/2- w/2,y,w,h)
                                        font = pygame.font.Font(self.game.font_name,font_size)
                                        font_text= font.render(text,True,(255,255,255))
                                        text_surface = font_text.get_rect(center = rect.center)
                                        pygame.draw.rect(self.game.display,(0,0,0),rect)
                                        self.game.display.blit(font_text,text_surface)
                                    def checkInput(self):# tạo con trỏ giúp thoát giao diện Credits Character
                                        if self.game.KEY_BACK:
                                            self.game.curr_Character = self.game.main_Character
                                        self.run_playing = False
                                        

                                class Character5Character(Character):
                                    def __init__(self, game):
                                        Character.__init__(self,game)
                                        self.back = pygame.image.load('l.png')
                                        self.bg_Character5Character = pygame.transform.scale(pygame.image.load('chooseCharacter.jpg'),(self.game.SCREEN_W,self.game.SCREEN_H))
                                        self.bgwooden = pygame.transform.scale(pygame.image.load('border2.png'),(800,400))
                                        self.BGCR = self.bg_Character5Character
                                        self.BGCR_x = 0
                                        self.BGCR_y = 0
                                    def displayCharacter(self):
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
                                                self.game.curr_Character = self.game.Character5
                                                self.run_playing = False 
                                    def creditMember(self,text,font_size,y,w,h):
                                        rect = pygame.Rect(self.game.SCREEN_W/2- w/2,y,w,h)
                                        font = pygame.font.Font(self.game.font_name,font_size)
                                        font_text= font.render(text,True,(255,255,255))
                                        text_surface = font_text.get_rect(center = rect.center)
                                        pygame.draw.rect(self.game.display,(0,0,0),rect)
                                        self.game.display.blit(font_text,text_surface)
                                    def checkInput(self):# tạo con trỏ giúp thoát giao diện Credits Character
                                        if self.game.KEY_BACK:
                                            self.game.curr_Character = self.game.main_Character
                                        self.run_playing = False

                                ###Test again
                                class Game():
                                    def __init__(self):
                                        pygame.init()
                                        pygame.font.init()
                                        self.img = pygame.transform.scale(pygame.image.load('chooseCharacter.jpg'),(960,540))
                                        self.img_x = 0
                                        self.img_y = 0
                                        self.run  = True
                                        self.font_name = 'Quantum.otf'
                                        self.WHITE = (255,255,255)
                                        self.BLACK = (0,0,0)
                                        self.SCREEN_W, self.SCREEN_H = 960,540
                                        self.display = pygame.Surface((self.SCREEN_W,self.SCREEN_H))
                                        self.window = pygame.display.set_mode((self.SCREEN_W,self.SCREEN_H),RESIZABLE)
                                        self.main_Character = MainCharacter(self)
                                        self.Character2 = Character2Character(self)
                                        self.Character3 = Character3Character(self)
                                        self.curr_Character = self.main_Character
                                        self.KEY_DOWN = False
                                        self.KEY_UP = False
                                        self.KEY_ENTER = False
                                        self.KEY_BACK = False
                                        self.KEY_Character1 = False
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
                                            self.KEY_Character1 = False
                                            self.KEY_MOUSE = False
                                        
                                g = Game()

                                while True:
                                    g.curr_Character.displayCharacter()
                                # g.game_loop()
                            elif self.state == "Map 2":
                                self.game.curr_Map = self.game.map2
                            elif self.state == "Map 3":
                                self.game.curr_Map = self.game.map3   
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
                        
                class Map2Map(Map):
                    def __init__(self, game):
                        Map.__init__(self,game)
                        self.back = pygame.image.load('l.png')
                        self.bg_Map2Map = pygame.transform.scale(pygame.image.load('choosemap.png'),(self.game.SCREEN_W,self.game.SCREEN_H))
                        self.bgwooden = pygame.transform.scale(pygame.image.load('border2.png'),(800,400))
                        self.BGCR = self.bg_Map2Map
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
                                self.game.curr_Map = self.game.map2
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
                        self.map2 = Map2Map(self)
                        self.map3 = Map3Map(self)
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
                    g.game_loop()
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
