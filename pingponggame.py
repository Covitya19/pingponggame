from pygame import *

class GameSprite():
    def __init__(self, player_image, player_x, player_y, player_s, player_w, player_h):
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.player_s = player_s

    def reset(self):
        pass

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
            

background_c = (120, 255, 50)
window = display.set_mode((700, 500))
display.set_caption('ping pong game')
window.fill(background_c)

racket1 = Player1('racket.jpg', 30, 200, 4, 50, 150) 
racket2 = Player2('racket.jpg', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

FPS = 60
clock = time.Clock()

running = True
finish = False

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    if finish != True:

       racket1.update()
       racket2.update()
       ball.rect.x += 3
       ball.rect.y += 3

    racket1.reset()
    racket2.reset()
    ball.reset()


    display.update()
    clock.tick(FPS)
