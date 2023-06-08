import pygame
import time

from background import get_background
from spritesheet import SpriteSheet

pygame.init()
(w, h) = (1000, 900)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Horror")

running = True

background, bg_image = get_background()

ghost_data = {
    "walk_forward": {
        "n": 6,
        "index": 0
    },
    "walk_left": {
        "n": 6,
        "index": 1
    },
    "walk_right": {
        "n": 6,
        "index": 2
    },
    "walk_away": {
        "n": 6,
        "index": 3
    },
    "dimensions": [48, 48]
}

ghost = SpriteSheet(screen, 100, 100, pygame.image.load("ghost.png"), ghost_data)


clock = pygame.Clock()
t0 = time.time()

while running:
    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for tile in background:
        screen.blit(bg_image, tile)

    t1 = time.time()

    if t1 - t0 > 0.1:
        ghost.animate("walk_forward")
        t0 = time.time()

    ghost.render()

    pygame.display.update()

pygame.quit()
