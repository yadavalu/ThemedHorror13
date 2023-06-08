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

ninja_data = {
    "idle": [9, 0],
    "right": [8, 1],
    "jump": [8, 2],
    "side_attack": [4, 6],
    "front_attack": [8, 7],
    "death": [7, 8],
    "dimensions": [288, 288]
}

mage_data = {
    "idle": [8, 0],
    "dimensions": [64, 64]
}

viking_data = {
    "idle": [7, 0],
    "right": [6, 1],
    "jump": [5, 2],
    "attack": [9, 3],
    "shield": [9, 4],
    "death": [9, 5],
    "dimensions": [32, 32]
}

ghost = SpriteSheet(screen, 100, 100, pygame.image.load("ghost.png"), ghost_data)
sprite = SpriteSheet(screen, 200, 100, pygame.image.load("sprite.png"), sprite_data)
ninja = SpriteSheet(screen, 300, 100, pygame.image.load("Ninja_Free(FIXED)/Ninja_Free(FIXED)/Ninja HD Sample.png"), ninja_data)
mage = SpriteSheet(screen, 400, 100, pygame.image.load("Wizard/Wizard/MAGE.png"), mage_data)
viking = SpriteSheet(screen, 500, 100, pygame.image.load("viking(1)/viking/viking2.png"), viking_data)

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
        ninja.animate("idle")
        mage.animate("idle")
        viking.animate("attack")
        t0 = time.time()

    ghost.render()
    sprite.render()
    ninja.render()
    mage.render()
    viking.render()

    pygame.display.update()

pygame.quit()
