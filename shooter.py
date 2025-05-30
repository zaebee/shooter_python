import os
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
    IMAGES = os.path.join(os.path.dirname(__file__), 'images')
    SOUNDS = os.path.join(os.path.dirname(__file__), 'sounds')
    
    def __init__(self):
        pygame.init()
        self._caption = 'Space shooter'
        self._clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.background = pygame.image.load(os.path.join(self.IMAGES, 'kosmos.png'))
        
        self.all_sprites = pygame.sprite.Group()
        self.hero = player.Player(self.all_sprites)
        
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
            
            pygame.display.flip()
            self._clock.tick(self.FPS)
            

game = Game()
game.start()