import os
import random
import pygame

WIDTH = 500
HEIGHT = 500
game_folder = os.path.dirname(__file__)

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, *groups):
        super().__init__(*groups)
        self.groups = groups
        self.image = pygame.image.load(
            os.path.join(game_folder, 'images/enemy.png'))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 500)
        self.rect.y = random.randrange(0, 50)
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(1, 5)
        
    def update(self, *args, **kwargs):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)