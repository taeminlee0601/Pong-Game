"""
This is an individual project. This game uses Python3 and pygame.
"""

import pygame
from start_window import *
from game_window import * 
from game_mechanics import *
from Ball import *

pygame.init()

WIDTH, HEIGHT = 900, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pong Game")

FPS = 60

WHITE = 255,255,255
BLACK = 0,0,0
GREY = 219,219,219

score_left = 0
score_right = 0

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

    center_line = pygame.Rect((screen.get_width()/2 - 5, 0), (10, screen.get_height()))
    top_line = pygame.Rect((0,0), (screen.get_width(), 10))
    bottom_line = pygame.Rect((0, screen.get_height()-10), (screen.get_width(), 10))

    left_paddle = pygame.rect.Rect((10, screen.get_height()/2 - 50), (10, 100))
    right_paddle = pygame.rect.Rect((screen.get_width() - 20, screen.get_height()/2 - 50), (10,100))
    ball = Ball(screen)

    end_score = 10

    while run:
        clock.tick(FPS)

        if score_left == 10 or score_right == 10:
            end_game()

        right_paddle.x = screen.get_width() - 20
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if ball.check_out(screen):

            left_right = ball.out_left_right(screen)

            if left_right == 1:
                score_left += 1
            else:
                score_right += 1

            ball.new_round(screen)
        else:
            check = ball.check_collision(left_paddle, right_paddle, top_line, bottom_line)
            
            if check == 1:
                ball.hit_left()
            elif check == 2:
                ball.hit_right()
            elif check == 3:
                ball.hit_top_bottom()
        
        ball.move()

        handle_left_paddle(screen, left_paddle)
        handle_right_paddle(screen, right_paddle)

        game_window(screen, left_paddle, right_paddle, SCORE_FONT, score_left, score_right, ball)

def end_game():
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                play_game()


if __name__ == "__main__":
    start()