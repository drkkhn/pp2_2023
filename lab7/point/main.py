import pygame as pg
from sys import exit

screen=pg.display.set_mode((800,600))
pg.display.set_caption("Task 3, TSIS 7")
clock=pg.time.Clock()

bg=pg.Surface((800,600))
bg2=pg.Surface((800,600))
pg.Surface.fill(bg2,(255,255,255))

posx=0
posy=0

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_DOWN:
                if(posy+45<=375):
                    posy+=20
            if event.key==pg.K_UP:
                if(posy-45>=-25):
                    posy-=20
            if event.key==pg.K_RIGHT:
                if(posx+45<=475):
                    posx+=20
            if event.key==pg.K_LEFT:
                if(posx-45>=-25):
                    posx-=20
        

    screen.fill('black')
    pg.draw.circle(screen, (255,204,204), (posx+25, posy+25), 25)
    pg.display.flip()
    clock.tick(60)