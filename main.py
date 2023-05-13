from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, speed, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_RIGHT] and self.rect.x < 700 - 65 - 5:
            self.rect.x += self.speed
            


window = display.set_mode((700, 500))
display.set_caption('Пинг - Понг')
background = transform.scale(image.load('пинг понг.jpg'), (700, 500))
clock = time.Clock()
FPS = 40
game = True
finish = False

while game:
    if finish != True:
        window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(40)
