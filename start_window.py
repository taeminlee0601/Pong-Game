import pygame

BLACK = 0,0,0
WHITE = 255,255,255

def start_window(screen, START_FONT, TITLE_FONT):
    screen.fill(BLACK)

    start_text = START_FONT.render("Press Any Key to Start", 1, WHITE)
    title = TITLE_FONT.render("PONG GAME", 1, WHITE)

    screen.blit(start_text, (screen.get_width() / 2 - start_text.get_width() / 2, screen.get_height() / 2 - start_text.get_height()/2 + 100))
    screen.blit(title, (screen.get_width() / 2 - title.get_width() / 2, screen.get_height() / 2 - title.get_height()/2 - 50))

    pygame.display.update()

