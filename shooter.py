import os
import pygame
import player
import enemy

WIDTH = 500
HEIGHT = 500
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_folder = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(game_folder, 'images/kosmos.png'))
background_rect = background.get_rect()

pygame.init()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
hero = player.Player([all_sprites])

for i in range(5):
    mob = enemy.Enemy([all_sprites, enemies])

clock = pygame.time.Clock()

running = True
while running:
    all_sprites.update(screen=screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        hero.on_event(event)
            
    hits = pygame.sprite.groupcollide(enemies, hero.fireballs, True, True)
    for hit in hits:
        mob = enemy.Enemy([all_sprites, enemies])
        
    screen.fill((BLACK))
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)