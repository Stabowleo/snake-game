from turtle import position
import pygame
from pygame.locals import *
from sprites import *


def main():
    fpsclock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((480, 480))
    pygame.display.set_caption("Snake")
    position = (30, 30)

    snake = pygame.sprite.Group(BodyPiece("art/SnakeHead.png", position))
    apple = pygame.sprite.GroupSingle(Apple())
    apple.draw(screen)
    snake.draw(screen)
    velocity = (0, 0)

    while True:
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                   velocity = (10, 0)
                if event.key == pygame.K_s:
                    velocity = (0, 10)
                if event.key == pygame.K_a:
                    velocity = (-10, 0)
                if event.key == pygame.K_w:
                    velocity = (0, -10)

   
        dt = fpsclock.tick(30)
        snake.draw(screen)
        snake.update(velocity, dt)

        


if __name__ == "__main__":
    main()
