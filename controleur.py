class Interface():
    def __init__(self, ):
        """
        """     
        
    def recup_mot(self,vue):
        """
        recupere le mot tapé par l'utilisateur
        """
        self.mot_a_verifier = vue.mot_ecrit
        
        
    def verification(self):
        """
        verifie que la reponse correspond au mot affiché et renvoie un booléen
        """
        if self.mot_a_taper == self.mot_a_verifier:
            reponse = True
        else:
            reponse = False
        return reponse
        
    def backspace():
        """
        renvoie un booléen si la touche backspace est utilisé

        """
    
    def type_de_jeu_choisi(self, interface):
        """
        recupère le type de jeu choisi par le joueur
        """
        self.type_de_jeu = interface.type_de_jeu
    
    def creation_liste_mots():
        """
        renvoie en fonction du type de jeu choisi, une liste de mots pour la partie à partir de la banque de données

        """
    
    def recupere_stats():
        """
        recupere les stats du joueur pendant la partie pour les envoyer à l'affichage

        """
    
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

    def recupere_temps():
        """
        va recupérer le temps pour pouvoir faire les stats de mots par seconde en utilisant la classe Calcul
        """
    
