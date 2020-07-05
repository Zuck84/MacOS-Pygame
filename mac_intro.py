import pygame

pygame.init()
window_resolution = (1280, 657)

programIcon = pygame.image.load("logo.png")
pygame.display.set_icon(programIcon)

#Colors
white = (255, 255, 255)
black = (0, 0, 0)

pygame.display.set_caption("Welcome to MacOS PYGAME developed by Charles SOKOL")
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)


pygame.mixer.music.load("boot-sound.ogg")
pygame.mixer.music.play()

macos_picture = pygame.image.load("intro0.jpg")
macos_picture.convert()
macos_picture.set_colorkey(black)

macos_picture1 = pygame.image.load("intro1.jpg")
macos_picture1.convert()
macos_picture1.set_colorkey(black)

macos_picture2 = pygame.image.load("intro2.jpg")
macos_picture2.convert()
macos_picture2.set_colorkey(black)

macos_picture3 = pygame.image.load("intro3.jpg")
macos_picture3.set_colorkey(black)
macos_picture3.convert()

pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False


    window_surface.fill(black)
    window_surface.blit(macos_picture, [310, 90])
    pygame.display.flip()

    launch = 500

    pygame.time.wait(launch)

    window_surface.fill(black)
    window_surface.blit(macos_picture1, [310, 90])
    pygame.display.flip()

    pygame.time.wait(launch)


    window_surface.fill(black)
    window_surface.blit(macos_picture2, [310, 90])
    pygame.display.flip()

    pygame.time.wait(launch)

    window_surface.fill(black)
    window_surface.blit(macos_picture3, [310, 90])
    pygame.display.flip()

    pygame.time.wait(1000)
    quit()
