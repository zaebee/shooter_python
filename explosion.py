import os
import pygame
import animator

game_folder = os.path.dirname(__file__)


class Explosion(pygame.sprite.Sprite):
    
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.frames = animator.load_sprite_sheet(
            os.path.join(game_folder, 'images', 'explosion.png'),
            96, 96)
        self.current_frame = 0
        self.last_update = 0
        self.animation_speed = 100 # milliseconds
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        
    def update(self, *args, **kwargs):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update > self.animation_speed:
            self.last_update = current_time
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            if self.current_frame + 1 >= len(self.frames):
                self.kill()