import tkinter as tk
from tkinter import filedialog, messagebox
from controleur import Controleur

class Vue(tk.Tk):
    def __init__(self):
        
       super().__init__()
       self.title("Accueil")
       self.geometry("1200x500")
       self.controlleur = None
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

        self.radio1 = tk.Radiobutton(boutons_frame, text="Course contre la montre", variable=self.jouer, value="mode1", bg="#f0f8ff")
        self.radio2 = tk.Radiobutton(boutons_frame, text="Tolérance Zéro", variable=self.jouer, value="mode2", bg="#f0f8ff")

        self.radio1.grid(row=0, column=0, padx=20)
        self.radio2.grid(row=0, column=1, padx=20)

        self.bouton_jouer = tk.Button(self.conteneur, text="Jouer", command=self.lancer_jeu, bg="yellow")
        self.bouton_jouer.pack(pady=20)

    

    def lancer_jeu(self):
        
        if not self.fichier_var.get():
            messagebox.showwarning("Attention", "Choisissez un fichier CSV.")
            return
        mode = self.jouer.get()
        self.withdraw()
        if mode == "mode1":
            Fenetre_Course_Contre_La_Montre(self)
        elif mode == "mode2":
            Fenetre_Tolerance_Zero(self)
            
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

        


class Fenetre_jeu(tk.Toplevel):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.geometry("1200x500")
        self.configure(bg="light blue")
        
        self.conteneur = tk.Frame(self, bg="light blue")
        self.conteneur.place(relx=0.5, rely=0.5, anchor="center")
        
        bouton_jouer = tk.Button(self.conteneur, text="Jouer", bg="yellow", font=("Helvetica", 12, "bold"), command = self.jouer())
        bouton_jouer.pack(pady=5)

        bouton_resultats = tk.Button(self.conteneur, text="Montrer les résultats", bg="light green", font=("Helvetica", 12))
        bouton_resultats.pack(pady=5)
        bouton_resultats.bind("<Button-1>", lambda event: self.ouvrir_resultats())
        
        bouton_fichier = tk.Button(self.conteneur, text="Choisi Ton Dictionnaire", command=self.choisir_fichier, bg="purple", font=("Helvetica", 12))
        bouton_fichier.pack(pady=20)
        
        bouton_changer_mode = tk.Button(self.conteneur, text="Retour", command=self.changer_mode, bg="orange", font=("Helvetica", 12), command = self.changer_mode())
        bouton_changer_mode.pack(pady=20)
        
        
        
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
