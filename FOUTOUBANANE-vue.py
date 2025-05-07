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
        self.fichier_var = tk.StringVar()
        tk.Button(self, text="Choisir fichier CSV", command=self.choisir_fichier).pack(pady=5)
        tk.Entry(self, textvariable=self.fichier_var).pack()

        self.duree_var = tk.IntVar(value=60)
        tk.Label(self, text="Durée (sec):").pack()
        tk.Entry(self, textvariable=self.duree_var).pack()

        tk.Button(self, text="Démarrer", command=self.lancer_jeu).pack(pady=10)

    def choisir_fichier(self):
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
        mot_utilisateur = self.saisie.get().strip()
        couleur = self.controlleur.verification(mot_utilisateur)
        self.config(bg=couleur)

    def couleur_streak(self, streak):
        if streak >= 5:
            return "#007FFF"
        elif streak >= 4:
            return "#22ff77"
        elif streak >= 3:
            return "#33ff77"
        elif streak >= 2:
            return "#44ff77"
        elif streak >= 1:
            return "#55ff55"
        return "white"

    def start_timer(self):
        self.time_left = self.controlleur.duree
        self.timer_label = tk.Label(self, text=f"Temps restant : {self.time_left}s", font=("Helvetica", 14))
        self.timer_label.pack()
        self.update_timer()

    def update_timer(self):
        self.time_left -= 1
        self.timer_label.config(text=f"Temps restant : {self.time_left}s")
        if self.time_left > 0:
            self.after(1000, self.update_timer)
        else:
            self.fin_partie()

    def fin_partie(self):
        stats = self.controlleur.stats()
        self.clear()
        tk.Label(self, text="Fin de partie !", font=("Helvetica", 24)).pack(pady=10)
        for key, value in stats.items():
            tk.Label(self, text=f"{key} : {value}", font=("Helvetica", 16)).pack(pady=2)

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def lancer_timer(self, duree):
        pass  # déjà géré dans start_timer
