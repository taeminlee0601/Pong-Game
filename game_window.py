import pygame

BLACK = 0,0,0
WHITE = 255,255,255
GREY = 219,219,219

def game_window(screen, left_paddle, right_paddle, SCORE_FONT, score_left, score_right, ball):
    screen.fill(BLACK)
    
    center_line = pygame.Rect((screen.get_width()/2 - 5, 0), (10, screen.get_height()))
    top_line = pygame.Rect((0,0), (screen.get_width(), 10))
    bottom_line = pygame.Rect((0, screen.get_height()-10), (screen.get_width(), 10))

    right_score = SCORE_FONT.render(str(score_right), 1, WHITE)
    left_score = SCORE_FONT.render(str(score_left), 1, WHITE)

    pygame.draw.rect(screen, WHITE, center_line)
    pygame.draw.rect(screen, WHITE, top_line)
    pygame.draw.rect(screen, WHITE, bottom_line)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.rect(screen, GREY, ball.ball)
    screen.blit(right_score, (screen.get_width()/2 + 30, 20))

    if score_left < 10:
        screen.blit(left_score, (screen.get_width()/2 - 23 - 25, 20))
    else:
        screen.blit(left_score, (screen.get_width()/2 - 23 - 23 - 25, 20))


    pygame.display.update()