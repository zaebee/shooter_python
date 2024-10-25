import os
import pygame
import player
import enemy
import splash
import explosion

WIDTH = 500
HEIGHT = 500
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_folder = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(
    game_folder, 'images/kosmos.png'))
background_rect = background.get_rect()

pygame.init()

splash.load_menu(screen)

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
hero = player.Player([all_sprites])

for i in range(5):
    mob = enemy.Enemy([all_sprites, enemies])

clock = pygame.time.Clock()

running = True
pygame.mixer.music.load(
    os.path.join(game_folder, 'sounds/song18.mp3'))
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

score = 0

while running:
    all_sprites.update(screen=screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        hero.on_event(event)
            
    hits = pygame.sprite.groupcollide(enemies, hero.fireballs, True, True)
    for hit in hits:
        score += 1
        explosion.Explosion(hit.rect.centerx, hit.rect.centery, [all_sprites])
        mob = enemy.Enemy([all_sprites, enemies])
        
    screen.fill((BLACK))
    screen.blit(background, background_rect)
    splash.load_score(screen, score)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)