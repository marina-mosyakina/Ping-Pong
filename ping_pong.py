from pygame import *
window = display.set_mode((1000,700))
display.set_caption('ОКНООООООО')
fon = transform.scale(image.load('fon.jpg'),(1000,700))
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 610:
            self.rect.y += self.speed
    def move2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 610:
            self.rect.y += self.speed
platform1 = Player('platforma1.png',20,300,30,90,10)
platform2 = Player('platforma2.png',930,300,30,90,10)
ball = GameSprite('ball.png',470,330,50,50,5)
game = True
while game:
    clock.tick(60)
    window.blit(fon,(0,0))
    platform1.move2()
    platform1.reset()
    platform2.move()
    platform2.reset()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
