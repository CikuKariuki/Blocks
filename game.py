import pygame
import sys
import random

pygame.init()

WIDTH = 500
HEIGHT = 500

PINK = (255,0,125)
BLUE = (125,0,200)
BACKGROUND_COLOR = (0,0,0)

player_size = 50
player_pos = [WIDTH/2,HEIGHT-1.5*player_size]

enemy_size = 40
enemy_pos = [random.randint(0,WIDTH - enemy_size),0]
SPEED = 10

screen = pygame.display.set_mode((WIDTH,HEIGHT))

game_over = False

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size

            player_pos=[x,y]

    screen.fill(BACKGROUND_COLOR)
# position of the enemy
    if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
        enemy_pos[1] += SPEED
    else:
        enemy_pos[0] = random.randint(0,WIDTH-enemy_size)
        enemy_pos[1] = 0

    pygame.draw.rect(screen, BLUE, (enemy_pos[0],enemy_pos[1], enemy_size,enemy_size))
    pygame.draw.rect(screen, PINK, (player_pos[0], player_pos[1],player_size,player_size))

    clock.tick(30)

    pygame.display.update()

    
    
