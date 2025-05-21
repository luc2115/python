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
        """
        lance la parite avec le chrono et le premier mot

        """
        self.vue.afficher_mot(self.liste_mots[self.index_mot])
        self.vue.lancer_timer(self.duree)

    def verification(self, mot_utilisateur):
        """
        verifie que la reponse correspond au mot affiché et renvoie la couleur a afficher dans le background en fonction du mot, s'il est juste ou non
        """

        mot_attendu = self.liste_mots[self.index_mot]
        if mot_utilisateur.strip() == mot_attendu:
            self.score.mot_reussi(mot_utilisateur)
            couleur = self.recupere_streak(self.score)
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
        """
        récupère le nombre de fois que la touche backspace est pressée

        """
        self.score.compte_backspace()

    def stats(self):
        """
        récupère différentes stats du joueur pour les afficher ?
        """

        
        return {
            "points": self.score.points,
            "précision": f"{self.score.precision():.2f}%",
            "mots réussis": self.score.mots_reussis,
            "mots ratés": self.score.mots_rates
        }
    def recupere_streak(self, score):
        
       """
       
       recupere le nombre de mots correct d'affilée et y associe une couleur pour l'affichage 
       
       """
       liste_couleur = ['red','orange red', 'orange', 'light salmon', 'sandyy brown', 'dark goldenrod', 'dark khaki', 'yellow green', 'green yellow', 'lime green', 'medium sea green', 'sea green', 'light sea green', 'dark turquoise', 'deep sky blue', 'blue', 'medium blue', 'midnight blue', 'purple4', 'purple1','maroon1']
       streak = score.streak
       if streak< len(liste_couleur):
           color = liste_couleur[streak]
       else:
           color = 'yellow2'
       return color
