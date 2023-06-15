import pygame
import random

class SpriteSheet:
    def __init__(self, screen, x, y, clock: pygame.time.Clock, img, data, tile_rects, part_colour):
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

        self.particles = []
        self.part_colour = part_colour
        self.curr_action = None

    def get_size(self, x, y, width, height):
        self.render_img = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        self.render_img.blit(self.img, (0, 0), (x, y, width, height))

    def move(self, dir, dt):
        x = self.x
        y = self.y

        if dir == 3:
            y += self.vel * dt * 0.08
        if dir == 2:
            x -= self.vel * dt * 0.08
        if dir == 1:
            x += self.vel * dt * 0.08
        if dir == 4:
            y -= self.vel * dt * 0.08

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

        if x != self.x or y != self.y:
            for i in range(3): self.particles.append([[self.x + self.data["scale"][0]/2, self.y + self.data["scale"][1]], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])

        self.x = x
        self.y = y
        self.collision = False

        self.rect = pygame.Rect(self.x + self.data["offset"][0], self.y + self.data["offset"][1], self.data["scale"][0] - 2 * self.data["offset"][0], self.data["scale"][1] - self.data["offset"][1])

    def collect(self, coins):
            for i in coins:
                if self.x // 64 - 1 <= i.pos[0] / 64 <= self.x // 64 + 1 and self.y // 64 - 1 <= i.pos[1] / 64 <= self.y // 64 + 1:
                    i.destroy = True

    def render(self):
        self.screen.blit(pygame.transform.scale(self.render_img, self.data["scale"]), (self.x, self.y))

        to_remove = []
        for particle in self.particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            pygame.draw.circle(self.screen, self.part_colour, particle[0], particle[2])
            if particle[2] <= 0:
                to_remove.append(particle)

        for i in to_remove:
            self.particles.remove(i)

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
