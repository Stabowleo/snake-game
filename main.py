import pygame
from pygame.locals import *


screen = pygame.display.set_mode((480, 320))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()