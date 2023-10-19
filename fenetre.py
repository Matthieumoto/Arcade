from setting import *
from tkinter import *
import morpion
import snake
import snake_game

def ma_fenetre():
    global score
    fenetre = Tk()
    fenetre.geometry('300x300')
    fenetre.title('Jeux')

    l = LabelFrame(fenetre, text="Morpion", padx=20, pady=20)
    l.pack(fill="both", expand="no")

    bouton_bot = Button(l, text="Joueur VS Bot", command=lambda: [fenetre.destroy(), morpion.main()])
    bouton_bot.pack()

    bouton_jouer = Button(l, text="Joueur VS Joueur", command=lambda: [fenetre.destroy(), morpion.main2()])
    bouton_jouer.pack()

    m = LabelFrame(fenetre, text="Snake", padx=20, pady=20)
    m.pack(fill="both", expand="no")

    score = snake_game.charger_donnees()
    if not score:
        score = {'best_score': 0}
    meilleur_score = Label(m, text=f"Meilleur Score : {score['best_score']}")
    meilleur_score.pack()

    bouton_jouer_snake = Button(m, text="Jouer", command=lambda: [fenetre.destroy(), snake.main()])
    bouton_jouer_snake.pack()

    bouton_quit = Button(fenetre, text="Quitter", command=lambda: fenetre.destroy())
    bouton_quit.pack()

    fenetre.mainloop()

def rejouer(resultat):
    fenetre = Tk()
    fenetre.geometry('300x300')
    fenetre.title(f"le gagnant est : {resultat}")

    if resultat == "Joueur":
        choix_label = Label(fenetre, text="Vous avez gagner !")
        choix_label.pack()
    elif resultat == "Bot":
        choix_label = Label(fenetre, text="Vous avez perdu !")
        choix_label.pack()
    else:
        choix_label = Label(fenetre, text="Vous avez fait match nul !")
        choix_label.pack()

    bouton_jouer = Button(fenetre, text="Voulez vous rejouer ?", command=lambda: [fenetre.destroy(), pygame.quit(), morpion.main()])
    bouton_jouer.pack()

    bouton_quit = Button(fenetre, text="Quitter", command=lambda: [fenetre.destroy(),pygame.quit(), ma_fenetre()])
    bouton_quit.pack()

    fenetre.mainloop()

def rejouer2(resultat1):
    fenetre = Tk()
    fenetre.geometry('300x300')
    fenetre.title(f"le gagnant est : {resultat1}")

    if resultat1 == "Joueur 1 (Croix)":
        choix_label = Label(fenetre, text="Le joueur 1 (Croix) a Gagner !")
        choix_label.pack()
    elif resultat1 == "Joueur 2 (Cercle)":
        choix_label = Label(fenetre, text="Le joueur 2 (Cercle) a Gagner !")
        choix_label.pack()
    else:
        choix_label = Label(fenetre, text="Vous avez fait match nul !")
        choix_label.pack()

    bouton_jouer = Button(fenetre, text="Voulez vous rejouer ?", command=lambda: [fenetre.destroy(), pygame.quit(), morpion.main2()])
    bouton_jouer.pack()

    bouton_quit = Button(fenetre, text="Quitter", command=lambda: [fenetre.destroy(),pygame.quit(), ma_fenetre()])
    bouton_quit.pack()

    fenetre.mainloop()

def mort(point, score):
    fenetre = Tk()
    fenetre.geometry('200x200')
    fenetre.title("Vous etes mort !")

    snake_game.actualiser(point, score)

    m = Label(fenetre, text=f"Votre score est de {point} ")
    m.pack()

    l = Label(fenetre, text=f"Votre meilleur score est de {score['best_score']} points !")
    l.pack()

    bouton_pause = Button(fenetre, text="Rejouer ?", command=lambda: [fenetre.destroy(), pygame.quit(), snake.main()])
    bouton_pause.pack()

    bouton_quit = Button(fenetre, text="Quitter", command=lambda: [fenetre.destroy(),pygame.quit(), ma_fenetre()])
    bouton_quit.pack()

    fenetre.mainloop()