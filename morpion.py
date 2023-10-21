from setting import *
import fenetre

def main():
    pygame.init()
    pygame.mixer.init()
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    screen_width = 300
    screen_height = 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Morpion Joueur VS Bot :")

    running = True

    background_color = (255, 255, 255)
    screen.fill(background_color)
    
    music1 = pygame.mixer.Sound("musique/F_I_R_E_128k_Spectrum_Title_Music.mp3")
    music1.play()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche de la souris
                    x, y = event.pos  # Obtenez les coordonnées du clic
                    morpion_game.win(grid)
                    morpion_game.croix(screen, x, y, screen_width, screen_height, grid)
                    music2 = pygame.mixer.Sound("musique/Menu_Selection_Sound_Effect.mp3")
                    music2.play()
                    morpion_game.rond(screen, screen_width, screen_height, grid)
                    
        
        morpion_line.lig(screen, screen_width, screen_height)
        pygame.display.update()

        game_over = False
        resultat = morpion_game.win(grid)
        if resultat:
            music1.stop()
            print("Le gagnant est:", resultat)
            if resultat == "Joueur":
                music2 = pygame.mixer.Sound("musique/Victory_Sound_Effect.mp3")
                music2.play()
            else:
                music3 = pygame.mixer.Sound("musique/Losing_sound_effect.mp3")
                music3.play()
            game_over = True
        
        if game_over == True:
            fenetre.rejouer(resultat)

def main2():
    pygame.init()
    pygame.mixer.init()
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    screen_width = 300
    screen_height = 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Morpion Joueur VS Joueur :")

    running = True

    background_color = (255, 255, 255)
    screen.fill(background_color)

    music1 = pygame.mixer.Sound("musique/F_I_R_E_128k_Spectrum_Title_Music.mp3")
    music1.play()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche de la souris
                    x, y = event.pos  # Obtenez les coordonnées du clic
                    morpion_game.croix(screen, x, y, screen_width, screen_height, grid)
                    music2 = pygame.mixer.Sound("musique/Menu_Selection_Sound_Effect.mp3")
                    music2.play()
                if event.button == 3: # Clic gauche
                    x, y = event.pos
                    morpion_game.croix2(screen, x, y, screen_width, screen_height, grid)
                    music3 = pygame.mixer.Sound("musique/Menu_Selection_Sound_Effect.mp3")
                    music3.play()
                    
        
        morpion_line.lig(screen, screen_width, screen_height)
        pygame.display.update()

        game_over = False
        resultat1 = morpion_game.win2(grid)
        if resultat1:
            music1.stop()
            music2 = pygame.mixer.Sound("musique/Victory_Sound_Effect.mp3")
            music2.play()
            print("Le gagnant est:", resultat1)
            game_over = True
        
        if game_over == True:
            fenetre.rejouer2(resultat1)