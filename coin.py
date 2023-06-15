import pygame
import random
import pprint

class Coin:
    def __init__(self, screen, tilemap, coin_img):
        self.screen = screen
        self.tilemap = tilemap
        self.img = pygame.image.load(coin_img)
        self.pos = self.init_pos()
    
    def init_pos(self):
        randx = random.randint(0, len(self.tilemap) - 1)
        randy = random.randint(0, len(self.tilemap[0]) - 1)
        print(randx, randy)
        pprint.pprint(self.tilemap)
        if self.tilemap[randx][randy] == 1:
            self.init_pos()
        return ((randx - 1) * 64, (randy - 1) * 64)

    def render(self):
        self.screen.blit(self.img, self.pos)