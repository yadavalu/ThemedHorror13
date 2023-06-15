import pygame
import time
import random

import tilemaps
from background import get_background
from spritesheet import SpriteSheet
from wheel import Wheel

pygame.init()
(w, h) = (1000, 900)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Horror")

running = True

tilemap = random.choice(tilemaps.tilemaps)
background, bg_image = get_background(tilemap)

rects = []
for tile in background:
    rects.append(pygame.Rect(*tile, *bg_image.get_rect()[2:]))

ghost_data = {
    "forward": [6, 0],
    "left": [6, 1],
    "right": [6, 2],
    "away": [6, 3],
    "dimensions": [48, 48],
    "scale": [64, 64],
    "offset": [10, 5]
}


sprite_data = {
    "forward": [8, 0],
    "right": [8, 1],
    "left": [8, 2],
    "away": [8, 3],
    "dimensions": [77, 77],
    "scale": [64, 64],
    "offset": [20, 10]
}


clock = pygame.Clock()
ghost = SpriteSheet(screen, 896, 64, clock, pygame.image.load("ghost.png"), ghost_data, rects)
sprite = SpriteSheet(screen, 64, 64, clock, pygame.image.load("sprite.png"), sprite_data, rects)
dir = 0
dir2 = 1
no_animation = 0

sprite.animate("forward")
pygame.display.set_icon(pygame.image.load("icon.png"))

wheel = Wheel(screen, "icon.png")  # TODO: get wheel images

t0 = time.time()
t0_1 = time.time()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dir = 2
            if event.key == pygame.K_RIGHT:
                dir = 1
            if event.key == pygame.K_UP:
                dir = 4
            if event.key == pygame.K_DOWN:
                dir = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dir = 0
            if event.key == pygame.K_SPACE:
                wheel.turn()

    t1 = time.time()

    if t1 - t0_1 > 1:
        dir2 = random.randint(1, 4)
        t0_1 = time.time()

    sprite.move(dir)
    while True:
        ghost.move(dir2)
        if not ghost.collision:
            break
        else:
            dir2 = random.randint(1, 4)

    screen.fill((0, 0, 0))

    for tile in background:
        screen.blit(bg_image, tile)

    t1 = time.time()

    if t1 - t0 > 0.07:
        if dir == 3:
            sprite.animate("forward")
        elif dir == 2:
            sprite.animate("right")
        elif dir == 1:
            sprite.animate("left")
        elif dir == 4:
            sprite.animate("away")
        else:
            sprite.single(0, 0)

        if dir2 == 3:
            ghost.animate("forward")
        elif dir2 == 1:
            ghost.animate("right")
        elif dir2 == 2:
            ghost.animate("left")
        elif dir2 == 4:
            ghost.animate("away")
        else:
            ghost.single(0, 0)

        t0 = time.time()

    ghost.render()
    sprite.render()
    wheel.render()

    pygame.display.update()

pygame.quit()
