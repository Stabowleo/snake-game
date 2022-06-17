import pygame
from pygame.locals import *
from sprites import *


def main():
    fpsclock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((480, 480))
    background = pygame.Surface(pygame.display.get_window_size())
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

        for sprite in snake.sprites():

            if pygame.sprite.collide_rect(sprite, apple.sprite):
                apple.clear(screen, background)
                apple.empty()
                apple.add(Apple())

                last_part = snake.sprites()[len(snake.sprites()) -1]
                new_part_position = (last_part.update(True)[0] - last_part.update(False, True)[0],
                                     last_part.update(True)[1] - last_part.update(False, True)[1])
                snake.add(BodyPiece("art/SnakeBody.png", new_part_position))
   

        dt = fpsclock.tick(30)
        snake.clear(screen, background)
        snake.draw(screen)
        apple.draw(screen)
        snake.update(False, False, velocity, dt)



if __name__ == "__main__":
    main()
