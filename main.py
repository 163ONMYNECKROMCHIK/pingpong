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

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 500 - 150 - 5:
            self.rect.y += self.speed

    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 500 - 150 - 5:
            self.rect.y += self.speed

rocket1 = Player("платформа2.jpg", 5, 20, 50, 20, 150)
rocket2 = Player("платформа3.jpg", 5, 660, 50, 20, 150)



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
        rocket1.reset()
        rocket1.update_l()
        rocket2.reset()
        rocket2.update_r()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(40)
