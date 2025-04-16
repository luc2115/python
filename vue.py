class Affichage():
  
  def affichage_text():
  #recupère la liste des mots a afficher et affiche les premiers mots de la liste dans la zone d'affichage
  #losque la touche espace est appuyée le premier mot de la liste disparait et le reste de la liste se décale vers la gauche 
  # + la suite de la liste (mot suivant dans la liste) apparait a la fin de la ligne

  def couleur_background():
    #change la couleur du fond en fonction de la couleur reçue par la class interface
    
  def nombre_erreurs():
    #si la touche backspace est appuyée on ajoute 1 a la variable nb_erreurs
    #(cette variable sera envoyée pur traitement et utilisée dans la page résultats)
    
  def text_utilisateur():
    #event= appui sur la touche espace
    #recupère le text écrit par l'utilisateur dans la zone de texte (variable text=".....")
    #réinitialise la zone de text de l'interface pour que l'utilisateur puisse ecrire un nouveau mot
    #renvoie la variable text

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
