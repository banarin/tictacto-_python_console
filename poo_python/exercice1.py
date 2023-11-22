class Etudiant:
    # le contructeur
    ## le mot cle self est comme un this en java
    def __init__ (self,nom:str,note1:float,note2:float):
        self.nom = nom
        self.note1 = note1
        self.note2 = note2
    
    #la methode calc_moy()
    def calc_moy(self):
        # moy = (self.note1 + self.note2)/2
        return (self.note1 + self.note2)/2
    # methode pour affiche le nom et la note moyenne.
    def afficher (self):
        print(f"le nom : {self.nom}")
        print(f"la moyenne : {self.calc_moy()}")
        
#le programme principale main
if __name__ == "__main__":
    #demander utilisateur
    nom = input("Entrer le nom : ")
    not1 = float(input("Entrer la note 1 : "))
    not2 = float(input("Entrer la note 2 : "))

    # creation de l'objet
    etudiant = Etudiant(nom,not1,not2)
    print(etudiant.calc_moy())
    etudiant.afficher()