import pygame
import importlib

import options
from widgets import Button, Label
import play
import instructions
import sfx

pygame.init()
(w, h) = (1000, 900)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Horror")
clock = pygame.Clock()

font = pygame.font.SysFont(None, 30)
l = Label(screen,  pygame.font.SysFont(None, 100), "PacGhost", (200, 100, 100), 450, 150, 100, 50)
l2 = Label(screen,  font, "ThemedHorror13 Game Jam", (183, 183, 183), 450, 225, 100, 50)
b = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "Play", (183, 183, 183), 200, 300, 600, 50)
i = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "Instructions", (183, 183, 183), 200, 400, 600, 50)
o = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "Options", (183, 183, 183), 200, 500, 600, 50)
q = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "Quit", (183, 183, 183), 200, 600, 600, 50)
r = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "Replay", (183, 183, 183), 200, 700, 600, 50)

sfx.bgm()

while True:
    dt = clock.tick(60)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if r.handle_event(event, pos):
            importlib.reload(play)
            ret = play.play()
            if ret == 1:
                b.text = "Resume"
            elif ret == 100: 
                l2.text = "Congrats!! You Won!!"
        if b.handle_event(event, pos):
            ret = play.play()
            if ret == 1:
                b.text = "Resume"
            elif ret == 100: 
                l2.text = "Congrats!! You Won!!"
        if q.handle_event(event, pos):
            pygame.quit()
            exit(0)
        if i.handle_event(event, pos):
            instructions.instructions()
        if o.handle_event(event, pos):
            options.options()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    screen.fill((36, 34, 30))
    l.render()
    l2.render()
    b.render()
    r.render()
    i.render()
    o.render()
    q.render()
    pygame.display.update()