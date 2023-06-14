import pygame
import random

class Wheel:
    def __init__(self, screen, wheel_img):
        self.screen = screen
        self.wheel_img = pygame.image.load(wheel_img)
        self.wheel_pos = (50, 50)
    
    def turn(self):
        self.wheel_img = pygame.transform.rotate(self.wheel_img, random.randint(0, 360))
        self.wheel_pos = self.wheel_img.get_rect(center = self.wheel_img.get_rect(center = (50, 50)).center)

    def render(self):
        self.screen.blit(self.wheel_img, self.wheel_pos)
