import pygame
from background import get_background
from pprint import pprint



tilemap = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


pygame.init()
(w, h) = (1000, 900)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Horror")

background, bg_image = get_background(tilemap)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pprint(tilemap)
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drag = True
        if event.type == pygame.MOUSEBUTTONUP and drag:
            x, y = pygame.mouse.get_pos()
            print(x//64, y//64)
            try:
                if tilemap[x//64 - 1][y//64 - 1] == 1:
                    tilemap[x//64 - 1][y//64 - 1] = 0
                else:
                    tilemap[x//64 - 1][y//64 - 1] = 1
                background, bg_image = get_background(tilemap)
            except:
                pass

    screen.fill((0, 0, 0))
    for tile in background:
        screen.blit(bg_image, tile)

    pygame.display.update()
