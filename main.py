import sys

import pygame

FPS = 60

pygame.init()
screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175, 215, 70))
    pygame.display.update()
    clock.tick(FPS)
