import pygame
class Explosion(pygame.sprite.Sprite):
    default_life = 12
    animation_cycle = 3
    images = []

    def _init_(self, actor):
        pygame.sprite.Sprite._init_(self,self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.default_life
        
    def update(self):
        '''
            explosion will last 12 frames
        '''
        self.life = self.life - 1
        self.image = self.images[self.life//self.animation_cycle % 2]
        if (self.life <=0):
            self.kill()