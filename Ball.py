import pygame

class Ball():
    vel_x = 5
    vel_y = 0
    server = -1
    bounce = 0

    def __init__(self, screen):
        self.ball = pygame.rect.Rect((screen.get_width()/2 - 5, screen.get_height()/2 - 5), (10,10))
        self.bounce = 0

    def new_round(self, screen):
        self.ball = pygame.rect.Rect((screen.get_width()/2 - 5, screen.get_height()/2 - 5), (10,10))
        self.server *= -1
        self.vel_x *= -1
        self.vel_y = 0
        self.bounce = 0

    def check_collision(self, left_paddle, right_paddle, top, bottom):
        if self.ball.colliderect(left_paddle):
            self.bounce += 1
            return 1
        elif self.ball.colliderect(right_paddle):
            self.bounce += 1
            return 2
        elif self.ball.colliderect(top) or self.ball.colliderect(bottom):
            self.bounce += 1
            return 3
        else:
            return -1

    def check_out(self, screen):
        if self.ball.x < 0 or self.ball.x > screen.get_width():
            return True
        return False

    def out_left_right(self, screen):
        if self.ball.x < 0:
            return -1
        
        return 1

    def hit_top_bottom(self):
        self.vel_y *= -1

    def hit_left(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.vel_x *= -1
            self.vel_y = -5
        elif keys[pygame.K_s]:
            self.vel_x *= -1
            self.vel_y = 5
        else:
            self.vel_x *= -1
            self.vel_y *= -1

    def hit_right(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.vel_x *= -1
            self.vel_y = -5
        elif keys[pygame.K_DOWN]:
            self.vel_x *= -1
            self.vel_y = 5
        else:
            self.vel_x *= -1
            self.vel_y *= -1

    def move(self):
        self.ball.x += self.vel_x
        self.ball.y += self.vel_y