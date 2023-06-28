import pygame
from widgets import *


def instructions():
    pygame.init()
    screen = pygame.display.set_mode((1000, 900))
    font = pygame.font.SysFont(None, 30)

    main_menu_button = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "Menu", (183, 183, 183), 5, 5, 100, 50)
    inst = [
        Label(screen, pygame.font.SysFont(None, 100), "Instructions", (200, 100, 100), 450, 200, 100, 50),
        Label(screen, font, "Escape from the ghosts and collect coins to go to the next level (of which there are 13)", (183, 183, 183), 450, 300, 100, 50),
        Label(screen, font, "right arrow key to move right", (183, 183, 183), 450, 400, 100, 50),
        Label(screen, font, "left arrow key to move left", (183, 183, 183), 450, 450, 100, 50),
        Label(screen, font, "up arrow key to move up", (183, 183, 183), 450, 500, 100, 50),
        Label(screen, font, "down arrow key to move down", (183, 183, 183), 450, 550, 100, 50),
        Label(screen, font, "space key to collect coins", (183, 183, 183), 450, 600, 100, 50),
    ]

    while True:
        event = pygame.event.wait()
        pos = pygame.mouse.get_pos()
        if main_menu_button.handle_event(event, pos):
            break
        if event.type == pygame.QUIT:
            break

        screen.fill((36, 34, 30))
        main_menu_button.render()
        for i in inst:
            i.render()
        pygame.display.update()

