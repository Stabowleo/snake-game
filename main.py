import pygame
from pygame.locals import *
from sprites import *


def main():
    screen = pygame.display.set_mode((480, 480))
    pygame.display.set_caption("Snake")

    snake = pygame.sprite.Group(BodyPiece("art/SnakeHead.png"))

    while True:
        snake.draw(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        pygame.display.flip()


if __name__ == "__main__":
    main()
