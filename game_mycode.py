#basic comments
import pygame
import sys
import random
#initial pygame
pygame.init()
#create display parameters (width, heigth)
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

#create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#window name
pygame.display.set_caption('dodge the blox')
#textfield with game over
font = pygame.font.Font('freesansbold.ttf', 80)
text = font.render('GAME OVER', True, RED, BLUE)
textRect = text.get_rect()
textRect.center = (WIDTH // 2, HEIGHT // 2)


# font_co = pygame.font.Font('freesansbold.ttf', 80)
# text_co = font_co.render(str(counter), True, RED, BLUE)
# textRect_co = text_co.get_rect()
# textRect_co.center = (WIDTH //2, HEIGHT //2)

#display the score
def counter(count):
    font_co = pygame.font.Font('freesansbold.ttf', 32)
    text_co = font_co.render(str(count), True, RED, BLUE)
    textRect_co = text_co.get_rect()
    textRect_co.center = (WIDTH*0.9, HEIGHT *0.1)
    screen.blit(text_co, textRect_co)


game_over = False

count = 0

level = 3


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
            #change player position with K_LEFT
            if event.key == pygame.K_LEFT:
                x -= player_size/1.2
            #change player position with K_RIGTH
            elif event.key == pygame.K_RIGHT:
                x += player_size/1.2
            #update player position
            player_pos = [x,y]
    #define display colour
    screen.fill(BACKGROUND)

    #display the score
    counter(count)
    #screen.blit(text_co, textRect_co)

    #motion of enemy
    if enemy_pos[1] >= 0 and enemy_pos[1] <= HEIGHT:
        enemy_pos[1] += enemy_size/level
    else:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0+enemy_size, WIDTH-enemy_size)
        count +=1
        if level > 0.25 and count % 5 == 0:
            level -= 0.25

    #game over if positions xy of cubes are the same
    if (enemy_pos[1]+25-player_pos[1]+25) >= 0 and (enemy_pos[1]+25-player_pos[1]+25) < 50 or (player_pos[1]+25-enemy_pos[1]+25) >= 0 and (player_pos[1]+25-enemy_pos[1]+25) < 50:
        if (enemy_pos[0]+25-player_pos[0]+25) >= 0 and (enemy_pos[0]+25-player_pos[0]+25) < 50 or (player_pos[0]+25-enemy_pos[0]+25) >= 0 and (player_pos[0]+25-enemy_pos[0]+25) < 50:
            screen.blit(text, textRect)
            game_over = True
    else:
        print('ok', counter)

    #creat cubes for player and enemy
    pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)
    #update display
    pygame.display.update()

    #pencil(x,y)

    #pygame.display.update()
#pause for a few seconds
pygame.time.wait(2000)
pygame.quit()
exit()
