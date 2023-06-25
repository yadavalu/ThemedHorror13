import pygame

pygame.mixer.init()

# https://www.chess.com capture sfx
walk = pygame.mixer.Sound("walk.mp3")
# jsfxr
collect = pygame.mixer.Sound("coin.wav")
level = pygame.mixer.Sound("level.wav")
gameover = pygame.mixer.Sound("gameover.wav")

def bgm():
    # Conjuring 2 bgm https://www.youtube.com/watch?v=O9FNI5Kn9sI
    pygame.mixer.music.load("bgm.mp3")
    pygame.mixer.music.play(-1)


def play(sound):
    pygame.mixer.Sound.play(sound)


def stop():
    pygame.mixer.music.stop()
