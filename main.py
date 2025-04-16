import random
import sys

import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]

    def draw_snake(self):
        for block in self.body:
            x_position = int(block.x * CELL_SIZE)
            y_position = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(
                x_position,
                y_position,
                CELL_SIZE,
                CELL_SIZE,
            )
            pygame.draw.rect(screen, pygame.Color("blue"), block_rect)


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
snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175, 215, 70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(FPS)
