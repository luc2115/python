import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from controleur import Controleur
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class Vue(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DAKTYLOGRAF")
        self.geometry("800x600")
        self.controlleur = None
        self.time_left = 0
        self.precision_history = []
        self.wpm_history = []
        self.time_points = []
        
        self.accueil()
        
    def accueil(self):
        """ 
        interface d'accueil qui propose de choisir un liste de mots avec laquelle jouer (dans un fichier CSV), et de définir la durée de la partie
        """
        
        self.configure(bg="light blue")

        self.conteneur = tk.Frame(self, bg="light blue")
        self.conteneur.place(relx=0.5, rely=0.5, anchor="center")

        titre_label = tk.Label(
            self.conteneur,
            text="DAKTILOGRAF",
            font=("Helvetica", 42, "bold"),
            fg="blue",
            bg="light blue"
        )
        titre_label.pack(pady=(0, 10))

        intro_label = tk.Label(
            self.conteneur,
            text="Bienvenue sur DAKTILOGRAF ! Le jeu où tu peux tester ta dextérité et ta rapidité !",
            font=("Helvetica", 14),
            bg="light blue",
            fg="white"
        )
        intro_label.pack(pady=(0, 20))
        
        

        choix_label = tk.Label(
            self.conteneur,
            text="Choisis ton mode de jeu :",
            font=("Helvetica", 16),
            bg="light blue",
            fg="blue"
        )
        choix_label.pack(pady=(0, 10))

        self.jouer = tk.StringVar(value="mode1")

        boutons_frame = tk.Frame(self.conteneur, bg="light blue")
        boutons_frame.pack(pady=10)
        
        var = tk.IntVar()
        self.radio1 = tk.Radiobutton(boutons_frame, text="Course contre la montre", variable = var, value="course", bg="#f0f8ff")
        self.radio2 = tk.Radiobutton(boutons_frame, text="Tolérance Zéro", variable = var, value="zero",bg="#f0f8ff")

        self.radio1.grid(row=0, column=0, padx=20)
        self.radio2.grid(row=0, column=1, padx=20)
        
        
        self.fichier_var = tk.StringVar()
        tk.Button(self, text="Choisir fichier CSV", command=self.choisir_fichier).pack(side = "bottom",pady=5)
        tk.Entry(self, textvariable=self.fichier_var).pack(side= "bottom")

        self.bouton_jouer = tk.Button(self.conteneur, text="Jouer", command=lambda x=var.get() :self.acces_fenetre_jeu(x), bg="yellow")
        self.bouton_jouer.pack(pady=20)
        
        

    
    def acces_fenetre_jeu(self,mode):
        if not self.fichier_var.get():
            messagebox.showwarning("Attention", "Choisissez un fichier CSV.")
            return
        self.withdraw()
        if mode == "course":
            fenetre = Fenetre_Course_Contre_La_Montre(self)
        elif mode == "zero":
            fenetre = Fenetre_Tolerance_Zero(self)

    def choisir_fichier(self):
        """
        permet de sélectionner les fichiers qui contiennent les listes de mots pour la partie
        """
        fichier = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.fichier_var.set(fichier)

    

    def update_stats(self):
        """Met à jour les statistiques en temps réel"""
        if self.controlleur:
            stats = self.controlleur.get_current_stats()
            self.precision_label.config(text=f"Précision: {stats['precision']:.1f}%")
            self.wpm_label.config(text=f"MPM: {stats['wpm']:.1f}")
            self.streak_label.config(text=f"Streak: {stats['streak']}")
            
            # Enregistrement pour les graphiques
            self.precision_history.append(stats['precision'])
            self.wpm_history.append(stats['wpm'])
            self.time_points.append(self.duree_var.get() - self.time_left)
            
            if not self.controlleur.game_over:
                self.after(1000, self.update_stats)

    def fin_partie(self):
        """Affiche les statistiques finales avec des graphiques"""
        stats = self.controlleur.stats()
        self.clear()
        
        # Frame principale pour les résultats
        results_frame = ttk.Frame(self)
        results_frame.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Titre
        tk.Label(results_frame, text="Fin de partie !", font=("Helvetica", 24)).pack(pady=10)
        
        # Statistiques textuelles
        stats_frame = ttk.Frame(results_frame)
        stats_frame.pack(fill='x', pady=10)
        for key, value in stats.items():
            ttk.Label(stats_frame, text=f"{key} : {value}", font=("Helvetica", 12)).pack(pady=2)
        
        # Création des graphiques
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
        
        # Graphique de précision
        ax1.plot(self.time_points, self.precision_history, 'b-')
        ax1.set_title('Précision au fil du temps')
        ax1.set_xlabel('Temps (s)')
        ax1.set_ylabel('Précision (%)')
        ax1.grid(True)
        
        # Graphique de MPM
        ax2.plot(self.time_points, self.wpm_history, 'r-')
        ax2.set_title('Mots par minute au fil du temps')
        ax2.set_xlabel('Temps (s)')
        ax2.set_ylabel('MPM')
        ax2.grid(True)
        
        # Intégration des graphiques dans l'interface
        canvas = FigureCanvasTkAgg(fig, master=results_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        
        # Bouton pour rejouer
        ttk.Button(results_frame, text="Rejouer", command=self.accueil).pack(pady=10)

    def afficher_mot(self, mot):
        """
        affiche le nouveau mot et efface tout ce qui était écrit dans le cadre de saisie des mots
        """
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

    def clear(self):
        """
        enlève tous les widget ouverts
        """
        for widget in self.winfo_children():
            widget.destroy()

    def lancer_timer(self, duree):
        pass  # déjà géré dans start_timer
        
class Fenetre_jeu(tk.Toplevel):
    def __init__(self,master):
        
        super().__init__(master)
        self.master = master
        self.geometry("1200x500")
        self.configure(bg="light blue")
        
        self.conteneur = tk.Frame(self, bg="light blue")
        self.conteneur.place(relx=0.5, rely=0.5, anchor="center")
        
        bouton_jouer = tk.Button(self.conteneur, text="Jouer", bg="yellow", font=("Helvetica", 12, "bold"), command = self.lancer_jeu)
        bouton_jouer.pack(pady=5)

        bouton_resultats = tk.Button(self.conteneur, text="Montrer les résultats", bg="light green", font=("Helvetica", 12))
        bouton_resultats.pack(pady=5)
        bouton_resultats.bind("<Button-1>", lambda event: self.ouvrir_resultats())
        
        
        bouton_changer_mode = tk.Button(self.conteneur, text="Retour", command=self.retour_accueil, bg="orange", font=("Helvetica", 12))
        bouton_changer_mode.pack(pady=20)
        
    def lancer_jeu(self):
        self.controlleur = Controleur(self, self.master.fichier_var.get(), 60, self.mode)
        self.clear()
        
        # Frame principale pour le jeu
        game_frame = ttk.Frame(self)
        game_frame.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Frame pour les statistiques en temps réel
        stats_frame = ttk.Frame(game_frame)
        stats_frame.pack(side=tk.TOP, fill='x', pady=5)
        
        self.precision_label = ttk.Label(stats_frame, text="Précision: 100%")
        self.precision_label.pack(side=tk.LEFT, padx=10)
        
        self.wpm_label = ttk.Label(stats_frame, text="MPM: 0")
        self.wpm_label.pack(side=tk.LEFT, padx=10)
        
        self.streak_label = ttk.Label(stats_frame, text="Streak: 0")
        self.streak_label.pack(side=tk.LEFT, padx=10)
        
        self.label_mot = tk.Label(game_frame, text="", font=("Impact", 24))
        self.label_mot.pack(pady=20)

        self.saisie = tk.Entry(game_frame, font=("Impact", 18))
        self.saisie.pack()
        self.saisie.bind("<space>", self.valider)
        self.saisie.bind("<Return>", self.valider)  # Ajout de la touche Entrée
        self.saisie.bind("<BackSpace>", lambda e: self.controlleur.backspace())
        self.saisie.focus()

        self.start_timer()
        self.precision_history = []
        self.wpm_history = []
        self.time_points = []
        self.update_stats()
        self.controlleur.start_game()
        
    def choisir_fichier(self):
        """
        permet de sélectionner les fichiers qui contiennent les listes de mots pour la partie
        """
        fichier = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.fichier_var.set(fichier)

        
    def retour_accueil(self):
        self.destroy()
        self.master.deiconify()


    def ouvrir_resultats(self):
        self.destroy()
        Fenetre_Resultats(self.master, self.mode)


class Fenetre_Course_Contre_La_Montre(Fenetre_jeu):
    def __init__(self, master):
        super().__init__(master)
        self.mode = "course"
        self.title("Course contre la montre")
        label = tk.Label(self.conteneur, text="Mode : Course contre la montre", font=("Helvetica", 20, "bold"), fg="dark blue", bg="light blue")
        label.pack(pady=(0, 20))
        

class Fenetre_Tolerance_Zero(Fenetre_jeu):
    def __init__(self, master):
        super().__init__(master)
        self.mode = "zero"
        self.title("Tolérance Zéro")
        label = tk.Label(self.conteneur, text="Mode : Tolérance Zéro ", font=("Helvetica", 20, "bold"), fg="red", bg="light blue")
        label.pack(pady=(0, 20))


class Fenetre_Resultats(tk.Toplevel):
    def __init__(self, master_accueil, mode):
        super().__init__(master_accueil)
        self.title("Résultats")
        self.geometry("1200x500")
        self.configure(bg="light blue")
        self.master_accueil = master_accueil
        self.mode = mode

        conteneur = tk.Frame(self, bg="light blue")
        conteneur.place(relx=0.5, rely=0.5, anchor="center")

        label = tk.Label(conteneur, text=" Résultats du jeu ", font=("Helvetica", 20, "bold"), fg="purple", bg="light blue")
        label.pack(pady=(0, 20))

        bouton_accueil = tk.Button(conteneur, text="Revenir à l'accueil", command=self.revenir_accueil, bg="cyan", font=("Helvetica", 12))
        bouton_accueil.pack(pady=5)

        bouton_rejouer = tk.Button(conteneur, text="Rejouer", command=self.rejouer, bg="yellow", font=("Helvetica", 12))
        bouton_rejouer.pack(pady=5)

    def revenir_accueil(self):
        self.destroy()
        self.master_accueil.deiconify()

    def rejouer(self):
        self.destroy()
        if self.mode == "course":
            Fenetre_Course_Contre_La_Montre(self.master_accueil)
        elif self.mode == "zero":
            Fenetre_Tolerance_Zero(self.master_accueil)
