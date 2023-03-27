import pygame, sys
import time
import random
from pygame.locals import *
pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
red = (255, 0, 0)
WINDOWWIDTH = 960
WINDOWHEIGHT = 540

BG = pygame.image.load('bgteam 2.png')
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
        self.surface = pygame.image.load('hung.png')
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
        self.surface1 = pygame.image.load('hung.1.png')
        self.surface2 = pygame.image.load('hung.png')
        self.surface3 = pygame.image.load('hung.1.png')
        self.speed = 0
        self.surfacelist = [self.surface1,self.surface2,self.surface3]
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
        self.surface = pygame.image.load('thu.png')
        
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
        self.surface1 = pygame.image.load('thu.1.png')
        self.surface2 = pygame.image.load('thu.png')
        self.surface3 = pygame.image.load('thu.1.png')
        self.speed = 0
        self.surfacelist = [self.surface1,self.surface2,self.surface3]
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
        self.surface = pygame.image.load('vinh.png')
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
        self.surface1 = pygame.image.load('vinh.1.png')
        self.surface2 = pygame.image.load('vinh.png')
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
        self.surface = pygame.image.load('hau.png')
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
        self.surface1 = pygame.image.load('hau.1.png')
        self.surface2 = pygame.image.load('hau.png')
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
        self.surface = pygame.image.load('duy.png')
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
        self.surface1 = pygame.image.load('duy.1.png')
        self.surface2 = pygame.image.load('duy.png')
        self.surface3 = pygame.image.load('duy.1.png')
        self.speed = 0
        self.surfacelist = [self.surface1,self.surface2,self.surface3]
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
                player1.speed = 3
                meeting_acceleration = True
                exist_acceleration[0] += 1 
            elif CollisionAcceleration(player2,acceleration ) == True:
                player2.speed = 3
                meeting_acceleration = True
                exist_acceleration[1] += 1 
            elif CollisionAcceleration(player3,acceleration ) == True:
                player3.speed = 3
                meeting_acceleration = True
                exist_acceleration[2] += 1 
            elif CollisionAcceleration(player4,acceleration ) == True:
                player4.speed = 3
                meeting_acceleration = True
                exist_acceleration[3] += 1 
            elif CollisionAcceleration(player5,acceleration ) == True:
                player5.speed = 3
                meeting_acceleration = True
                exist_acceleration[4] += 1 
            else:
                if meeting_acceleration == False: #and exist_acceleration == 1:
                    acceleration.draw(bg)
                    
        #Thời gian hiệu lực bùa
        # muốn lâu hơn thì thay đổi số 100
        if meeting_acceleration == True:
             effect_slow += 1
             if effect_slow > 75:
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
             if effect_slow > 75:
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
             if effect_pause > 75:
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
             if effect_goback > 75:
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
            if count == 750:
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
time.sleep(5)
 
pygame.quit()
quit()

