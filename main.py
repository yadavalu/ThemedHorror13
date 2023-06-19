import pygame
from widgets import Button

pygame.init()
(w, h) = (1000, 900)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Horror")
clock = pygame.Clock()

font = pygame.font.SysFont(None, 30)

while True:        
    b = Button(screen, (0, 140, 10), (140, 10, 0), (140, 140, 10), font, "Resume", (100, 100, 255), 500, 500, 200, 50)
    dt = clock.tick(60)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if b.handle_event(event, pos):
            import play
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    screen.fill((52, 78, 91))
    b.render()
    pygame.display.update()