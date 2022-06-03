from pygame import *

window = display.set_mode((700, 600))

clock = time.Clock()

display.set_caption("Ping Pong")

class ImageSprite(sprite.Sprite):
    def __init__(self, file, position, size, speed=(0, 0)):
        super().__init__()
        self.image = image.load(file)
        self.image = transform.scale(self.image, size)
        self.rect = Rect(position, size)
        self.speed = Vector2(speed)
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

class Player2(ImageSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_DOWN]:
            self.rect.y += self.speed.y
        if keys[K_UP]:
            self.rect.y -= self.speed.y
        
        if self.rect.top >= 500:
            self.rect.top = 500
        if self.rect.bottom <= 100:
            self.rect.bottom = 100

        

class Player1(ImageSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_s]:
            self.rect.y += self.speed.y
        if keys[K_w]:
            self.rect.y -= self.speed.y

        if self.rect.top >= 500:
            self.rect.top = 500
        if self.rect.bottom <= 100:
            self.rect.bottom = 100

class Ball(ImageSprite):
    def update(self):
        self.rect.topleft += self.speed

         
        

player_1 = Player1(file="rocket.png", position=(0, 510), size=(80, 80), speed=(0, 12.5))
player_2 = Player2(file="rocket.png", position=(620, 510), size=(80, 80), speed=(0, 12.5))
ball = Ball(file="ball.png", position=(250, 250), size=(80, 80), speed=(2, 3))





game_on = True

while game_on:

    for ev in event.get():

        if ev.type == QUIT:
            game_on = False

    window.fill((255, 255, 255))
    player_1.update()
    player_1.draw(window)
    player_2.update()
    player_2.draw(window)
    ball.update()
    ball.draw(window)

    display.update()
    clock.tick(69)