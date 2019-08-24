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
        self.direction_factor = random.choice((-1, 1))
        self.x_velocity = self. direction_factor * self.speed
        self.frame = 0
        if self.x_velocity < 0:
            