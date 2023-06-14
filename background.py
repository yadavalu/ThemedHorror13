import random
import pygame
import tilemaps

def get_background(tilemap):
    image = pygame.image.load("bg.png")

    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(pygame.display.get_surface().get_size()[0] // width + 1):
        for j in range(pygame.display.get_surface().get_size()[1] // height + 1):
            try:
                if tilemap[i - 1][j - 1] == 1:
                    pos = (i * width, j * height)
                    tiles.append(pos)
                else:
                    tiles.append((-1, -1))
            except: pass

    return tiles, image
