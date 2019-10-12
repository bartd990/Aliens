import pygame
from pygame.locals import Color
class PlayerLives(pygame.sprite.Sprite):
    lives = 3
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font
        self.font.set_bold(1)
        self.color = Color("red")
        self.last_lives = -1
        self.update()
        self.rect = self.image.get_rect().move(850, 5)
    def update(self):
        if self.lives != self.last_lives:
            self.last_lives = self.lives
            