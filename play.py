import pygame
import time
import random
import sfx

import tilemaps
from background import get_background
from spritesheet import SpriteSheet
from wheel import Wheel
from coin import Coin
from unlucky import Unlucky
from widgets import Button, Label

pygame.init()
(w, h) = (1000, 900)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Horror")
font = pygame.font.SysFont(None, 72)
font2 = pygame.font.SysFont(None, 20)

t = list()
for i in range(10):
    t.append(i)
random.shuffle(t)

tile_no = 0
background, bg_image = get_background(tilemaps.tilemaps[t[tile_no]])
rects = []
for tile in background:
    rects.append(pygame.Rect(*tile, *bg_image.get_rect()[2:]))

clock = pygame.Clock()


dir = 0
dir_ghosts = [1, 1]
rand_legal = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
no_animation = 0

pygame.display.set_icon(pygame.image.load("icon.png"))

wheel = Wheel(screen, "chooser.png")
coins = []
for i in range(5):
    coins.append(Coin(screen, tilemaps.tilemaps[t[tile_no]], "coin.png"))
    coins_left = 5

main_menu_button = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font2, "Menu", (183, 183, 183), 50, 0, 100, 50)
collected_label = Label(screen, font2, "Coins Collected: " + str(5 - coins_left), (255, 0, 0), 100, 850, 100, 10)

t0 = time.time()
t0_1 = [time.time(), time.time(), time.time(), time.time(), time.time(), time.time(), time.time(), time.time(), time.time()]
t0_2 = time.time()

game_over = False

ghost_data = {
    "forward": [6, 0],
    "left": [6, 1],
    "right": [6, 2],
    "away": [6, 3],
    "dimensions": [48, 48],
    "scale": [64, 64],
    "offset": [10, 5]
}

sprite_data = {
    "forward": [8, 0],
    "right": [8, 1],
    "left": [8, 2],
    "away": [8, 3],
    "dimensions": [77, 77],
    "scale": [64, 64],
    "offset": [20, 10]
}
sprite = SpriteSheet(screen, 64, 64, clock, pygame.image.load("sprite.png"), sprite_data, rects, (200, 50, 50))
sprite.animate("forward")

def play():
    global game_over, t0, t0_1, t0_2, dir, dir_ghosts, rand_legal, no_animation, main_menu_button, collected_label, wheel, coin, coins, clock, tile_no, bg_image, background, coins_left, ghost_data, sprite_data, sprite

    sfx.play(sfx.level)
    running = True
    gameover_played = 0

    rects = []
    for tile in background:
        rects.append(pygame.Rect(*tile, *bg_image.get_rect()[2:]))

    ghost_no = 2
    ghosts = list()
    for i in range(ghost_no):
        a = random.randint(1, 15)
        b = random.randint(1, 13)
        while tilemaps.tilemaps[t[tile_no]][a - 1][b - 1] != 0 and (a > 10 or b > 10) and a != sprite.x // 64 and b != sprite.x // 64:
            a = random.randint(1, 15)
            b = random.randint(1, 13)
        ghosts.append(SpriteSheet(screen, a*64, b*64, clock, pygame.image.load("ghost.png"), ghost_data, rects, (200, 200, 200)))
    
    while running:
        dt = clock.tick(60)
        pos = pygame.mouse.get_pos()

        coins_left = (2*tile_no) + 5
        for coin in coins:
            if coin.destroy:
                coins_left -= 1
        if coins_left == 0:
            tile_no += 1
            try:
                background, bg_image = get_background(tilemaps.tilemaps[t[tile_no]])
            except IndexError:
                print("Congrats!! You finished the Game!!")
                running = False
                return 100
            ghost_no += 1
            sfx.play(sfx.level)
            rects = []
            for tile in background:
                rects.append(pygame.Rect(*tile, *bg_image.get_rect()[2:]))
            ghosts = []
            sprite = []
            dir_ghosts = []
            rand_legal = []
            for i in range(ghost_no):
                a = random.randint(1, 15)
                b = random.randint(1, 13)
                while tilemaps.tilemaps[t[tile_no]][a - 1][b - 1] != 0 and (a > 7 or b > 7):
                    a = random.randint(1, 15)
                    b = random.randint(1, 13)
                ghosts.append(SpriteSheet(screen, a*64, b*64, clock, pygame.image.load("ghost.png"), ghost_data, rects, (200, 200, 200)))
                dir_ghosts.append(1)
                rand_legal.append(([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]))
            sprite = SpriteSheet(screen, 64, 64, clock, pygame.image.load("sprite.png"), sprite_data, rects, (200, 50, 50))
            for i in range(5):
                coins.append(Coin(screen, tilemaps.tilemaps[t[tile_no]], "coin.png"))
                coins[i].destroy = False
        collected_label.text = "Coins Collected: " + str((2*tile_no) + 5 - coins_left)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit(0)
            if main_menu_button.handle_event(event, pos):
                running = False
                return 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dir = 2
                if event.key == pygame.K_RIGHT:
                    dir = 1
                if event.key == pygame.K_UP:
                    dir = 4
                if event.key == pygame.K_DOWN:
                    dir = 3
                if event.key == pygame.K_x:
                    sprite.collect(coins)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    dir = 0
                if event.key == pygame.K_r:
                    wheel.turn()

        t1 = time.time()

        for i in range(len(ghosts)):
            if t1 - t0_1[i] > 1:
                # Low weighted directions
                rand_legal[i] = [1, 2, 3, 4]
                # High weighted directions
                if ghosts[i].x - sprite.x > 0:
                    rand_legal[i].append(2)
                    rand_legal[i].append(2)
                    rand_legal[i].append(2)
                elif ghosts[i].x - sprite.x < 0:
                    rand_legal[i].append(1)
                    rand_legal[i].append(1)
                    rand_legal[i].append(1)

                if ghosts[i].y - sprite.y > 0:
                    rand_legal[i].append(4)
                    rand_legal[i].append(4)
                    rand_legal[i].append(4)
                elif ghosts[i].y - sprite.y < 0:
                    rand_legal[i].append(3)
                    rand_legal[i].append(3)
                    rand_legal[i].append(3)

                try:
                    dir_ghosts[i] = random.choice(rand_legal[i])
                except IndexError:
                    game_over = True

                t0_1[i] = time.time()

        for i in range(len(ghosts)):
            if ghosts[i].rect.colliderect(sprite.rect):
                ghosts[i].x = sprite.x
                ghosts[i].y = sprite.y
                game_over = True

        if not game_over:
            sprite.move(dir, dt, sound=True)
            for i in range(len(ghosts)):
                ghosts[i].move(dir_ghosts[i], dt)
                if ghosts[i].collision:
                    t0_1[i] = 0

        screen.fill((0, 0, 0))

        for tile in background:
            screen.blit(bg_image, tile)

        t1 = time.time()

        if t1 - t0 > 0.07:
            if dir == 3:
                sprite.animate("forward")
            elif dir == 2:
                sprite.animate("right")
            elif dir == 1:
                sprite.animate("left")
            elif dir == 4:
                sprite.animate("away")
            else:
                sprite.single(0, 0)

            for i in range(len(ghosts)):
                if dir_ghosts[i] == 3:
                    ghosts[i].animate("forward")
                elif dir_ghosts[i] == 1:
                    ghosts[i].animate("right")
                elif dir_ghosts[i] == 2:
                    ghosts[i].animate("left")
                elif dir_ghosts[i] == 4:
                    ghosts[i].animate("away")
                else:
                    ghosts[i].single(0, 0)

            t0 = time.time()

        if not game_over:
            t1 = time.time()
            if 1 < t1 - t0_2 <= 4:
                pass
            elif t1 - t0_2 > 4:
                t0_2 = time.time()
            else:
                for i in range(len(ghosts)): ghosts[i].render()
        else:
            for i in range(len(ghosts)): ghosts[i].render()

        sprite.render()
        wheel.render()

        main_menu_button.render()
        collected_label.render()

        for coin in coins:
            coin.render()

        if game_over:
            if gameover_played < 5:
                sfx.play(sfx.gameover)
                gameover_played += 1
            size = font.size("Game Over!!!")
            screen.blit(font.render("Game over!!!", True, (100, 0, 0)),
                        (random.randint(-1, 1) + (w / 2) - (size[0] / 2), random.randint(-1, 1) + (h / 2) - (size[1] / 2)))

        pygame.display.update()
