import os
import pygame

game_folder = os.path.dirname(__file__)

class Fireball(pygame.sprite.Sprite):
    
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.speedy = -10
        self.angle = 30
        self.pos = pygame.math.Vector2(x, y)
        self.image = pygame.image.load(
            os.path.join(game_folder, 'images/fireball.png'))
        self.rect = self.image.get_rect(center=self.pos)
        self.rect.centerx = x
        self.rect.bottom = y
        self.velocity = self.pos.rotate(self.angle)
        
    def update(self, *args, **kwargs):
        screen = kwargs.get('screen')
        self.rect.y += self.speedy
        screen.blit(self.image, self.rect)