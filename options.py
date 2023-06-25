import pygame
import sfx

from widgets import *


def options():
    pygame.init()
    screen = pygame.display.set_mode((1000, 900))
    font = pygame.font.SysFont(None, 30)

    main_menu_button = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "Menu", (183, 183, 183), 50, 0, 100, 50)
    opts_l = [
        Label(screen, pygame.font.SysFont(None, 100), "Options", (200, 100, 100), 450, 200, 100, 50),
        Label(screen, font, "Background Music: ", (183, 183, 183), 450, 300, 100, 50),
        Label(screen, font, "SFX: ", (183, 183, 183), 450, 400, 100, 50),
    ]

    bgm_b = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "On", (183, 183, 183), 600, 300, 100, 50)
    sfx_b = Button(screen, (180, 20, 10), (180, 80, 10), (10, 75, 20), font, "On", (183, 183, 183), 600, 400, 100, 50)
    if not sfx.bgm_on:
        bgm_b.text = "Off"
    if not sfx.sfx_on:
        sfx_b.text = "Off"

    while True:
        event = pygame.event.wait()
        pos = pygame.mouse.get_pos()
        if main_menu_button.handle_event(event, pos):
            break
        if event.type == pygame.QUIT:
            break
        if bgm_b.handle_event(event, pos):
            if bgm_b.text == "On":
                bgm_b.text = "Off"
                sfx.stop()
            elif bgm_b.text == "Off":
                bgm_b.text = "On"
                sfx.bgm()
        if sfx_b.handle_event(event, pos):
            if sfx_b.text == "On":
                sfx_b.text = "Off"
                sfx.sfx_on = False
            elif sfx_b.text == "Off":
                sfx_b.text = "On"
                sfx.sfx_on = True


        screen.fill((36, 34, 30))
        main_menu_button.render()
        for i in opts_l:
            i.render()
        bgm_b.render()
        sfx_b.render()
        pygame.display.update()




