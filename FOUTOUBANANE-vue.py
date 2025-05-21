#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 14:55:40 2025

@author: blucas
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from controleur import Controleur

class Vue(tk.Tk):
    def __init__(self):
        
        super().__init__()
        self.title("Jeu de Dactylographie")
        self.geometry("600x400")
        self.controlleur = None
        self.time_left = 0

        self.accueil()

    def accueil(self):
        """ 
        interface d'accueil qui propose de choisir un liste de mots avec laquelle jouer (dans un fichier CSV), et de définir la durée de la partie
        """
        
        self.fichier_var = tk.StringVar()
        tk.Button(self, text="Choisir fichier CSV", command=self.choisir_fichier).pack(pady=5)
        tk.Entry(self, textvariable=self.fichier_var).pack()

        self.duree_var = tk.IntVar(value=60)
        tk.Label(self, text="Durée (sec):").pack()
        tk.Entry(self, textvariable=self.duree_var).pack()

        tk.Button(self, text="Démarrer", command=self.lancer_jeu).pack(pady=10)

    def choisir_fichier(self):
        """
        permet de sélectionner les fichiers qui contiennent les listes de mots pour la partie
        """
        fichier = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.fichier_var.set(fichier)

    def lancer_jeu(self):
        
        if not self.fichier_var.get():
            messagebox.showwarning("Attention", "Choisissez un fichier CSV.")
            return
        self.controlleur = Controleur(self, self.fichier_var.get(), self.duree_var.get())
        self.clear()
        self.label_mot = tk.Label(self, text="", font=("Impact", 24))
        self.label_mot.pack(pady=20)

        self.saisie = tk.Entry(self, font=("Impact", 18))
        self.saisie.pack()
        self.saisie.bind("<space>", self.valider)
        self.saisie.bind("<BackSpace>", lambda e: self.controlleur.backspace())
        self.saisie.focus()

        self.start_timer()
        self.controlleur.start_game()

    def afficher_mot(self, mot):
        self.label_mot.config(text=mot)
        self.saisie.delete(0, tk.END)

    def valider(self, event):
        """
        change la couleur du background en fonction de la valeur qui a été renvoyée par les autres fonctions lors de la vérifiaction du mot
        """
        
        mot_utilisateur = self.saisie.get().strip()
        couleur = self.controlleur.verification(mot_utilisateur)
        self.config(bg=couleur)



    def start_timer(self):
        """
        affiche le chrono en temps réel
        """
        self.time_left = self.controlleur.duree
        self.timer_label = tk.Label(self, text=f"Temps restant : {self.time_left}s", font=("Helvetica", 14))
        self.timer_label.pack()
        self.update_timer()

    def update_timer(self):
        """
        met a jour la valeur du temps, et met fin à la partie si le temps est écoulé
        """
        
        self.time_left -= 1
        self.timer_label.config(text=f"Temps restant : {self.time_left}s")
        if self.time_left > 0:
            self.after(1000, self.update_timer)
        else:
            self.fin_partie()

    def fin_partie(self):
        """
        affiche toutes les stats calculées à la fin de la aprtie
        """
        stats = self.controlleur.stats()
        self.clear()
        tk.Label(self, text="Fin de partie !", font=("Helvetica", 24)).pack(pady=10)
        for key, value in stats.items():
            tk.Label(self, text=f"{key} : {value}", font=("Helvetica", 16)).pack(pady=2)

    def clear(self):
        """
        enlève tous les widget ouverts
        """
        for widget in self.winfo_children():
            widget.destroy()

    def lancer_timer(self, duree):
        pass  # déjà géré dans start_timer
