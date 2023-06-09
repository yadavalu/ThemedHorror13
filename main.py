import pygame
import time
import random

import tilemaps
from background import get_background
from spritesheet import SpriteSheet

pygame.init()
(w, h) = (1000, 900)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Horror")

running = True

tilemap = random.choice(tilemaps.tilemaps)
background, bg_image = get_background(tilemap)

# TODO: Scaling
ghost_data = {
    "forward": [6, 0],
    "left": [6, 1],
    "right": [6, 2],
    "away": [6, 3],
    "dimensions": [48, 48],
    "scale": [64, 64]
}


sprite_data = {
    "forward": [8, 0],
    "right": [8, 1],
    "left": [8, 2],
    "away": [8, 3],
    "dimensions": [77, 77],
    "scale": [64, 64]
}


ghost = SpriteSheet(screen, 100, 100, pygame.image.load("ghost.png"), ghost_data)
sprite = SpriteSheet(screen, 200, 100, pygame.image.load("sprite.png"), sprite_data)
f, r, l, a = 0, 0, 0, 0
no_animation = 0

sprite.animate("forward")
pygame.display.set_icon(pygame.image.load("icon.png"))

clock = pygame.Clock()
t0 = time.time()

while running:
    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                f, r, l, a = 0, 1, 0, 0
            if event.key == pygame.K_RIGHT:
                f, r, l, a = 0, 0, 1, 0
            if event.key == pygame.K_UP:
                f, r, l, a = 0, 0, 0, 1
            if event.key == pygame.K_DOWN:
                f, r, l, a = 1, 0, 0, 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                f, r, l, a = 0, 0, 0, 0

    if f:
        sprite.y += 3
    if r:
        sprite.x -= 3
    if l:
        sprite.x += 3
    if a:
        sprite.y -= 3

    screen.fill((0, 0, 0))

    for tile in background:
        screen.blit(bg_image, tile)

    t1 = time.time()

    if t1 - t0 > 0.07:
        ghost.animate("left")
        if f:
            sprite.animate("forward")
        elif r:
            sprite.animate("right")
        elif l:
            sprite.animate("left")
        elif a:
            sprite.animate("away")
        else:
            sprite.single(0, 0)

        t0 = time.time()

    ghost.render()
    sprite.render()

    pygame.display.update()

pygame.quit()
