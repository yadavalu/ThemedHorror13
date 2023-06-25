import pygame
from widgets import Button
import play
import instructions
import importlib

pygame.init()
(w, h) = (1000, 900)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Horror")
clock = pygame.Clock()

font = pygame.font.SysFont(None, 30)
b = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "Play", (183, 183, 183), 50, 200, 600, 50)
i = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "Instructions", (183, 183, 183), 50, 300, 600, 50)
o = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "Options", (183, 183, 183), 50, 400, 600, 50)
q = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "Quit", (183, 183, 183), 50, 500, 600, 50)
r = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "Replay", (183, 183, 183), 50, 600, 600, 50)
reimport = False

while True:
    dt = clock.tick(60)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if r.handle_event(event, pos):
            importlib.reload(play)
            play.play()
        if b.handle_event(event, pos):
            play.play()
        if q.handle_event(event, pos):
            pygame.quit()
            exit(0)
        if i.handle_event(event, pos):
            instructions.instructions()
        if o.handle_event(event, pos):
            pass
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    screen.fill((36, 34, 30))
    b.render()
    r.render()
    i.render()
    o.render()
    q.render()
    pygame.display.update()