"""
This is an individual project. This game uses Python3 and pygame.
"""

import pygame

pygame.init()

WIDTH, HEIGHT = 900, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

FPS = 60

WHITE = 255,255,255
BLACK = 0,0,0

pygame.time.Clock()

