import os
import pygame

import weapon

WIDTH = 800
HEIGHT = 800
game_folder = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    health: int = 10
    score: int = 0
    skin: str = "ship_orange.png"

    def __init__(self, *groups):
        super().__init__(*groups)
        self.groups = groups  # type: ignore
        self.fireballs = pygame.sprite.Group()
        self.image = pygame.image.load(os.path.join(game_folder, f"images/{self.skin}"))

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2  # type: ignore
        self.rect.bottom = HEIGHT - 50
        self.speedx = 0

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.speedx = -8
            if event.key == pygame.K_RIGHT:
                self.speedx = 8
            if event.key == pygame.K_SPACE:
                self.shoot()
        elif event.type == pygame.KEYUP:
            self.speedx = 0

    def update(self, *args, **kwargs):
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        self.rect.x += self.speedx

    def shoot(self):
        self.fireballs.add(
            weapon.Bullet(
                self.rect.centerx, self.rect.top, *self.groups  # type: ignore
            )
        )
