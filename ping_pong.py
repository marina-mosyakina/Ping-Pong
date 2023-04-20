from pygame import *
window = display.set_mode((1000,700))
display.set_caption('ОКНООООООО')
fon = transform.scale(image.load('fon.jpg'),(1000,700))
clock = time.Clock()
game = True
while game:
    clock.tick(60)
    window.blit(fon,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
