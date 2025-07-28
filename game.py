import pygame, sys, random

def draw_floor():
    screen.blit(floor, (floor_x_pos, 600))
    screen.blit(floor, (floor_x_pos + 432, 600))
def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop = (500, 384))
    return new_pipe
def move_pipe(pipes):
    for pipes in pipes :
        pipes.centerx -=5
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)
# Đmm toàn mấy cái hàm tạo vật thể cho game ý mà

pygame.init()
screen = pygame.display.set_mode((432, 768))
clock = pygame.time.Clock()
gravity =0.25
bird_movement = 0
# Mấy dòng này để khởi tạo thôi, không cần quan tâm lắm đâu

bg = pygame.image.load('img/Copilot_20250702_223548.png').convert()
bg = pygame.transform.scale2x(bg)
# background thôi

floor = pygame.image.load('img/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
# floor ý mà

bird = pygame.image.load('img/yellowbird-midflap.png').convert()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (100,384))
#bird, hay còn gọi là chim

pipe_surface = pygame.image.load('img/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []

pipe_list = move_pipe(pipe_list)
draw_pipe(pipe_list)
#pipes, hay còn gọi là ống cống

spawnpipe= pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # cái này liên quan đến việc thoaát game chim ống cống
        
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement =-11
        # cái này để di chuyển chim

        if event.type ==spawnpipe:
            pipe_list.extend(create_pipe())
            print(create_pipe)
        # cái này giúp vẽ ra ống cống

    screen.blit(bg, (0, 0))
        # đéo biết nói gì 
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird,(bird_rect))
        # vật lý chim

    pipe_list = move_pipe(pipe_list)
    draw_pipe(pipe_list)
        #vật lý ống cống
    
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
        # vật lý của sàn
    
# vật lý của game
    pygame.display.update()
    clock.tick(60)
