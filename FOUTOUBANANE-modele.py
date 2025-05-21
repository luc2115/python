
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
        un compteur qui fait +1 dès que le joueur fait un backspace, et réinitialise la streak du joueur
        """
        self.backspaces += 1
        self.streak = 0

    def mot_reussi(self, mot):
        """
        fonction qui augmente la streak et compte le nombre de mots réussis, qui compte les points du joueur
        """
        self.streak += 1
        self.mots_reussis += 1
        bonus = self.calcul_bonus()
        self.points += len(mot) * bonus
        self.compte_caractere(mot)

    def mot_rate(self, mot):
        self.streak = 0
        self.mots_rates += 1

    def calcul_bonus(self):
        if self.streak >= 3:
            return 2.0
        elif self.streak >= 2:
            return 1.25
        elif self.streak >= 1:
            return 1.10
        return 1.0

    def precision(self):
        if self.caracteres_total == 0:
            return 100.0
        return 100 - (self.backspaces / self.caracteres_total * 100)
