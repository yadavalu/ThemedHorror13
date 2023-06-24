import pygame
import random
from pprint import pprint

from a_star_path_finder import AStarPathFinder
from spritesheet import SpriteSheet
import tilemaps
from background import get_background


pygame.init()

screen = pygame.display.set_mode((1000, 900))

open = True

clock = pygame.Clock()
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

tilemap = tilemaps.tilemaps[0]
background, bg_image = get_background(tilemap)

rects = []
for tile in background:
    rects.append(pygame.Rect(*tile, *bg_image.get_rect()[2:]))

ghost = SpriteSheet(screen, 896, 64, clock, pygame.image.load("ghost.png"), ghost_data, rects, (200, 200, 200))
sprite = SpriteSheet(screen, 64, 64, clock, pygame.image.load("sprite.png"), sprite_data, rects, (200, 50, 50))
ghost.single(0, 0)
sprite.single(0, 0)

path_finder = AStarPathFinder(ghost, sprite, tilemap)
path_finder.calculate()

clock = pygame.Clock()

while open:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
            break

    screen.fill((0, 0, 0))

    for tile in background:
        screen.blit(bg_image, tile)

    path_finder.find_path(dt)
    path_finder.calculate()

    sprite.render()
    ghost.render()

    pygame.display.update()


pygame.quit()
