import pygame
import tkinter

pygame.init()
white = (255, 255, 255)
window_resolution = (1280, 657)

window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)

pygame.display.set_caption("MacOS PYGAME by Charles SOKOL")
FINDER = pygame.image.load("Finder.jpg").convert()

x = 300
y = 625
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
        window_surface.blit(FINDER, [300, 625])
        pygame.display.flip()
        if event.type == pygame.QUIT:
            launched = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos >= (299, 624) and event.pos <= (325, 650):
                print("DONE")


        elif event.type == pygame.MOUSEMOTION:
            print("{}".format(event.pos))
