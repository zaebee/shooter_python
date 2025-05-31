import os
import random
import pygame

import player
import enemy
import splash
import explosion

# TODO: destroy enemy and show explosion when laser is collided with enemy.


class Game:
    FPS = 60
    WIDTH = 800
    HEIGHT = 800
    RUNNING = True
    IMAGES = os.path.join(os.path.dirname(__file__), "images")
    SOUNDS = os.path.join(os.path.dirname(__file__), "sounds")

    def __init__(self):
        pygame.init()
        self._caption = "Space shooter"
        self._clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.background = pygame.image.load(os.path.join(self.IMAGES, "kosmos.png"))

        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.hero = player.Player(self.all_sprites)
        # Added boss
        enemy.Boss(self.all_sprites, self.enemies)
        # Added enemies
        for _ in range(5):
            enemy.Enemy(self.all_sprites, self.enemies)

    def check_collision(self):
        enemy_collided = pygame.sprite.spritecollideany(self.hero, self.enemies)
        if enemy_collided:
            enemy_collided.kill()
            explosion.Explosion(
                self.hero.rect.centerx, self.hero.rect.centery, self.all_sprites
            )
        for laser in self.hero.fireballs:
            # TODO: destroy enemy when collided with laser -> create explosion.
            enemy_collided = pygame.sprite.spritecollideany(
                laser, self.enemies)
            if enemy_collided:
                enemy_collided.kill()
                laser.kill()
                explosion.Explosion(
                    enemy_collided.rect.centerx,
                    enemy_collided.rect.centery,
                    self.all_sprites)
    
    def start(self):
        """Starts game cycle."""
        while self.RUNNING:
            self.screen.blit(self.background, self.background.get_rect())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False
                self.hero.on_event(event)

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            
            self.check_collision()
            
            splash.load_health(self.screen, self.hero.health)
            splash.load_score(self.screen, self.hero.score)
            
            pygame.display.flip()
            self._clock.tick(self.FPS)


game = Game()
splash.load_menu(game.screen)
game.start()
