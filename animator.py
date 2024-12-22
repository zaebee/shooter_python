import math
import pygame


def load_sprite_sheet(filename, frame_width, frame_height):
    """Loads sprite image and returns list of frames."""
    sprite_sheet = pygame.image.load(filename).convert_alpha()
    frames = []
    for y in range(0, sprite_sheet.get_height(), frame_height):
        for x in range(0, sprite_sheet.get_width(), frame_width):
            rect = pygame.Rect(x, y, frame_width, frame_height)
            image = pygame.Surface(rect.size, pygame.SRCALPHA)
            image.blit(sprite_sheet, (0, 0), rect)
            frames.append(image)
    return frames


def scroll(img, screen, scroll_offset=0, speed=1):
    """Scrolls image background with `speed`. """
    tiles = math.ceil(screen.get_height() / img.get_height()) + 1

    for i in range(tiles):
        screen.blit(img, (0, -img.get_height() * i - scroll_offset)) 
    scroll_offset -= speed
    if abs(scroll_offset) > img.get_height(): 
        scroll_offset = 0
    return scroll_offset