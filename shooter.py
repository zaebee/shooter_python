import os
import random
import pygame

import player
import enemy
import splash
import explosion


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
        # Added enemies
        self.spawn_enemies(5)
        self.score_timer = pygame.time.get_ticks()  # Initialize the timer

    def spawn_enemies(self, num = 5):
        for _ in range(num):
            enemy.Enemy(self.all_sprites, self.enemies)

    def check_collision(self):
        enemy_collided = pygame.sprite.spritecollideany(self.hero, self.enemies)
        if enemy_collided:
            self.hero.health -= 1
            enemy_collided.kill()
            enemy.Enemy(self.all_sprites, self.enemies)
            explosion.Explosion(
                self.hero.rect.centerx, self.hero.rect.centery, self.all_sprites
            )
        for laser in self.hero.fireballs:
            # TODO: destroy enemy when collided with laser -> create explosion.
            enemy_collided = pygame.sprite.spritecollideany(laser, self.enemies)
            if enemy_collided:
                self.hero.score += 1
                enemy_collided.kill()
                laser.kill()
                enemy.Enemy(self.all_sprites, self.enemies)
                explosion.Explosion(
                    enemy_collided.rect.centerx,
                    enemy_collided.rect.centery,
                    self.all_sprites,
                )

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

            # Increase score every 60 seconds
            time_now = pygame.time.get_ticks()
            if time_now - self.score_timer > 10000:  # 10000 milliseconds = 10 seconds
                enemy.Enemy.base_max_speed += 1  # Increase the base speed for enemy
                self.score_timer = time_now  # Reset the timer

            splash.load_health(self.screen, self.hero.health)
            splash.load_score(self.screen, self.hero.score)

            pygame.display.flip()
            self._clock.tick(self.FPS)


game = Game()
splash.load_menu(game.screen)
game.start()
