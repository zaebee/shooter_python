import os
import pygame

game_folder = os.path.dirname(__file__)

class Bullet(pygame.sprite.Sprite):
    skin: str = 'laser.png'
    
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.speedy = -10
        self.angle = 30
        self.pos = pygame.math.Vector2(x, y)
        self.image = pygame.image.load(
            os.path.join(game_folder, f'images/{self.skin}'))
        self.rect = self.image.get_rect(center=self.pos)
        self.rect.centerx = x
        self.rect.bottom = y
        self.velocity = self.pos.rotate(self.angle)
        
    def update(self, *args, **kwargs):
        self.rect.y += self.speedy