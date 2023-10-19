from setting import *
import os
import json

score = {'best_score': 0}

def charger_donnees():
    if os.path.exists('donnees.json'):
        with open('donnees.json', 'r') as fichier_json:
            score_data = fichier_json.read()
            if score_data:
                return json.loads(score_data)
    return {}

def actualiser(point, score):
    if point > score['best_score']:
        score['best_score'] = point
        with open("donnees.json", 'w') as f:
            json.dump(score, f)