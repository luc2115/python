
class Score:
    def __init__(self):
        self.points = 0
        self.caracteres_total = 0
        self.backspaces = 0
        self.streak = 0
        self.mots_reussis = 0
        self.mots_rates = 0

    def compte_caractere(self, mot):
        """
        Un compteur qui ajoute le nombre de lettres du mot qu'on aurait du ecrire à chauqe mot de toute la partie
        """
        self.caracteres_total += len(mot)

    def compte_backspace(self):
        """
        un compteur qui fait +1 dès que le joueur fait un backspace, et réinitialise la streak du joueur quand le joueur fais un backspace
        """
        self.backspaces += 1
        self.streak = 0

    def mot_reussi(self, mot):
        """
        augmente la streak et compte le nombre de mots réussis, qui compte les points du joueur si le mot est correct
        """
        self.streak += 1
        self.mots_reussis += 1
        bonus = self.calcul_bonus()
        self.points += len(mot) * bonus
        self.compte_caractere(mot)

    def mot_rate(self, mot):
        """
        compte les mots ratés et réinitialise la streak du joueur si le mot est raté
        """
        
        self.streak = 0
        self.mots_rates += 1

     def calcul_bonus(self):
         """ 
         renvoie le bonus relatif a la streak du joueur
         """
        if self.streak >= 5 : 
            bonus = 2.5
        elif self.streak >= 4 :
            bonus = 2.0
        elif self.streak >= 3:
            bonus = 1.5
        elif self.streak >= 2:
            bonus = 1.25
        elif self.streak >= 1:
            bonus = 1.10
        else :
            bonus = 1.0
        return bonus
    
    def bonus_caractere(self,mot):
        """
        Calcul de la seconde partie du bonus, basée ce coup-ci sur la difficulté des caractères à taper
        """
        nombre_caractere_spe = 0 
        nombre_accent_cir = 0
        for lettre in mot : 
            if lettre == "é" or lettre == "è" or lettre == "ù" or lettre == "à" or lettre == "ç" :
                nombre_caractere_spe += 1
            if lettre =="ê" or lettre == "î" or lettre == "ô" or lettre == "â" or lettre == "û":
                nombre_accent_cir += 1
        return 0.25*nombre_caractere_spe + 0,75* nombre_accent_cir

    def precision(self):
        ratio_erreur = 0 
        if self.caracteres_total != 0 :
            ratio_erreur = (self.backspaces / self.caracteres_total * 100)
        return 100 - ratio_erreur
