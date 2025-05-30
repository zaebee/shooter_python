import pygame, random

pygame.init()
window = pygame.display.set_mode((400, 200))
clock = pygame.time.Clock()

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load("images/ufo_small.png")
        self.rect = self.image.get_rect(center = (x, y))
        self.particles = []

    def move(self):
        for particle in self.particles:
            particle[0][0] -= 2
            particle[0][1] += particle[1]
        particle = [
            list(self.rect.midbottom),
            random.uniform(-1, 1), 
            pygame.Color(255, random.randrange(255), 0)]
        self.particles.append(particle)
        if len(self.particles) > 30:
            self.particles.pop(0)
        self.rect.centerx -= 3

    def draw(self, screen):
        for i, particle in enumerate(self.particles):
            pygame.draw.circle(screen, particle[2], particle[0], random.uniform(0.2, 3.3), draw_bottom_right=True)
        screen.blit(self.image, self.rect)
        

background = pygame.Surface(window.get_size())

bullet = Bullet(0, 100)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        
    bullet.move()
    if bullet.rect.left < -40:
        bullet.rect.right = 400

    window.blit(background, (0, 0))
    bullet.draw(window)
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
exit()