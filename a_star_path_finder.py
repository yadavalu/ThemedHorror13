from math import sqrt

class AStarPathFinder:
    def __init__(self, ghost, sprite, tile_map):
        self.ghost = ghost
        self.ghost.vel = 64
        self.sprite = sprite
        self.tile_map = tile_map

        self.g_cost = [[0] * 13] * 16
        self.h_cost = [[0] * 13] * 16
        self.f_cost = [[0] * 13] * 16
        self.dir = 0

        self.quit_calculate = False

    def move(self, dt):
        self.ghost.move(self.dir, dt)

    @staticmethod
    def distance(x0, x1, y0, y1):
        return sqrt((x1 - x0)**2 + (y1 - y0)**2)

    def calculate(self):
        if self.quit_calculate:
            self.quit_calculate = False
            return

        x0 = self.ghost.x // 64
        x1 = self.sprite.x // 64
        y0 = self.ghost.y // 64
        y1 = self.sprite.y // 64
        for i in range(16):
            for j in range(13):
                if self.tile_map[i][j] == 0:
                    if i == x0 and j == y0:
                        self.g_cost[i][j] = 100000000
                        self.h_cost[i][j] = 100000000
                        self.f_cost[i][j] = 200000000
                    else:
                        self.g_cost[i][j] = AStarPathFinder.distance(x0, i, y0, j)
                        self.h_cost[i][j] = AStarPathFinder.distance(x1, i, y1, j)
                        self.f_cost[i][j] = self.g_cost[i][j] + self.h_cost[i][j]
                        print(False)

                elif self.tile_map[i][j] == 1:
                    self.g_cost[i][j] = 100000000
                    self.h_cost[i][j] = 100000000
                    self.f_cost[i][j] = 200000000
                    print(True)

                print(self.f_cost[0][0])
        print(self.f_cost[0][0])
        ####################### ???????????????????????????????????????????????????????????????????????????????????


    def find_path(self, dt):
        x0 = int(self.ghost.x // 64)
        y0 = int(self.ghost.y // 64)

        local_f_cost = [[200000000] * 3] * 3

        if y0 - 1 >= 0:
            local_f_cost[0][0] = self.f_cost[x0][y0 - 1]
        local_f_cost[0][1] = self.f_cost[x0][y0]
        if y0 + 1 <= 15:
            local_f_cost[0][2] = self.f_cost[x0][y0 + 1]
        if x0 - 1 >= 0:
            if y0 - 1 >= 0:
                local_f_cost[0][0] = self.f_cost[x0 - 1][y0 - 1]
            local_f_cost[0][1] = self.f_cost[x0 - 1][y0]
            if y0 + 1 <= 15:
                local_f_cost[0][2] = self.f_cost[x0 - 1][y0 + 1]
        if x0 + 1 <= 12:
            if y0 - 1 >= 0:
                local_f_cost[0][0] = self.f_cost[x0 + 1][y0 - 1]
            local_f_cost[0][1] = self.f_cost[x0 + 1][y0]
            if y0 + 1 <= 15:
                local_f_cost[0][2] = self.f_cost[x0 + 1][y0 + 1]


        dir = [0, 0, 0]
        for i in range(3):
            try:
                dir[i] = local_f_cost[i].index(min(local_f_cost[i]))
            except ValueError: return

        x = min(dir)
        y = dir.index(x)
        print(x, y)

        self.dir = 0
        if x == 0:
            self.dir = 2
        elif x == 2:
            self.dir = 1

        self.move(dt)

        self.dir = 0
        if y == 0:
            self.dir = 4
        elif y == 2:
            self.dir = 3

        self.move(dt)
