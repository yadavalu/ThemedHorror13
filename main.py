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
    "walk_forward": [6, 0],
    "walk_left": [6, 1],
    "walk_right": [6, 2],
    "walk_away": [6, 3],
    "dimensions": [48, 48]
}


sprite_data = {
    "walk_forward": [8, 0],
    "walk_right": [8, 1],
    "walk_left": [8, 2],
    "walk_away": [8, 3],
    "dimensions": [77, 77]
}


ghost = SpriteSheet(screen, 100, 100, pygame.image.load("ghost.png"), ghost_data)
sprite = SpriteSheet(screen, 200, 100, pygame.image.load("sprite.png"), sprite_data)
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
        ghost.animate("walk_left")
        sprite.animate("walk_right")
        t0 = time.time()

    ghost.render()
    sprite.render()

    pygame.display.update()

pygame.quit()
