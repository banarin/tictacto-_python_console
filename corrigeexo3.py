
liste = ["" for _ in range(10)]
#
def displayBoard(listes,gagnant = None):
    print("   " + liste[0]  + "   |   " + liste[1] + "   |   "+ liste[2] +"  ")
    print("______+______+______\n")
    print("   " + liste[3] + "   |   " + liste[4] + "   |   "+ liste[5] +"  ")
    print("______+______+______\n")
    print("   " + liste[6] + "   |   " + liste[7] + "   |   "+ liste[8] +"  ")
    print("\n")
    if gagnant :
        print(f"{gagnant} a ganger")

# displayBoard()

# la fonction morpion

def morpion():
    count = 0
    jouer_X = "X"
    while count < 9:
        displayBoard(liste)
        deplacer = int(input(f"c'est le tour du {jouer_X} (Entrer un nombre entre 1 et 9) : "))
        if liste[deplacer - 1] == "":
             liste[deplacer - 1] = jouer_X
             count = count + 1
        else:
            print("la case est occupée")
            continue

        #les conditions de reussite
        if (liste[0] == liste[1] == liste[2] != "" \
             or liste[0] == liste[3] == liste[6] != "" \
                  or liste[0] == liste[4] == liste[8] != "" \
                      or liste[1] == liste[4] == liste[7] != "" \
                         or liste[2] == liste[5] == liste[8] != ""\
                             or liste[6] == liste[4] == liste[2] != ""\
                                 or liste[6] == liste[7] == liste[8] != ""\
                                     or liste[3] == liste[4] == liste[5] != "" ):
            displayBoard(liste,jouer_X)
            break
        if jouer_X == "X":
            jouer_X = "O"
        else:
            jouer_X = "X"
        if count == 9:
            print("Personne n'a gagner")
if __name__ == "__main__":
    morpion()
    

        
        