from numpy import pi
import pygame , sys , random
#san
def draw_floor():
    screen.blit(floor,(floor_x_pos,550))
    screen.blit(floor,(floor_x_pos+432,550))
def draw_pg():
    screen.blit(bg,(bg_x_pos,0))
    screen.blit(bg,(bg_x_pos-432,0))
#ham chua ong  
def create_pipe():
    random_pipe_pos = random.choice(pipe_cao)
    bottompipe = pipe_surface.get_rect(midtop = (432,random_pipe_pos))
    toppipe = pipe_surface.get_rect(midtop = (432,random_pipe_pos - 666))
    return bottompipe,toppipe
#ham move ong
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -=2.65 #tangtocdo
    return pipes
#lui cac ong ve ban trai
def draw_pipe(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface,pipe)
#xu ly va cham
def check_collision(pipes):
    for pipe in pipes :
        if bird_rect.colliderect(pipe): 
            die_sound.play()
            return False
    if bird_rect.top <= -50 or bird_rect.bottom  >= 570:
        die_sound.play()
        return False
    else :
        return True
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1,-bird_move*5,1) #bird1,xoay theo chieu nao(- la huong xuong),scale len
    return new_bird    
        #tao hieu ung xoay
#ham dap canh
def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
    return new_bird,new_bird_rect
#ham diem
def score_display(game_state):
    #game chay chi hien diem
    if game_state == 'main game':
        score_surface = game_font.render(f'Score : {int(score)}',True,(225,225,225)) 
        #f' ' la dung hien thi van ban
        score_rect = score_surface.get_rect(center = (225,70))
        screen.blit(score_surface,score_rect)
    #game thua hien highscore
    if game_state == 'Game over':
        score_surface = game_font.render(f'Score : {int(score)}',True,(225,225,225))
        score_rect = score_surface.get_rect(center = (225,70))
        screen.blit(score_surface,score_rect)
        
        highscore_surface = game_font.render(f'HighScore : {int(high_score)}',True,(225,225,225))
        highscore_rect = highscore_surface.get_rect(center = (220,520))
        screen.blit(highscore_surface,highscore_rect)
#ham cap nhat diem 
def update_score(score,high_score):
    if score > high_score:
        high_score = score
    return high_score
        
#chinh am thanh phu hop voi pygame
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)  
pygame.init()
screen = pygame.display.set_mode((432,650))
#fps
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.TTF',40) 
#ten chu, size
score = 0
high_score = 0
#taobien
gravity = 0.09
bird_move = 0
game_active = True
#background
bg = pygame.image.load('assets/background-night.png').convert()
bg = pygame.transform.scale2x(bg)
bg_x_pos = 0
#floor
floor = pygame.image.load('assets/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
#chim
bird_up= pygame.image.load('assets/1.png').convert_alpha()
bird_down= pygame.image.load('assets/1.2.png').convert_alpha()
bird_mid = pygame.image.load('assets/1.1.png').convert_alpha()
bird_list = [bird_down,bird_mid,bird_up]
bird_index = 1# ve cai canh huong xuong, > 0 la huong len,tuong ung voi birddoown = 0, bird mid = 1,bird up = 2
bird = bird_list[bird_index]
bird_rect = bird.get_rect(center = (100,200))
#tao timer dap canh cho bird
bird_flap = pygame.USEREVENT + 1
pygame.time.set_timer(bird_flap,200)
#ống
pipe_surface= pygame.image.load('assets/pipe-green.png').convert()
pipe_surface =pygame.transform.scale2x(pipe_surface)
pipe_list = []
#tao thoi gian xuat hien ong
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 650) 
#sau 0.5 giay
pipe_cao = [180,200,220,240,260,280,290]
#gameover
gameover_surface1 = pygame.image.load('assets/message.png').convert_alpha()
gameover_rect1 = gameover_surface1.get_rect(center = (216 , 325))
gameover_surface2 = pygame.image.load('assets/gameover.png').convert_alpha()
gameover_surface2 =pygame.transform.scale2x(gameover_surface2)
gameover_rect2 = gameover_surface2.get_rect(center = (216 , 150))
#chen am thanh
flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
die_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
point_sound = pygame.mixer.Sound('sound/sfx_point.wav')
point_sound_coutdown = 100

#while loop tro choi
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active :
                bird_move = 0
                bird_move = -3.1
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False :
                game_active = True
                #reset tat ca gia tri
                pipe_list.clear()
                bird_rect.center=(100,200)
                bird_move = 0
                score = 0
        if event.type == spawnpipe :
            pipe_list.extend(create_pipe())
        if event.type == bird_flap :
            if bird_index < 2:
                bird_index += 1
            else :
                bird_index = 0
            bird,bird_rect = bird_animation()
#background         
    bg_x_pos += 1
    draw_pg()
    if bg_x_pos >= 432:
        bg_x_pos = 0
#chim
    if game_active:
        #chim rot xuong
        bird_move += gravity
        #xoay chim
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_move
        #in chim
        screen.blit(rotated_bird,bird_rect)
        #check chim
        game_active = check_collision(pipe_list)
    #ong 
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        score += 0.0095
        score_display('main game')
        point_sound_coutdown -= 1 
        if point_sound_coutdown <= 0:
            point_sound.play()
            point_sound_coutdown = 100 
    else :
        score_display('Game over')
        high_score = update_score(score,high_score)
        screen.blit(gameover_surface1,gameover_rect1)
        screen.blit(gameover_surface2,gameover_rect2)
#san
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
        
    pygame.display.update()
    clock.tick(120)