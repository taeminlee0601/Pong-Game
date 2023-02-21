import pygame

def handle_left_paddle(screen, left_paddle):
    VEL = 10
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and left_paddle.y > 10:
        left_paddle.y -= VEL
    elif keys[pygame.K_s] and left_paddle.y < screen.get_height() - 110:
        left_paddle.y += VEL

def handle_right_paddle(screen, right_paddle):
    VEL = 10
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and right_paddle.y > 10:
        right_paddle.y -= VEL
    elif keys[pygame.K_DOWN] and right_paddle.y < screen.get_height() - 110:
        right_paddle.y += VEL