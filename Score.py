import pygame
from pygame.locals import Color
class Score(pygame.sprite.Sprite):
    score_points = 0
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        self.font = pygame.font.Font(None, 48)
        self.font.set_italic(1)
        self.color = Color("White")
        self.last_score = -1
        self.update()
        self.rect = self.image.get_rect().move(20,5)
    def update(self):
        if (self.score_points != self.last_score):
            self.last_score = self.score_points
            msg = "Score: %d" % self.score_points
            self.image = self.font.render(msg, 0, self.color)
            