import pygame

pygame.mixer.init()

# https://www.chess.com capture sfx
walk = pygame.mixer.Sound("walk.mp3")
# jsfxr
collect = pygame.mixer.Sound("coin.wav")
level = pygame.mixer.Sound("level.wav")
gameover = pygame.mixer.Sound("gameover.wav")

sfx_on = True
bgm_on = True

def bgm():
    # Conjuring 2 bgm https://www.youtube.com/watch?v=O9FNI5Kn9sI
    pygame.mixer.music.load("bgm.mp3")
    pygame.mixer.music.play(-1)


def play(sound):
    global sfx_on
    if sfx_on:
        pygame.mixer.Sound.play(sound)


def stop():
    global bgm_on
    bgm_on = False
    pygame.mixer.music.stop()
