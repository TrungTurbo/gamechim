import pygame, sys
def draw_floor():
    screen.blit(floor, (floor_x_pos, 600))
    screen.blit(floor, (floor_x_pos + 432, 600))

pygame.init()
screen = pygame.display.set_mode((432, 768))
clock = pygame.time.Clock()
#
bg = pygame.image.load('img/Copilot_20250702_223548.png')
bg = pygame.transform.scale2x(bg)

floor = pygame.image.load('img/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0

# Make sure you have a 'bird.png' file in your 'img' folder
bird = pygame.image.load('img/bird.png').convert_alpha()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (100, 384))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 8
        if event.type == pygame.MOUSEBUTTONDOWN:
            bird_movement = 0
            bird_movement -= 8

    screen.blit(bg, (0, 0))

    # Bird physics
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird, bird_rect)

    # Floor movement
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(60)
