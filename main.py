import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
from frame import Frame

WITDH, HEIGHT = 1100, 900

screen = pygame.display.set_mode((WITDH,HEIGHT))

PCore = Frame(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    keys= pygame.key.get_pressed()
    x,y = pygame.mouse.get_pos()
    screen.fill((255,255,255))
    PCore.VelUpdate(x,y)

    pygame.time.wait(5)
    pygame.display.update()
