from random import randint
import pygame

def get_background():
    image = pygame.image.load("bg.png")

    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(pygame.display.get_surface().get_size()[0] // width + 1):
        for j in range(pygame.display.get_surface().get_size()[1] // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image
