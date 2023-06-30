import pygame
import sys

class Unlucky:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.event = pygame.event.get()

    def render(self):
        pygame.draw.circle(self.screen, (150, 150, 0), (500, 500), 100)
        pygame.draw.line(self.screen, (255, 0, 0), (500, 500), (500, 400))
        pygame.display.update()

    def handle(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                self.running = False
                sys.exit(0)
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_SPACE:
                    self.running = False
