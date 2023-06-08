import pygame
from background import get_background

pygame.init()
(w, h) = (1000, 900)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Horror")

running = True

background, bg_image = get_background()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    for tile in background:
        screen.blit(bg_image, tile)
    pygame.display.update()