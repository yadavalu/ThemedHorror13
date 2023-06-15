import pygame
import random
import pygame

class Coin:
    def __init__(self, screen, tilemap, coin_img):
        self.screen = screen
        self.tilemap = tilemap
        self.img = pygame.image.load(coin_img)
        self.pos = self.init_pos()

    def init_pos(self):
        randx = random.choice(range(pygame.display.get_surface().get_size()[0] // 64 + 1))
        randy = random.choice(range(pygame.display.get_surface().get_size()[1] // 64 + 1))
        while self.tilemap[randx - 1][randy - 1] == 1:
            randx = random.choice(range(pygame.display.get_surface().get_size()[0] // 64 + 1))
            randy = random.choice(range(pygame.display.get_surface().get_size()[1] // 64 + 1))
        return (randx * 64, randy * 64)

    def render(self):
        self.screen.blit(self.img, self.pos)