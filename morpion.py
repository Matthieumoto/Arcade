from setting import *
import fenetre

def main():
    pygame.init()
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    screen_width = 300
    screen_height = 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Morpion Joueur VS Bot :")

    running = True

    background_color = (255, 255, 255)
    screen.fill(background_color)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche de la souris
                    x, y = event.pos  # Obtenez les coordonnées du clic
                    morpion_game.win(grid)
                    morpion_game.croix(screen, x, y, screen_width, screen_height, grid)
                    morpion_game.rond(screen, screen_width, screen_height, grid)
                    
        
        morpion_line.lig(screen, screen_width, screen_height)
        pygame.display.update()

        game_over = False
        resultat = morpion_game.win(grid)
        if resultat:
            print("Le gagnant est:", resultat)
            game_over = True
        
        if game_over == True:
            fenetre.rejouer(resultat)

def main2():
    pygame.init()
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    screen_width = 300
    screen_height = 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Morpion Joueur VS Joueur :")

    running = True

    background_color = (255, 255, 255)
    screen.fill(background_color)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche de la souris
                    x, y = event.pos  # Obtenez les coordonnées du clic
                    morpion_game.croix(screen, x, y, screen_width, screen_height, grid)
                if event.button == 3: # Clic gauche
                    x, y = event.pos
                    morpion_game.croix2(screen, x, y, screen_width, screen_height, grid)
                    
        
        morpion_line.lig(screen, screen_width, screen_height)
        pygame.display.update()

        game_over = False
        resultat1 = morpion_game.win2(grid)
        if resultat1:
            print("Le gagnant est:", resultat1)
            game_over = True
        
        if game_over == True:
            fenetre.rejouer2(resultat1)