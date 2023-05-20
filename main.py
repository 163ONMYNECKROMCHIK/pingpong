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
ball = GameSprite('kovobanga.png', 10, 250, 250, 100, 50)



window = display.set_mode((700, 500))
display.set_caption('Пинг - Понг')
background = transform.scale(image.load('пинг понг.jpg'), (700, 500))
clock = time.Clock()
FPS = 40
game = True
finish = False

font.init()
font1 = font.Font(None, 45)
lose1 = font1.render('PLAYER 1 LOSE!', True, (0, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (0, 0, 0))

speed_x = 3
speed_y = 3

while game:
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1

        if ball.rect.y > 500 - 50 or ball.rect.y < 0:
            speed_y *= -1
        window.blit(background, (0, 0))
        if ball.rect.x > 650:
            finish = True
            window.blit(lose1, (200, 200))


        if ball.rect.x < 0:
            finish = True
            window.blit(lose2, (200, 200))



        rocket1.reset()
        rocket1.update_l()
        rocket2.reset()
        rocket2.update_r()
        ball.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(40)
