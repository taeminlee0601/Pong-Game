import pygame

BLACK = 0,0,0
WHITE = 255,255,255

def end_window(screen, SCOREBOARD_FONT, END_FONT, score_left, score_right, winner):
    screen.fill(BLACK)

    scoreboard = SCOREBOARD_FONT.render(str(score_left) + ":" + str(score_right), 1, WHITE)
    player_win = END_FONT.render("Player " + str(winner) + " WINS", 1, WHITE)
    play_again = END_FONT.render("Press Any Key to Play Again", 1, WHITE)

    screen.blit(scoreboard, (screen.get_width() / 2 - scoreboard.get_width() / 2, screen.get_height() / 2 - scoreboard.get_height()/2))
    screen.blit(player_win, (screen.get_width()/2 - player_win.get_width()/2, screen.get_height()/2 - scoreboard.get_height()/2 - 50 - player_win.get_height()/2))
    screen.blit(play_again, (screen.get_width()/2 - play_again.get_width()/2, screen.get_height()/2 + scoreboard.get_height()/2 + 25))

    pygame.display.update()

    