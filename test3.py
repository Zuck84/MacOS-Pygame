import pygame

pygame.init()
window_resolution = (1280, 657)
white = (255, 255, 255)
screen = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)

pygame.display.set_caption('clicked on image')
FINDER = pygame.image.load("Finder.jpg").convert()

x = 1000
y = 500
screen.blit(FINDER, (x,y)) # paint to screen
pygame.display.flip() # paint screen one time

running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x = 1000
            y = 500
            x, y = event.pos
            if FINDER.get_rect().collidepoint(x, y):
                print('clicked on image')
#loop over, quit pygame
pygame.quit()
