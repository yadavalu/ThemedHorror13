import pygame
from widgets import Button

pygame.init()
(w, h) = (1000, 900)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Horror")
clock = pygame.Clock()

font = pygame.font.SysFont(None, 30)

while True:        
    b = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "Play", (183, 183, 183), 50, 200, 600, 50)
    dt = clock.tick(60)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if b.handle_event(event, pos):
            import play
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    screen.fill((36, 34, 30))
    b.render()
    pygame.display.update()