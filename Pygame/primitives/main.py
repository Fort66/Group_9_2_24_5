import pygame as pg

from pygame.locals import QUIT, RESIZABLE, FULLSCREEN, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN, MOUSEMOTION

from pygame.display import set_mode, set_caption

from random import choice

pg.init()

# width = 1024
# height = 768

size = [1024, 768]

scr = set_mode(size)
set_caption('MyGame')


# colors = ['SteelBlue', 'Indigo', 'DarkOliveGreen', 'DarkRed']

class Player:
    def __init__(self):
        self.image = pg.Surface([50, 50])
        self.image.fill('SteelBlue')
        self.rect = self.image.get_rect()


player = Player()


loop = True

while loop:
    scr.fill('black')

    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

        if event.type == KEYDOWN:
            if event.key == pg.K_RIGHT:
                player.rect.centerx += 10
            elif event.key == pg.K_LEFT:
                player.rect.centerx -= 10

        # if event.type == MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         scr.fill(choice(colors), pg.Rect(event.pos[0], event.pos[1], 15, 15))

    scr.blit(player.image, player.rect)
    
    
    # pg.draw.circle(scr, 'blue', (100, 100), 50, 5)
    # pg.draw.rect(scr, 'red', (10, 10, 100, 100), 1)

    # pg.draw.aaline(scr, 'green', (10, 10), (300, 600))
    # pg.draw.line(scr, 'green', (100, 10), (600, 600), 1)

    # pg.draw.polygon(scr, 'yellow', [[150, 310], [180, 350], [90, 390]], 1)


    pg.display.update()
pg.quit() # выход из pygame