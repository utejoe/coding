import pygame
screen = pygame.display.set_mode((400,400))
import pygame, sys
from pygame.locals import *

def draw_gallows(screen):
    pygame.draw.rect(screen, PURPLE, (450, 350, 100, 10)) # bottom
    pygame.draw.rect(screen, PURPLE, (495, 250, 10, 100)) # support
    pygame.draw.rect(screen, PURPLE, (450, 250, 50, 10)) # crossbar
    pygame.draw.rect(screen, PURPLE, (450, 250, 10, 25)) # noose

def draw_word(screen, spaces):
    x = 10
    for i in range (spaces):
        pygame.draw.line(screen, YELLOW, (x, 350), (x+20, 350), 3)
        x += 30

def draw_letter(screen, font, word, guess):
    x = 10
    for letter in word:
        if letter == guess:
            letter = font.render(letter, 3, (255, 255, 255))
            screen.blit(letter, (x, 300))
        x += 30

def draw_man(screen, body_part):
    if body_part == "head":
        pygame.draw.circle(screen, RED, (455, 270), 10) #HEAD
    if body_part == "body":
        pygame.draw.line(screen, RED, (455, 280). (455, 320), 3) #body
    if body_part == "I_arm":