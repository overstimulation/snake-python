import random
import sys

import pygame
from pygame.math import Vector2


class Fruit:
    def __init__(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.position = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            int(self.position.x * CELL_SIZE),
            int(self.position.y * CELL_SIZE),
            CELL_SIZE,
            CELL_SIZE,
        )
        pygame.draw.rect(screen, pygame.Color("red"), fruit_rect)


FPS = 60
CELL_SIZE = 40
CELL_NUMBER = 20

pygame.init()
screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
clock = pygame.time.Clock()

fruit = Fruit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175, 215, 70))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(FPS)
