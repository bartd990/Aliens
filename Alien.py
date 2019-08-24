import pygame
from pygame.locals import *
import random
class Alien(pygame.sprite.Sprite):
    speed = 13
    animation_cycle = 12
    images = []

    def _init_(self, screen_rectangle):
        pygame.sprite.Sprite._init_(self,self.containers)
        self.SCREENRECT = screen_rectangle
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        