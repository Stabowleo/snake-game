import pygame
import random


class BodyPiece(pygame.sprite.Sprite):

    def __init__(self, texture, position: tuple):
        super().__init__()
        self.image = pygame.image.load(texture).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = position


class Apple(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("art/APPLE.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = [random.randrange(10, 470), random.randrange(10, 470)]