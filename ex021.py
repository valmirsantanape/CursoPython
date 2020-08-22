import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer_music.load('gtasound.mp3')
pygame.mixer_music.play()
pygame.event.wait()