from setting import *
import os
import json
from random import randint


score = {'best_score': 0}

def charger_donnees():
    if os.path.exists('donnees.json'):
        with open('donnees.json', 'r') as fichier_json:
            score_data = fichier_json.read()
            if score_data:
                return json.loads(score_data)
    return {}

def sauvegarder_donnees():
    with open("donnees.json", 'w') as f:
        json.dump(score, f)

def actualiser(point):
    if point > score['best_score']:
        score['best_score'] = point

def pomme(screen, personnage_x, personnage_y, apple_x, apple_y):
    apple_size = 10
    apple_color = (200, 0, 0)
    
    if (personnage_x <= apple_x <= personnage_x + 10 or
        personnage_x <= apple_x + apple_size <= personnage_x + 10) and \
       (personnage_y <= apple_y <= personnage_y + 10 or
        personnage_y <= apple_y + apple_size <= personnage_y + 10):

        # Si le personnage touche la pomme, générer une nouvelle pomme
        apple_x = randint(0, 400)
        apple_y = randint(0, 400)
        pygame.draw.rect(screen, apple_color, (apple_x, apple_y, apple_size, apple_size))
    
    return apple_x, apple_y