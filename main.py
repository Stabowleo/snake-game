import pygame
from pygame.locals import *
from sprites import *


def main():
    screen = pygame.display.set_mode((480, 480))
    pygame.display.set_caption("Snake")

    snake = pygame.sprite.Group(BodyPiece("art/SnakeHead.png", (100, 100)))
    apple = pygame.sprite.Group(Apple())
    apple.draw(screen)

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    snake.add(BodyPiece("art/SnakeBody.png", (100, 130)))


        snake.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
