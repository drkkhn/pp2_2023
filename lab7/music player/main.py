from pygame import mixer as mix
import pygame as pg
from sys import exit
from tkinter import *
from tkinter import filedialog

songs=['1.wav' , '2.wav']

pg.init()
mix.init()
clock=pg.time.Clock()

screen=pg.display.set_mode((480, 400))
pg.display.set_caption("music player")

bg=pg.Surface((800,800))
pg.Surface.fill(bg,(0,0,0))
f1=pg.font.SysFont('freesansbold', 40, True)
f2=pg.font.SysFont('freesansbold', 35)

play=pg.image.load("play.png")
pause=pg.image.load("stop.png")

next=pg.image.load("next1.png")

prev=pg.image.load("prev1.png")



currid=0
currsong=pg.mixer.music.load(songs[currid])
pg.mixer.music.play()
pg.mixer.music.pause()
ch=False
ch1=False
ch2=False
tm=0
tm2=0

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        elif event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                if(ch):
                    pg.mixer.music.pause()
                    ch=0
                else:
                    pg.mixer.music.unpause()
                    ch=1
            if event.key==pg.K_RIGHT:
                currid=(currid+1)%3
                pg.mixer.music.stop()
                pg.mixer.music.load(songs[currid])
                pg.mixer.music.play()
                ch1=True
                if not ch :
                    pg.mixer.music.pause()
            if event.key==pg.K_LEFT:
                currid=(currid-1+3)%3
                pg.mixer.music.stop()
                pg.mixer.music.load(songs[currid])
                pg.mixer.music.play()
                ch2=True
                if not ch :
                    pg.mixer.music.pause()
                   


                  
    text1=f1.render("Currently playing:", True, (255, 255, 255))
    text2=f2.render(songs[currid], True, (255, 255, 255))        
    screen.blit(bg, (0,0))
    screen.blit(text1,(25,25))
    screen.blit(text2,(50,50))
    if ch:
        screen.blit(pause, (195,90))
    else:
        screen.blit(play, (195,90))

    if ch1:
        screen.blit(next, (295,90))
        tm+=1
    else:
        screen.blit(next, (295,90))

    if ch2:
        screen.blit(prev, (95,90))
        tm2+=1
    else:
        screen.blit(prev, (95,90))

    if tm>=8:
        ch1=False
        tm=0
    if tm2>=8:
        ch2=False
        tm2=0
    pg.display.update()
    clock.tick(60)