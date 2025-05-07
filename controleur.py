import random as rd

class Interface():
    def __init__(self, ):
        self.caractere_tape = 0     
        
        
    def verification(self, mot_a_verifier):
        """
        verifie que la reponse correspond au mot affiché et renvoie un booléen
        """
        if self.mot_a_taper == self.mot_a_verifier:
            reponse = True
        else:
            reponse = False
        return reponse
        
        
        
    def backspace(self, vue):
        """
        renvoie un booléen si la touche backspace est utilisé

        """
        
    
    def type_de_jeu_choisi(self, vue):
        """
        recupère le type de jeu choisi par le joueur
        """
        self.type_de_jeu = vue.type_de_jeu
          
        
    
    def creation_liste_mots(self, banque):
        """
        renvoie en fonction du type de jeu choisi, une liste de mots pour la partie à partir de la banque de données

        """
        self.liste_de_mots = rd.choices(banque.liste_mot, 10)
        
            
    
    def recupere_stats():
        """
        recupere les stats du joueur pendant la partie pour les envoyer à l'affichage

        """
    
    def recupere_streak(self, calcul):
        """
        recupere le score de combo et y associe une couleur pour l'affichage 
        """
        liste_couleur = ['red','orange red', 'orange', 'light salmon', 'sandyy brown', 'dark goldenrod', 'dark khaki', 'yellow green', 'green yellow', 'lime green', 'medium sea green', 'sea green', 'light sea green', 'dark turquoise', 'deep sky blue', 'blue', 'medium blue', 'midnight blue', 'purple4', 'purple1','maroon1']
        streak = calcul.streak
        if streak< len(liste_couleur):
            color = liste_couleur[streak]
        else:
            color = 'yellow2'
        return color
        
    
    def recupere_temps(self, vue):
        """
        va recupérer le temps pour pouvoir faire les stats de mots par seconde en utilisant la classe Calcul
        """
        self.temps_de_jeu = vue.temps
