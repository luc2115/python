class Score:
    def __init__(self):
        self.points = 0
        self.caracteres_total = 0
        self.backspaces = 0
        self.streak = 0
        self.mots_reussis = 0
        self.mots_rates = 0

    def compte_caractere(self, mot):
        self.caracteres_total += len(mot)

    def compte_backspace(self):
        self.backspaces += 1
        self.streak = 0

    def mot_reussi(self, mot):
        self.streak += 1
        self.mots_reussis += 1
        bonus = self.calcul_bonus() + self.bonus_caractere(mot)
        self.points += len(mot) * bonus 
        self.compte_caractere(mot)

    def bonus_caractere(self,mot):
        nombre_caractere_spe = 0
        nombre_accent_cir = 0
        for lettre in mot : 
            if lettre == "é" or lettre == "è" or lettre == "ù" or lettre == "à" or lettre == "ç" :
                nombre_caractere_spe += 1
            if lettre =="ê" or lettre == "î" or lettre == "ô" or lettre == "â" or lettre == "û":
                nombre_accent_cir += 1
        return 0.25*nombre_caractere_spe + 0,75* nombre_accent_cir
                
    
    def mot_rate(self, mot):
        self.streak = 0
        self.mots_rates += 1

    def calcul_bonus(self):
        if self.streak >= 5 : 
            bonus = 2.5
        elif self.streak >= 4 :
            bonus = 2.0
        elif self.streak >= 3:
            bonus = 1;5
        elif self.streak >= 2:
            bonus = 1.25
        elif self.streak >= 1:
            bonus = 1.10
        else :
            bonus = 1.0
        return bonus

    def precision(self):
        if self.caracteres_total == 0:
            return 100.0
        return 100 - (self.backspaces / self.caracteres_total * 100)

class Banque():
    def __init__(self,fichier_csv):
        """
        fais appel à la fonction transforme 
        """
        
    def transforme_into_csv (self):
        """
        transforme le fichier csv en listes de mot
        """
