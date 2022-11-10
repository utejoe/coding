import pygame
screnn = pygame.display.set_mode((400,400))
from pygame.locals import *
import pygame, sys
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit ()
pygame.draw.circle(screen, RED, (20,20), 10)
pygame.display.update()