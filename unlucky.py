import pygame

class Unlucky:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
    
    def render(self):
        pygame.draw.circle(self.screen, (150, 150, 0), (500, 500), 100)
        pygame.display.update()

    def handle(self):
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.running = False
