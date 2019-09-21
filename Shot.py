import pygame
class Shot(pygame.sprite.Sprite):
    y_velocity = -11
    images = []

    def _init_(self, tank):
        pygame.sprite.Sprite._init_(self,self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=tank)
    def update(self):
        self.rect.move_ip(0, self.y_velocity)
        if self.rect.top <= 0:
            self.kill()