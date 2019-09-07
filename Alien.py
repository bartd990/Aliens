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
            self.rect.right = self.SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.x_velocity, 0)
        if not self.SCREENRECT.contains(self.rect):
            self.x_velocity = -self.x_velocity
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(self.SCREENRECT)
        self.frame = self.frame + 1
        self.image = self.images[self.frame//self.animation_cycle % 3]
        