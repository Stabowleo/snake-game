import random
from tkinter.tix import Tree
from aiohttp import TraceRequestChunkSentParams
import pygame
from pygame.locals import *
pygame.init()

green = (0, 255, 0)
red = (255, 0, 0)


class Snake:

    def __init__(self) -> None:
        self.size = 30
        self.speed = 10   
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2
        self.x_change = 0
        self.y_change = 0
        self.head = [self.x, self.y]
        self.snake_list = [self.head]
        self.length = 1

    def draw_snake(self):
        for x in self.snake_list:
            pygame.draw.rect(screen, green, [x[0], x[1], self.size, self.size])
            


class Food:

    def __init__(self) -> None:
        self.x = round(random.randrange(0, screen.get_width() - Snake().size) / 30) * 30
        self.y = round(random.randrange(0, screen.get_height() - Snake().size) / 30) * 30

    def draw_food(self):
        pygame.draw.rect(screen, red, [self.x, self.y, 30, 30])

    def move(self):
        self.x = round(random.randrange(0, screen.get_width() - Snake().size) / 30) * 30
        self.y = round(random.randrange(0, screen.get_height() - Snake().size) / 30) * 30


clock = pygame.time.Clock()
screen = pygame.display.set_mode((480, 480))
pygame.display.set_caption("Snake Game")
snake = Snake()
food = Food()



def main():
    game_over = False

    while not game_over:


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snake.x_change = 0
                    snake.y_change = -snake.size
                elif event.key == pygame.K_a:
                    snake.x_change = -snake.size
                    snake.y_change = 0
                elif event.key == pygame.K_s:
                    snake.x_change = 0
                    snake.y_change = snake.size
                elif event.key == pygame.K_d:
                    snake.x_change = snake.size
                    snake.y_change = 0

        if snake.x >= screen.get_width() or snake.x < 0 or snake.y >= screen.get_height() or snake.y < 0:
            game_over = TraceRequestChunkSentParams

        snake.x += snake.x_change
        snake.y += snake.y_change
        screen.fill((0, 0, 0))
        food.draw_food()
        snake.head = [snake.x, snake.y]
        snake.snake_list.append(snake.head)
        
        if len(snake.snake_list) > snake.length:
            del snake.snake_list[0]
        

        for x in snake.snake_list[:-1]:
            if x == snake.head:
                game_over = True

        
        snake.draw_snake()
        pygame.display.update()


        if snake.x == food.x and snake.y == food.y:
            food.move()
            snake.length += 1

        clock.tick(snake.speed)




if __name__ == "__main__":
    main()