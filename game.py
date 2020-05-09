#basic comments
import pygame
import sys
import random
#initial pygame
pygame.init()
#create screen (width, heigth)
WIDTH = 800
HEIGHT = 600

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND = (0,0,0)

player_size = 50
player_pos = [WIDTH/2, HEIGHT-HEIGHT/4]

enemy_size = 50
x_random = random.randint(0+enemy_size, WIDTH-enemy_size)
enemy_pos = [x_random, 0]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        #print(event)
        #quit while with cmd+q
        if event.type == pygame.QUIT:
            sys.exit()#game_over = True pygame.quit(), exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= player_size/0.75
            elif event.key == pygame.K_RIGHT:
                x += player_size/0.75

            player_pos = [x,y]

    screen.fill(BACKGROUND)
    if enemy_pos[1] >= 0 and enemy_pos[1] <= HEIGHT:
        enemy_pos[1] += enemy_size/3
    else:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0+enemy_size, WIDTH-enemy_size)
    pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)

    pygame.display.update()

    #pencil(x,y)

    #pygame.display.update()

pygame.quit()
exit()
