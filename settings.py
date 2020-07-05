import pygame
import os

pygame.init()

white = (255, 255, 255)
my_blue = (46, 112, 161)

window_resolution = (640, 480)

programIcon = pygame.image.load("Settings.png")
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption("SETTINGS")

arial_font = pygame.font.SysFont("arial", 10)
big_arial_font = pygame.font.SysFont("arial", 30)

settings_text_surface = big_arial_font.render("SETTINGS OF MACOS PYGAME", True, my_blue)

CONTROL = pygame.image.load("CONTROL.jpg").convert()
control_text_surface = arial_font.render("Control Panel", True, my_blue)

KEYBOARD = pygame.image.load("KEYBOARD.png").convert()
keyboard_text_surface = arial_font.render("Keyboard", True, my_blue)

MOUSE = pygame.image.load("MOUSE.jpg").convert()
mouse_text_surface = arial_font.render("Mouse", True, my_blue)

PRINTERS = pygame.image.load("PRINTERS.jpg").convert()
printers_text_surface = arial_font.render("Printers", True, my_blue)

ADMINTOOLS = pygame.image.load("ADMIN.jpg").convert()
admin_text_surface = arial_font.render("Admin Tools", True, my_blue)

window_surface.blit(CONTROL, (0, 0))

launched = True
while launched:
    for event in pygame.event.get():
        window_surface.fill(white)

        window_surface.blit(CONTROL, [105, 5])
        window_surface.blit(control_text_surface, (118, 55))

        window_surface.blit(KEYBOARD, [220, -5])
        window_surface.blit(keyboard_text_surface, (228, 55))

        window_surface.blit(MOUSE, [300, -5])
        window_surface.blit(mouse_text_surface, (318, 60))

        window_surface.blit(PRINTERS, [360, -15])
        window_surface.blit(printers_text_surface, (400, 60))

        window_surface.blit(ADMINTOOLS, [465, -5])
        window_surface.blit(admin_text_surface, (480, 63))

        window_surface.blit(settings_text_surface, (100, 250))
        pygame.display.flip()
        if event.type == pygame.QUIT:
            launched = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos >= (105, 5) and event.pos <= (190, 52):
                print("Opening the Control Panel")
                os.system("control")

            elif event.pos >= (220, 10) and event.pos <= (285, 50):
                print("Opening the Keyboard Settings")
                os.system("control keyboard")

            elif event.pos >= (320, 0) and event.pos <= (342, 54):
                print("Opening the Mouse Settings")
                os.system("control mouse")

            elif event.pos >= (382, 0) and event.pos <= (445, 56):
                print("Opening the Printers Settings")
                os.system("control printers")

            elif event.pos >= (475, 1) and event.pos <= (545, 60):
                print("Opening the Administrator Tools")
                os.system("control admintools")

        elif event.type == pygame.MOUSEMOTION:
            print("{}".format(event.pos))
