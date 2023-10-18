from setting import *
from random import randint

def croix(screen, x, y, screen_width, screen_height, grid):
    # Taille de la croix
    cross_size = 50

    # Calculez les indices de la grille en fonction des coordonnées du clic
    row = y // (screen_height // 3)
    col = x // (screen_width // 3)

    # Vérifiez si la case est déjà occupée
    if grid[row][col] == 0:
        grid[row][col] = 2
        x_center = col * (screen_width // 3) + (screen_width // 6)
        y_center = row * (screen_height // 3) + (screen_height // 6)
        pygame.draw.line(screen, (255, 0, 0), (x_center - cross_size, y_center - cross_size),
                        (x_center + cross_size, y_center + cross_size), 5)
        pygame.draw.line(screen, (255, 0, 0), (x_center - cross_size, y_center + cross_size),
                        (x_center + cross_size, y_center - cross_size), 5)

def rond(screen, screen_width, screen_height, grid):
    # Taille du rond
    circle_size = 50

    while True:
        # Générer des coordonnées aléatoires
        x = randint(0, screen_width)
        y = randint(0, screen_height)

        # Calculez les indices de la grille en fonction des coordonnées aléatoires
        row = y // (screen_height // 3)
        col = x // (screen_width // 3)

        if 0 <= row < 3 and 0 <= col < 3:
            # Vérifiez si la case est déjà occupée
            if grid[row][col] == 0:
                grid[row][col] = 1
                x_center = col * (screen_width // 3) + (screen_width // 6)
                y_center = row * (screen_height // 3) + (screen_height // 6)
                pygame.draw.circle(screen, (0, 0, 255), (x_center, y_center), circle_size, width=5)
                break  # Sortez de la boucle une fois que le rond est dessiné
        else:
            break
        
def win(grid):
    # Vérification des colonnes
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i] == 2:
            return "Joueur"
        elif grid[0][i] == grid[1][i] == grid[2][i] == 1:
            return "Bot"

    # Vérification des lignes
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] == 2:
            return "Joueur"
        elif grid[i][0] == grid[i][1] == grid[i][2] == 1:
            return "Bot"

    # Vérification des diagonales
    if grid[0][0] == grid[1][1] == grid[2][2] == 2:
        return "Joueur"
    elif grid[0][0] == grid[1][1] == grid[2][2] == 1:
        return "Bot"

    if grid[0][2] == grid[1][1] == grid[2][0] == 2:
        return "Joueur"
    elif grid[0][2] == grid[1][1] == grid[2][0] == 1:
        return "Bot"
    
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return None  # Il y a encore des cases vides, pas de résultat

    return "Match nul"

def win2(grid):
    # Vérification des colonnes
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i] == 2:
            return "Joueur 1 (Croix)"
        elif grid[0][i] == grid[1][i] == grid[2][i] == 1:
            return "Joueur 2 (Cercle)"

    # Vérification des lignes
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] == 2:
            return "Joueur 1 (Croix)"
        elif grid[i][0] == grid[i][1] == grid[i][2] == 1:
            return "Joueur 2 (Cercle)"

    # Vérification des diagonales
    if grid[0][0] == grid[1][1] == grid[2][2] == 2:
        return "Joueur 1 (Croix)"
    elif grid[0][0] == grid[1][1] == grid[2][2] == 1:
        return "Joueur 2 (Cercle)"

    if grid[0][2] == grid[1][1] == grid[2][0] == 2:
        return "Joueur 1 (Croix)"
    elif grid[0][2] == grid[1][1] == grid[2][0] == 1:
        return "Joueur 2 (Cercle)"
    
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return None  # Il y a encore des cases vides, pas de résultat

    return "Match nul"

def croix2(screen, x, y, screen_width, screen_height, grid):
    # Taille de la croix
    circle_size = 50

    # Calculez les indices de la grille en fonction des coordonnées du clic
    row = y // (screen_height // 3)
    col = x // (screen_width // 3)

    # Vérifiez si la case est déjà occupée
    if grid[row][col] == 0:
                grid[row][col] = 1
                x_center = col * (screen_width // 3) + (screen_width // 6)
                y_center = row * (screen_height // 3) + (screen_height // 6)
                pygame.draw.circle(screen, (0, 0, 255), (x_center, y_center), circle_size, width=5)