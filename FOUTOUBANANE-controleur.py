import tkinter as tk
from modele import Score
from banque import Banque

class Controleur:
    def __init__(self, vue, fichier, duree):
        self.vue = vue
        self.score = Score()
        self.banque = Banque(fichier)
        self.liste_mots = self.banque.liste_mots
        self.index_mot = 0
        self.duree = duree
        self.timer_id = None

    def start_game(self):
        self.vue.afficher_mot(self.liste_mots[self.index_mot])
        self.vue.lancer_timer(self.duree)

    def verification(self, mot_utilisateur):
        mot_attendu = self.liste_mots[self.index_mot]
        if mot_utilisateur.strip() == mot_attendu:
            self.score.mot_reussi(mot_utilisateur)
            couleur = self.vue.couleur_streak(self.score.streak)
        else:
            self.score.mot_rate()
            couleur = "red"
        self.index_mot += 1
        if self.index_mot < len(self.liste_mots):
            self.vue.afficher_mot(self.liste_mots[self.index_mot])
        else:
            self.vue.fin_partie()
        return couleur

    def backspace(self):
        self.score.compte_backspace()

    def stats(self):
        return {
            "points": self.score.points,
            "précision": f"{self.score.precision():.2f}%",
            "mots réussis": self.score.mots_reussis,
            "mots ratés": self.score.mots_rates
        }
