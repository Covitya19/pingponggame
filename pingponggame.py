
from pygame import *

class GameSprite():
    def __init__(self, player_image, player_x, player_y, player_s, player_w, player_h):
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.player_s = player_s

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.player_s
        if keys_pressed[K_s] and self.rect.y <= 500:
            self.rect.y += self.player_s

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.player_s
        if keys_pressed[K_DOWN] and self.rect.y <= 500:
            self.rect.y += self.player_s

font.init()
font = font.SysFont('Arial', 35)

win1 = font.render('Игрок 1 победил.', True, (255, 0, 0))
win2 = font.render('Игрок 2 победил.', True, (255, 0, 0))



background_c = (120, 255, 50)
window = display.set_mode((700, 500))
display.set_caption('ping pong game')
window.fill(background_c)

racket1 = Player1('palkaPPG.png', 30, 200, 4, 50, 150) 
racket2 = Player2('palkaPPG.png', 520, 200, 4, 50, 150)
ball = GameSprite('ballPPG.jpg', 200, 200, 4, 50, 50)

FPS = 60
clock = time.Clock()

running = True
finish = False

speed_x = 3
speed_y = 3

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    if finish != True:

        racket1.update()
        racket2.update()
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y


        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
            speed_x *= -1

        if ball.rect.x <= 0:
            window.blit(win2, (200, 200))

        if ball.rect.x >= 700:
            window.blit(win1, (200, 200))
            
    racket1.reset()
    racket2.reset()
    ball.reset()


    display.update()
    clock.tick(FPS)
