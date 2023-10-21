from setting import *
import snake_game
from pygame import *
from pygame.locals import *
import fenetre
import random
import time

def main():
    pygame.init()
    pygame.mixer.init()
    k = 2
    k1 = k

    current_direction = "h"

    snake_List = []
    Length_of_snake = 1

    snake_block = 15
    point = 0

    screen_width = 400
    screen_hight = 400
    screen = pygame.display.set_mode((screen_width, screen_hight))
    
    score = snake_game.charger_donnees()
    pygame.display.set_caption(f"Snake | Meilleur score : {score['best_score']}")
    
    background_color = (200, 200, 200)
    score_font = pygame.font.SysFont("comicsansms", 18)

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

    def Your_score(point):
        value = score_font.render("Score: " + str(point), True, (0,0,0))
        screen.blit(value, [0, 0])
    
    point = 0 
    green = (0, 128, 0)
    red = (255, 0, 0)

    y1 = screen_width / 2
    x1 = screen_hight /  2
    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, screen_width - 20) / 10.0) * 10.0
    foody = round(random.randrange(0, 385 - 35) / 10.0) * 10.0
    p1 = foodx + 10
    p2 = foody + 10

    clock = pygame.time.Clock()

    game_over = False

    music1 = pygame.mixer.Sound("musique/F_I_R_E_128k_Spectrum_Title_Music.mp3")
    music1.play()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(background_color)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and current_direction != "d":
                x1_change = - k
                y1_change = 0
                current_direction = "g"
            elif event.key == pygame.K_RIGHT and current_direction != "g":
                x1_change = k
                y1_change = 0
                current_direction = "d"
            elif event.key == pygame.K_UP and current_direction != "b":
                y1_change = - k1
                x1_change = 0
                current_direction = "h"
            elif event.key == pygame.K_DOWN and current_direction != "h":
                y1_change = k1
                x1_change = 0
                current_direction = "b"

        x1 += x1_change
        y1 += y1_change

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
                if x == snake_Head:
                    game_over = True
    
        # Mise à jour de l'affichage
        pygame.draw.rect(screen, background_color, [foodx, foody, 20, 20])
        pygame.draw.rect(screen, red, [p1, p2, 10, 10])

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Vérifier la collision avec la nourriture en dehors de la boucle principale
        if (foodx <= x1 <= foodx + 20) and (foody <= y1 <= foody + 20):
            music2 = pygame.mixer.Sound("musique/Eating_sound_effect.mp3")
            music2.play()
            foodx = round(random.randrange(0, 385 - 35) / 10.0) * 10.0
            foody = round(random.randrange(0, 385 - 35) / 10.0) * 10.0
            p1 = foodx + 10
            p2 = foody + 10
            Length_of_snake += 1
            point += 1
            k += 0.05
            k1 += 0.05               
            snake_game.actualiser(point, score)

        # Vérifier les collisions et conditions de fin du jeu
        if (x1 >= (screen_width - 15) or x1 < 0 or y1 >= (screen_width - 15) or y1 < 0
            or any(x == snake_Head for x in snake_List[:-1])):
            music1.stop()
            music3 = pygame.mixer.Sound("musique/Losing_sound_effect.mp3")
            music3.play()
            time.sleep(1)
            if point == score['best_score']:
                music4 = pygame.mixer.Sound("musique/Victory_Sound_Effect.mp3")
                music4.play()
                fenetre.new(point)
            fenetre.mort(point, score)
            game_over = True

        clock.tick(30)

pygame.quit()