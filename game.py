import pygame
import sys
import random

pygame.init()

WIDTH = 500
HEIGHT = 500

PINK = (255,0,125)
BLUE = (125,0,200)
BACKGROUND_COLOR = (0,0,0)

player_size = 20
player_pos = [WIDTH/2,HEIGHT-1.5*player_size]

enemy_size = 40
enemy_pos = [random.randint(0,WIDTH - enemy_size),0]
enemy_list = [enemy_pos]

SPEED = 10

screen = pygame.display.set_mode((WIDTH,HEIGHT))

game_over = False

score = 0

myFont = pygame.font.SysFont("monospace", 35)

clock = pygame.time.Clock()

def set_level(score, SPEED):
    # if score < 10:
    #     SPEED = 5
    # elif score > 10 and score < 20:
    #     SPEED = 6
    # elif score > 20 and score < 30:
    #     SPEED = 7
    # elif score > 30 and score < 40:
    #     SPEED = 11

    # else:
    #     SPEED = 13
    SPEED = score/5 + 4
    return SPEED

def drop_enemies(enemy_list):
    delay = random.random() 
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0,WIDTH-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos,y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos[0],enemy_pos[1], enemy_size,enemy_size))

def update_enemy_position(enemy_list,score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    return score


def detect_collision(player_pos,enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x+player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

def collision_check(enemy_list,player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos,player_pos):
            return True
    return False
# end of functions

# beginning of loop

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

    if detect_collision(player_pos,enemy_pos):
        game_over = True
        break
        

    drop_enemies(enemy_list)
    # updating the score
    score = update_enemy_position(enemy_list,score)

    # changing levels
    SPEED = set_level(score,SPEED)

    # displaying the score
    text = "Score:" + str(score)
    label = myFont.render(text,1,(255,255,0))
    screen.blit(label, (WIDTH-200, HEIGHT-40))


    if collision_check(enemy_list,player_pos):
        game_over = True
        break
    draw_enemies(enemy_list)
    
    pygame.draw.rect(screen, PINK, (player_pos[0], player_pos[1],player_size,player_size))

    clock.tick(30)

    pygame.display.update()

    
    
