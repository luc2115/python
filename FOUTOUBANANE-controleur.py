#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 14:59:57 2025

@author: blucas
"""

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
            couleur = self.recupere_streak(self.score.streak)
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
    def recupere_streak(self, score):
       """
       recupere le score de combo et y associe une couleur pour l'affichage 
       """
       liste_couleur = ['red','orange red', 'orange', 'light salmon', 'sandyy brown', 'dark goldenrod', 'dark khaki', 'yellow green', 'green yellow', 'lime green', 'medium sea green', 'sea green', 'light sea green', 'dark turquoise', 'deep sky blue', 'blue', 'medium blue', 'midnight blue', 'purple4', 'purple1','maroon1']
       streak = score.streak
       if streak< len(liste_couleur):
           color = liste_couleur[streak]
       else:
           color = 'yellow2'
       return color
