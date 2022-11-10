import pygame
screnn = pygame.display.set_mode((400,400))
from pygame.locals import *
import pygame, sys

RED = (255, 0, 0)

def main():
    pygame.init()

    screen = pygame.display.set_mode((400,300))

    pygame.draw.circle(screen, RED, (20, 20), 10)
    pygame.display.update()

    red = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
if __name__ == '__main__':
    main()