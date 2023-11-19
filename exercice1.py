###### exercice 1 ######

# la fonction qui return le dictionnaire  avec les cles et les valeurs qui sont la moyenne de chaque clé
def moyenne(dico):
    for key, value in dico.items():
        moy = sum(value)/len(value)
        dico[key] = moy
    return dico
    print(moy)
    
# declaration du dictionnaire 
 
dico = {
    "Aladin": [12,15,17],
    "Nathalie": [14,15,12],
    "Robert": [18,11,16],
}

# on a fait appel a la fonction en affichant
print(moyenne(dico))

####### exercice 2 ###########