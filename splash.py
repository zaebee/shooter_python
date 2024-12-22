import sys
import pygame

def load_menu(screen: pygame.Surface):
    splash = pygame.Surface([800, 800])
    font = pygame.font.SysFont('arial', 20)
    buttons = [
        (160, 140, 'Play', 0), #  x=160, y=140, text='Play', position = 0
        (160, 210, 'Exit', 1)  #  x=160, y=210, text='Exit', position = 1
    ]
    pygame.mouse.set_visible(True)
    
    done = False
    item = -1
    while not done:
        splash.fill([0, 0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print(item)
                if item == 0: # click Play button
                    done = True
                elif item == 1: # click Exit button
                    pygame.quit()
                    sys.exit()
        pointer = pygame.mouse.get_pos()
        for button in buttons:
            if (pointer[0] > button[0] and pointer[0] < button[0] + 155 and 
                pointer[1] > button[1] and pointer[1] < button[1] + 50):
                item = button[3]
        
        for button in buttons:
            if item == button[3]:
                btn = font.render(button[2], 1, (255, 0, 0))
            else:
                btn = font.render(button[2], 1, (255, 255, 255))
            splash.blit(btn, [button[0], button[1]])
            
        screen.blit(splash, [0, 0])
        pygame.display.flip()

       
def load_score(screen, score):
    surface = pygame.Surface([400, 40]) # создаем поверхность 500х40
    font = pygame.font.SysFont('arial', 20) # создаем шрифт 'arial' размером 20px
    surface.fill([131, 35, 35]) # заливаем нашу поверхность красным цветом
    surface.set_alpha(128)
    screen.blit(surface, [0, 0]) # отображаем поверхность на экране в точке 0px, 0px
    text = font.render(f'Score: {score}', 1, [255, 0, 0]) # создаем наш текст с очками
    screen.blit(text, [10, 10]) # отображаем текст на поверхности в точке 10px, 10px
    
    
def load_health(screen, health):
    """"""
    surface = pygame.Surface([400, 40]) # создаем поверхность 500х40
    font = pygame.font.SysFont('arial', 20) # создаем шрифт 'arial' размером 20px
    surface.fill([131, 35, 35]) # заливаем нашу поверхность красным цветом
    surface.set_alpha(128)
    screen.blit(surface, [400, 0]) # отображаем поверхность на экране в точке 0px, 0px
    text = font.render(f'Health: {health}', 1, [255, 0, 0]) # создаем наш текст с очками
    screen.blit(text, [440, 10]) # отображаем текст на поверхности в точке 10px, 10px