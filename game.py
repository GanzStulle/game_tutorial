#basic comments
import pygame

#initial pygame
pygame.init()
#create screen (width, heigth)
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((800, 600))

#
game_over = False

while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_over = True #pygame.quit(), exit()
