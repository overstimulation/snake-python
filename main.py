import sys

import pygame

FPS = 60
CELL_SIZE = 40
CELL_NUMBER = 20

pygame.init()
screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175, 215, 70))
    pygame.display.update()
    clock.tick(FPS)
