import random
import sys

import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = RIGHT
        self.can_grow = False

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

    def move_snake(self):
        if self.can_grow is True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.can_grow = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def grow(self):
        self.can_grow = True


class Fruit:
    def __init__(self):
        self.randomise_position()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            int(self.position.x * CELL_SIZE),
            int(self.position.y * CELL_SIZE),
            CELL_SIZE,
            CELL_SIZE,
        )
        screen.blit(apple, fruit_rect)

    def randomise_position(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.position = Vector2(self.x, self.y)


class SnakeGame:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()

    def check_collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomise_position()
            self.snake.grow()

    def check_fail(self):
        if (
            not 0 <= self.snake.body[0].x < CELL_NUMBER
            or not 0 <= self.snake.body[0].y < CELL_NUMBER
        ):
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()


FPS = 60
CELL_SIZE = 40
CELL_NUMBER = 20

UP = Vector2(0, -1)
DOWN = Vector2(0, 1)
LEFT = Vector2(-1, 0)
RIGHT = Vector2(1, 0)

pygame.init()
screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
clock = pygame.time.Clock()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

apple = pygame.image.load("textures/apple.png").convert_alpha()

snake_game = SnakeGame()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_game.snake.direction != DOWN:
                snake_game.snake.direction = UP
            if event.key == pygame.K_DOWN and snake_game.snake.direction != UP:
                snake_game.snake.direction = DOWN
            if event.key == pygame.K_LEFT and snake_game.snake.direction != RIGHT:
                snake_game.snake.direction = LEFT
            if event.key == pygame.K_RIGHT and snake_game.snake.direction != LEFT:
                snake_game.snake.direction = RIGHT

    screen.fill((175, 215, 70))
    snake_game.draw_elements()
    pygame.display.update()
    clock.tick(FPS)
