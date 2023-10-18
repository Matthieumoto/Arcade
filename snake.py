from setting import *
import snake_game
from pygame.locals import *
from random import randint


def main():
    global score
    pygame.init()

    screen_width = 400
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    score = snake_game.charger_donnees()
    if not score:
        score = {'best_score': 0}
    pygame.display.set_caption(f"Snake | Meilleur score : {score['best_score']}")

    background_color = (255, 255, 255)
    screen.fill(background_color)

    clock = pygame.time.Clock()

    running = True
    personnage_x = 200
    personnage_y = 200

    apple_x, apple_y = randint(0, 400), randint(0, 400)  # Initialisez les coordonnées de la pomme

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Efface l'écran
        screen.fill(background_color)

        # Gestion des touches fléchées
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            personnage_x -= 5
        if keys[K_RIGHT]:
            personnage_x += 5
        if keys[K_UP]:
            personnage_y -= 5
        if keys[K_DOWN]:
            personnage_y += 5

        x, y = screen_width // 2, screen_height // 2
        square_size = 10  # Taille du carré
        square_color = (0, 128, 0)  # Couleur du carré
        pygame.draw.rect(screen, square_color, (x, y, square_size, square_size))
        
        apple_x, apple_y = snake_game.pomme(screen, personnage_x, personnage_y, apple_x, apple_y)  # Obtenez les nouvelles coordonnées de la pomme

        # Mise à jour de l'affichage
        pygame.display.update()

        clock.tick(60)

    pygame.display.update()