"""
This is an individual project. This game uses Python3 and pygame.
"""

import pygame
from start_window import *
from game_window import * 
from game_mechanics import *

pygame.init()

WIDTH, HEIGHT = 900, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pong Game")

FPS = 60

WHITE = 255,255,255
BLACK = 0,0,0

START_FONT = pygame.font.Font('assets/bit5x5.ttf', 50)
TITLE_FONT = pygame.font.Font('assets/bit5x5.ttf', 100)
SCORE_FONT = pygame.font.Font('assets/bit5x5.ttf', 30)

clock = pygame.time.Clock()

screen.get_height()
screen.get_width()

def start():
    run = True

    while run:
        clock.tick(FPS)

        start_window(screen, START_FONT, TITLE_FONT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                play_game()

def play_game():
    run = True

    left_paddle = pygame.rect.Rect((10, screen.get_height()/2 - 50), (10, 100))
    right_paddle = pygame.rect.Rect((screen.get_width() - 20, screen.get_height()/2 - 50), (10,100))

    score_left = 0
    score_right = 0

    while run:
        clock.tick(FPS)

        right_paddle.x = screen.get_width() - 20
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        handle_left_paddle(screen, left_paddle)
        handle_right_paddle(screen, right_paddle)

        game_window(screen, left_paddle, right_paddle, SCORE_FONT, score_left, score_right)

if __name__ == "__main__":
    start()