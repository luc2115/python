import csv
import random



####Fait avec IA 
class Banque:
    def __init__(self, fichier_csv):
        self.fichier_csv = fichier_csv
        self.liste_mots = self.transforme_into_list()

    def transforme_into_list(self):
        """Transforme le fichier CSV en liste de mots"""
        mots = []
        with open(self.fichier_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                mots.extend(row)
        random.shuffle(mots)
        return mots
