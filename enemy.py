import os
import random
import pygame

import animator
import config

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, *groups, **kwargs):
        super().__init__(*groups)
        self.groups = groups # type: ignore
        self.max_health = 3
        self.health = 3
        self.filename = kwargs.get('filename', 'any.png')
        # self._load_image('images/alien_small.png')
        self._load_image(f'images/{self.filename}')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 500)
        self.rect.y = random.randrange(0, 50)
        self.speedx = random.randrange(-4, 4) or -1
        self.speedy = random.randrange(2, 4)
        
    def _load_image(self, name):
        self.image = pygame.image.load(os.path.join(config.game_folder, name))
        
    def update(self, *args, **kwargs):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (self.rect.top > config.HEIGHT + 10 or 
            self.rect.left < -25 or self.rect.right > config.WIDTH + 20):
            self.rect.x = random.randrange(config.WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedx = random.randrange(-4, 4)
                    
    def take_damage(self):
        self.health -= 1
        self._load_image('images/alien_small.png')
        self.speedy = random.randrange(5, 10)
        if self.health == 0:
            self.kill()
            
    def is_dead(self):
        return self.health <= 0
            

class Boss(Enemy):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frames = animator.load_sprite_sheet(
            os.path.join(config.game_folder, 'images', 'egg.png'), 128, 160)
        self.current_frame = 0
        self.last_update = 0
        self.animation_speed = 100 # milliseconds
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 50
        
    def update(self, *args, **kwargs):
        current_time = pygame.time.get_ticks()
        self.rect.x += self.speedx
        if current_time - self.last_update > self.animation_speed:
            self.last_update = current_time
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            if self.current_frame + 1 >= len(self.frames):
                pass # self.kill()