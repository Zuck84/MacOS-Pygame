import pygame
import tkinter
import os

#cd OneDrive\Documents\MacOS_Pygame

pygame.init()
white = (255, 255, 255)
window_resolution = (1280, 657)

programIcon = pygame.image.load("logo.png")
pygame.display.set_icon(programIcon)

window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)

pygame.display.set_caption("MacOS PYGAME by Charles SOKOL")

FINDER = pygame.image.load("Finder.jpg").convert()
SAFARI = pygame.image.load("Safari.png").convert()
WHATSAPP = pygame.image.load("Whatsapp.png").convert()
SETTINGS = pygame.image.load("Settings.jpg").convert()
TERMINAL = pygame.image.load("Terminal.jpg").convert()
STOCKS = pygame.image.load("Stocks.jpg").convert()

xF = 300
xSA = 400
xW = 500
XSE = 600
XT = 700
xST = 800
y = 625

window_surface.blit(FINDER, (xF, y))
window_surface.blit(SAFARI, (xSA, y))
window_surface.blit(WHATSAPP, (xW, y))
window_surface.blit(SETTINGS, (xW, y))
window_surface.blit(TERMINAL, (xW, y))
window_surface.blit(STOCKS, (xST, y))
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
        window_surface.blit(SAFARI, [400, 625])
        window_surface.blit(WHATSAPP, [500, 625])
        window_surface.blit(SETTINGS, [600, 625])
        window_surface.blit(TERMINAL, [700, 625])
        window_surface.blit(STOCKS, [800, 625])
        pygame.display.flip()
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos >= (299, 624) and event.pos <= (325, 650):
                print("Opening the Finder...")
                os.system("python finder.py")
            elif event.pos >= (399, 624) and event.pos <= (425, 650):
                print("Opening Safari...")
                os.system("start www.google.com")
            elif event.pos >= (499, 624) and event.pos <= (525, 650):
                print("Opening Whatsapp...")
                os.system("start https://web.whatsapp.com/")
            elif event.pos >= (599, 624) and event.pos <= (625, 650):
                print("Opening Settings...")
                os.system("python settings.py")
            elif event.pos >= (699, 624) and event.pos <= (725, 650):
                print("Opening the Jarvis Terminal...")
                os.system("cls")
                os.system("color a")
                print("Welcome to the JARVIS TERMINAL developed by Charles SOKOL in October 2019")
                os.system("python jarvis.py")
            elif event.pos >= (799, 624) and event.pos <= (825, 650):
                print("Opening Stocks...")
                os.system("python eco.py")

        elif event.type == pygame.MOUSEMOTION:
            print("{}".format(event.pos))
