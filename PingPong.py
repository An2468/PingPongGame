from pygame import *

WIDTH = 700
HEIGHT = 600

window = display.set_mode((WIDTH, HEIGHT))


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
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed.y *= -1
        self.rect.topleft += self.speed

         
        

player_1 = Player1(file="PingPong.png", position=(0, 510), size=(80, 80), speed=(0, 12.5))
player_2 = Player2(file="PingPongBlue.png", position=(620, 510), size=(80, 80), speed=(0, 12.5))
ball = Ball(file="ball.png", position=(100, 100), size=(30, 30), speed=(2, 3))
red_win = ImageSprite(file="RedTeam.png", position=(0, 0), size=(WIDTH, HEIGHT), speed=0)
blue_win = ImageSprite(file="BlueTeam.png", position=(0, 0), size=(WIDTH, HEIGHT), speed=0)






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
    
    if sprite.collide_rect(ball, player_1) or sprite.collide_rect(ball, player_2):
        ball.speed.x *= -1
        ball.rect.x += ball.speed.x
    
    if ball.rect.x <= 0:
        blue_win.draw(window)
        
 

    if ball.rect.right >= WIDTH:
        red_win.draw(window)


    display.update()
    clock.tick(69)
