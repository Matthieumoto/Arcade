from setting import *

def lig(screen, widht, height):
    x1 = 0
    x2 = widht
    y1 = 0
    y2 = height
    x = 100
    z = 100

    for i in range(2):
        pygame.draw.line(screen,(0, 0, 0), (x1, x), (x2, x), width=5)
        x += 100

    for j in range(2):
        pygame.draw.line(screen,(0, 0, 0), (z, y1), (z, y2), width=5)
        z += 100

