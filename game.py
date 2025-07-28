import pygame, sys, random

def draw_floor():
    screen.blit(floor, (floor_x_pos, 600))
    screen.blit(floor, (floor_x_pos + 432, 600))
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (500, random_pipe_pos - 200)) # Khoảng trống 200px
    return bottom_pipe, top_pipe
def move_pipe(pipes):
    for pipe in pipes :
        pipe.centerx -= 5
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 768: # Nếu là ống dưới
            screen.blit(pipe_surface, pipe)
        else: # Nếu là ống trên, lật ngược ảnh rồi vẽ
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False # Va chạm với ống, game kết thúc

    if bird_rect.top <= -70 or bird_rect.bottom >= 650:
        return False # Va chạm với sàn/trần, game kết thúc
    
    return True # Nếu không có va chạm, game tiếp tục

# Đmm toàn mấy cái hàm tạo vật thể cho game ý mà

pygame.init()
screen = pygame.display.set_mode((432, 768))
clock = pygame.time.Clock()
gravity =0.65
bird_movement = 0
game_active = True
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
#pipes, hay còn gọi là ống cống
pipe_height = [300, 450, 550]

spawnpipe= pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # cái này liên quan đến việc thoaát game chim ống cống
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement = -9
            if event.key == pygame.K_SPACE and game_active == False:
                # Khởi động lại game
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 384)
                bird_movement = 0

        if event.type == spawnpipe and game_active:
            pipe_list.extend(create_pipe())

    screen.blit(bg, (0, 0))

    if game_active:
        # --- Logic khi game đang chạy ---
        # Vật lý chim
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird, bird_rect)
        game_active = check_collision(pipe_list) # Cập nhật trạng thái game

        # Vật lý ống cống
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
    else:
        # --- Logic khi game kết thúc (có thể thêm màn hình "Game Over" ở đây) ---
        pass
    
    # Vật lý của sàn (luôn chạy)
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    
    pygame.display.update()
    clock.tick(60)
