import os
import pygame
import weapon

WIDTH = 500
HEIGHT = 500
game_folder = os.path.dirname(__file__)

class Player(pygame.sprite.Sprite):
    
    def __init__(self, *groups):
        super().__init__(*groups)
        self.groups = groups
        self.fireballs = pygame.sprite.Group()
        self.image = pygame.image.load(
            os.path.join(game_folder, 'images/hero.png'))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2 # 250 -
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
    
    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.speedx = -8
            if event.key == pygame.K_RIGHT:
                self.speedx = 8
            if event.key == pygame.K_SPACE:
                self.shoot()
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT:
                self.speedx = 0
            if event.key == pygame.K_RIGHT:
                self.speedx = 0
    
    def update(self, *args, **kwargs):
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        self.rect.x += self.speedx
        # self.speedx = 0
    
    def shoot(self):
        fireball = weapon.Fireball(self.rect.centerx, self.rect.top, *self.groups)
        self.fireballs.add(fireball)