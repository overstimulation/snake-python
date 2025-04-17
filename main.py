import random
import sys

import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = RIGHT
        self.can_grow = False

        self.head_up = pygame.image.load("textures/head_up.png").convert_alpha()
        self.head_down = pygame.image.load("textures/head_down.png").convert_alpha()
        self.head_left = pygame.image.load("textures/head_left.png").convert_alpha()
        self.head_right = pygame.image.load("textures/head_right.png").convert_alpha()

        self.tail_up = pygame.image.load("textures/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("textures/tail_down.png").convert_alpha()
        self.tail_left = pygame.image.load("textures/tail_left.png").convert_alpha()
        self.tail_right = pygame.image.load("textures/tail_right.png").convert_alpha()

        self.body_vertical = pygame.image.load("textures/body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load("textures/body_horizontal.png").convert_alpha()

        self.body_top_left = pygame.image.load("textures/body_top_left.png").convert_alpha()
        self.body_top_right = pygame.image.load("textures/body_top_right.png").convert_alpha()
        self.body_bottom_left = pygame.image.load("textures/body_bottom_left.png").convert_alpha()
        self.body_bottom_right = pygame.image.load("textures/body_bottom_right.png").convert_alpha()

    def draw_snake(self):
        self.update_head_texture()
        self.update_tail_texture()

        for index, block in enumerate(self.body):
            x_position = int(block.x * CELL_SIZE)
            y_position = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(
                x_position,
                y_position,
                CELL_SIZE,
                CELL_SIZE,
            )
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block

                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_top_left, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_top_right, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bottom_left, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_bottom_right, block_rect)

    def update_head_texture(self):
        head_direction = self.body[1] - self.body[0]

        if head_direction == UP:
            self.head = self.head_down
        elif head_direction == DOWN:
            self.head = self.head_up
        elif head_direction == LEFT:
            self.head = self.head_right
        elif head_direction == RIGHT:
            self.head = self.head_left

    def update_tail_texture(self):
        tail_direction = self.body[-2] - self.body[-1]
        if tail_direction == UP:
            self.tail = self.tail_down
        elif tail_direction == DOWN:
            self.tail = self.tail_up
        elif tail_direction == LEFT:
            self.tail = self.tail_right
        elif tail_direction == RIGHT:
            self.tail = self.tail_left

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
        self.apple_texture = pygame.image.load("textures/apple.png").convert_alpha()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            int(self.position.x * CELL_SIZE),
            int(self.position.y * CELL_SIZE),
            CELL_SIZE,
            CELL_SIZE,
        )
        screen.blit(self.apple_texture, fruit_rect)

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

    def draw_grass(self):
        grass_colour = (165, 210, 60)

        for row in range(CELL_NUMBER):
            if row % 2 == 0:
                for col in range(CELL_NUMBER):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, grass_colour, grass_rect)
            else:
                for col in range(CELL_NUMBER):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, grass_colour, grass_rect)

    def draw_elements(self):
        self.draw_grass()
        self.snake.draw_snake()
        self.fruit.draw_fruit()

    def check_collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomise_position()
            self.snake.grow()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < CELL_NUMBER or not 0 <= self.snake.body[0].y < CELL_NUMBER:
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
