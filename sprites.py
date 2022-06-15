import pygame


class BodyPiece(pygame.sprite.Sprite):

    def __init__(self, texture):
        super().__init__()
        self.image = pygame.image.load(texture).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = [100, 100]
