import pygame


class SpriteSheet:
    def __init__(self, screen, x, y, img, data):
        self.screen = screen

        self.x = x
        self.y = y
        self.img = img
        self.render_img = pygame.Surface((0, 0))

        self.data = data
        self.index = 0

        self.curr_action = None

    def get_size(self, x, y, width, height):
        self.render_img = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        self.render_img.blit(self.img, (0, 0), (x, y, width, height))

    def render(self):
        #self.screen.blit(self.render_img, (self.x, self.y))
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
