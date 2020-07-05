import pygame
import tkinter

pygame.init()
white = (255, 255, 255)
window_resolution = (1280, 657)

pygame.display.set_caption("MacOS PYGAME by Charles SOKOL")
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)

FINDER = pygame.image.load("Finder.jpg").convert()
x = 0
y = 0
window_surface.blit(FINDER, (x,y))
pygame.display.flip()

background = pygame.image.load("wallpaper.png")
background.convert()
background.set_colorkey(white)

launched = True
while launched:
    for event in pygame.event.get():
        window_surface.fill(white)
        window_surface.blit(background, [-330, -200])
        window_surface.blit(FINDER, [0, 0])
        pygame.display.flip()
        if event.type == pygame.QUIT:
            launched = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if FINDER.get_rect().collidepoint(x, y):
                print('FINDER')
