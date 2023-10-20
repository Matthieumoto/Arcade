from setting import *
import pygame

def start_music():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("musique/F_I_R_E_128K_Spectrum_Title_Music.mp3")  # Remplacez "musique.mp3" par le chemin de votre fichier musical
    pygame.mixer.music.play(-1)

if __name__ == "__main__":
    start_music()
    fenetre.ma_fenetre()