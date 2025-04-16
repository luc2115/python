class Affichage():
  
  def affichage_text():
      """
      recupère la liste des mots a afficher et affiche les premiers mots de la liste dans la zone d'affichage
      losque la touche espace est appuyée le premier mot de la liste disparait et le reste de la liste se décale vers la gauche 
      + la suite de la liste (mot suivant dans la liste) apparait a la fin de la ligne
      """

  def couleur_background():
      """"
      change la couleur du fond en fonction de la couleur reçue par la class interface
      """
      
  def nombre_erreurs():
      """
      si la touche backspace est appuyée on ajoute 1 a la variable nb_erreurs
      (cette variable sera envoyée pur traitement et utilisée dans la page résultats)
      """
    
  def text_utilisateur():
      """
      event= appui sur la touche espace
      recupère le text écrit par l'utilisateur dans la zone de texte (variable text=".....")
      réinitialise la zone de text de l'interface pour que l'utilisateur puisse ecrire un nouveau mot
      renvoie la variable text
      """

  def demarrer_le_jeu():
        """
        Lorsque une lettre est pressée dans la zone de texte,
            + le chronomètre se lance si mode de jeu = course contre la montre
        et on lance les fonctions/méthodes chargées de l'acquisition de toutes les données tels que le nombre de frappe, de mots...
        Les fonctions chargées de l'acquisition stockent les données dans des variables ensuite utilisées 
        par la partie 'calcul'
        
        """
        
  def arreter_le_jeu():
        """
        si mode_de_jeu = course_contre_la_montre:
            le jeu s'arrête quand le compte à rebourd arrive à 0
        si mode_de_jeu = tolerence_zero : 
            le jeu s'arrête dès qu'une erreur est commise
        Envoie toutes les données stockées dans les différentes variables vers la partie 'calcul' pour avoir 
        les résultats et statistiques du joueur sur cette partie.
        
        """
  def reinitialiser():
        """
        fonction lier au bouton 'RESTART' qui reinitialise toutes les variables quand le bouton est pressé,
        par exemple si le joueur a fait un mauvais départ ou veux faire une nouvelle partie
        
        """
        
  def chrono():
        """
        affiche un compte à rebours qui se déclenche avec la fonction 'demarrer_le_jeu'
        
        """



class Banque():
    def __init__(self,fichier_csv):
        """
        fais appel à la fonction transforme 
        """
        
    def transforme_into_csv (self):
        """
        transforme le fichier csv en listes de mot
        """




class Score():
    
    def __init__(self,):
         """
         intialise les différentes valeurs (surement à 0)
         """
    def nb_caracteres_mot_courant(self):
        """
        calcule le nb de caracteres d'un mot'
        """
    def compte_caracteres(self):
        """
        Un compteur qui fait +1 pour chaque caractère des mots

        """
    def compte_back_space(self):
        """
        un compteur qui fait +1 dès que le joueur fait un backspace
        """
    def streak(self):
        """
        Combien de bons mots sans avoir fait d'erreurs (un backspace remet le compteur à 0)
        """
    def bonus(self):
        """
        Prend en entrée la streak et donne des points en plus en fonction 
        Streak à 5 mots, +10% points
        Streak à 10 mots, +20% points
        Le 20ème mot bien écrit compte double puis on reste à +25% après
        """
    def point_du_mot(self):
        """
        Utilise bonus, le nb_de_caractères_du_mot
        et associe, si le mot est
        """
    def compteur_de_points(self):
        """
        Compte les points !!
        """
    def calcul_precision(self):
        """
        100 - compte_back_space/Nombre de caractères
        """
    def mots_reussis(self):
        """
        le nom parle de lui meme
        """
    def mots_rates(self):
        """
        le nom parle de lui meme
        """



class Controleur():
    def __init__():
        """
        initialise le controleur
        """
    def recup_mot():
        """
        recupere le mot tapé par l'utilisateur
        """
        
    def verification():
        """
        verifie que la reponse correspond au mot affiché et renvoie un booléen
        """
        
    def compte_lettre():
        """
        compte le nombre de caractere du mot tapé qu'il soit juste ou non
        
        """
        
    def backspace():
        """
        renvoie un booléen si la touche backspace est utilisé

        """
    
    def type_de_jeu_choisi():
        """
        recupère le type de jeu choisi par le joueur
        """
    
    def creation_liste_mots():
        """
        renvoie en fonction du type de jeu choisi, une liste de mots pour la partie à partir de la banque de données

        """
    
    def recupere_stats():
        """
        recupere les stats du joueur pendant la partie pour les envoyer à l'affichage

        """
    
    def recupere_streak():
        """
        recupere le score de combo et y associe une couleur pour l'affichage 
        """
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



















