import pygame
import numpy as np

class SpriteSheet:
    def __init__(self, screen, x, y, clock: pygame.time.Clock, img, data, tile_rects):
        self.screen = screen

        self.tile_rects = tile_rects

        self.x = x
        self.y = y
        self.vel = 2  # np.abs(int(5*np.sin(2*self.clock.get_time()) + 1))
        self.clock = clock
        self.img = img
        self.render_img = pygame.Surface((0, 0))


        self.data = data
        self.index = 0

        self.collision = False
        self.rect = pygame.Rect(self.x + self.data["offset"][0], self.y + self.data["offset"][1], self.data["scale"][0] - 2 * self.data["offset"][0], self.data["scale"][1] - self.data["offset"][1])

        self.curr_action = None

    def get_size(self, x, y, width, height):
        self.render_img = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        self.render_img.blit(self.img, (0, 0), (x, y, width, height))

    def move(self, dir):
        x = self.x
        y = self.y

        if dir == 3:
            y += self.vel
        if dir == 2:
            x -= self.vel
        if dir == 1:
            x += self.vel
        if dir == 4:
            y -= self.vel

        self.rect.x = x + self.data["offset"][0]
        self.rect.y = y + self.data["offset"][1]

        for i in self.tile_rects:
            if i.x != -1:
                if i.colliderect(self.rect):
                    if not self.collision:
                        self.collision = True
                    self.rect = pygame.Rect(self.x + self.data["offset"][0], self.y + self.data["offset"][1],
                                            self.data["scale"][0] - 2 * self.data["offset"][0],
                                            self.data["scale"][1] - self.data["offset"][1])
                    return

        self.x = x
        self.y = y
        self.collision = False

        self.rect = pygame.Rect(self.x + self.data["offset"][0], self.y + self.data["offset"][1], self.data["scale"][0] - 2 * self.data["offset"][0], self.data["scale"][1] - self.data["offset"][1])



    def render(self):
        #self.screen.blit(self.render_img, (self.x, self.y))
        #xoffset = 10
        #yoffset = 5
        #pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.x + xoffset, self.y + yoffset, self.data["scale"][0] - 2 * xoffset, self.data["scale"][1] - yoffset))
        self.screen.blit(pygame.transform.scale(self.render_img, self.data["scale"]), (self.x, self.y))

    def handle_event(self):
        pass

    def single(self, x, y):
        self.get_size(x, y, *self.data["dimensions"])

    def animate(self, action):
        if self.curr_action is None:
            self.index = 0
            self.curr_action = action
        else:
            if action == self.curr_action:
                self.index += 1
            else:
                self.index = 0
                self.curr_action = action

        if self.index == self.data[action][0] - 1:
            self.index = 0

        self.get_size(self.index*self.data["dimensions"][0], self.data[action][1]*self.data["dimensions"][1], *self.data["dimensions"])
