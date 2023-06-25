import pygame
from widgets import *


def instructions():
    pygame.init()
    screen = pygame.display.set_mode((1000, 900))
    font = pygame.font.SysFont(None, 20)

    main_menu_button = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "Menu", (183, 183, 183), 50, 0, 100, 50)
    inst = [
        Label(screen, pygame.font.SysFont(None, 50), "Instructions", (200, 100, 100), 150, 200, 100, 50),
        Label(screen, font, "Escape from the ghosts and collect coins to go to the next level", (183, 183, 183), 150, 300, 100, 50),
        Label(screen, font, "-> to move right", (183, 183, 183), 150, 400, 100, 50),
        Label(screen, font, "<- to move left", (183, 183, 183), 150, 450, 100, 50),
        Label(screen, font, "up arrow to move up", (183, 183, 183), 150, 500, 100, 50),
        Label(screen, font, "down arrow to move down", (183, 183, 183), 150, 550, 100, 50),
        Label(screen, font, "x to collect coins", (183, 183, 183), 150, 600, 100, 50),
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

