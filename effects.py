import math


def scroll(img, screen, scroll_offset=0, speed=1):
    """Scrolls image background with `speed`. """
    tiles = math.ceil(screen.get_height() / img.get_height()) + 1

    for i in range(tiles):
        screen.blit(img, (0, -img.get_height() * i - scroll_offset)) 
    scroll_offset -= speed
    if abs(scroll_offset) > img.get_height(): 
        scroll_offset = 0
    return scroll_offset

 
def shake():
    """Creates our shake-generator # it "moves" the screen to the left 
    and right three times by yielding (-5, 0), (-10, 0), ... (-20, 0), 
    (-15, 0) ... (20, 0) three times, then keeps yielding (0, 0)."""
    s = -1
    for _ in range(0, 3):
        for x in range(0, 20, 5):
            yield (x * s, 0)
        for x in range(20, 0, 5):
            yield (x * s, 0)
        s *= -1
    while True:
        yield (0, 0)