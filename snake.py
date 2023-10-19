from setting import *
import snake_game
from pygame.locals import *
import fenetre
import random

def main():
    pygame.init()

    k = 15

    screen_width = 400
    screen_hight = 400
    screen = pygame.display.set_mode((screen_width, screen_hight))
    
    score = snake_game.charger_donnees()
    pygame.display.set_caption(f"Snake | Meilleur score : {score['best_score']}")
    
    background_color = (200, 200, 200)

    def our_snake(snake_list):
        for i in snake_list:
            pygame.draw.rect(screen, green, [i[0], i[1], 15, 15])

    point = 0 
    green = (0, 128, 0)
    red = (255, 0, 0)

    y1 = screen_width / 2
    x1 = screen_hight /  2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, screen_width - 20) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_hight - 20) / 10.0) * 10.0
    p1 = foodx + 5
    p2 = foody + 5

    clock = pygame.time.Clock()

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(background_color)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -5
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 5
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -5
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 5
                x1_change = 0

        x1 += x1_change
        y1 += y1_change

        pygame.draw.rect(screen, green, [x1, y1, 15, 15])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Mise à jour de l'affichage
        pygame.draw.rect(screen, background_color, [foodx, foody, 20, 20])
        pygame.draw.rect(screen, red, [p1, p2, 10, 10])
        our_snake(snake_List)
        pygame.display.update()

        # Vérifier la collision avec la nourriture en dehors de la boucle principale
        if (foodx <= x1 <= foodx + 20) and (foody <= y1 <= foody + 20):
            foodx = round(random.randrange(0, screen_width - 20) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_hight - 20) / 10.0) * 10.0
            p1 = foodx + 5
            p2 = foody + 5
            Length_of_snake += 1
            point += 1
            k += 0.5
            snake_game.actualiser(point, score)

        # Vérifier les collisions et conditions de fin du jeu
        if (x1 == screen_width - 15 or x1 == 0 or y1 == screen_hight - 15 or y1 == 0
            or any(x == snake_Head for x in snake_List[:-1])):
            fenetre.mort(point, score)
            game_over = True

        clock.tick(k)

pygame.quit()