#ping pong game

from pygame import *

class GameSprite():
    def __init__(self, player_x, player_y, player_s, player_w, player_h):
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.player_s = player_s
        self.player_w = player_w
        self.player_h = player_h

    def reset(self):
        pass

class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= 500:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_Up] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_Down] and self.rect.y <= 500:
            self.rect.y += self.speed
            

background_c = (120, 255, 50)
window = pygame.display.setmode((700, 500))
pygame.display.set_caption('ping pong game')
window.fill(background_c)
pygame.display.flip()
FPS = 60
clock = time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.tipe == pygame.QUIT:
            running = False
    display.update()
    clock.tick(FPS)
    
