# import the pygame module
import pygame

# import pygame.locals for easier access to key coordinates
from pygame.locals import *

# initialize pygame
pygame.init()

# create the screen object
# here we pass it a size of 800x600
screen = pygame.display.set_mode((800,600))

# create our 'player', right now he's just a rectangle
player = pygame.Surface((50,50))
player.fill((255,255,255))


running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False


    screen.blit(player, player.get_rect())
    pygame.display.flip()
