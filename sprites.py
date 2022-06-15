import pygame


class BodyPiece(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("art/SnakeBody.png").convert_alpha()
        self.rect = self.image.get_rect()
