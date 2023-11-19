paying =  ["","","","","","","","",""]



def display():
    row = 2
    for i in range(1,row):
            print("  "+paying[0]+ "   |  " + paying[1]+ "   |  "+ paying[2]+"  ")
            print("_____+_____+_____\n")
            print("  "+paying[3]+ "   |  " + paying[4]+ "   |  "+ paying[5]+"  ")
            print("_____+_____+_____\n")
            print("  "+paying[6]+ "   |  " + paying[7]+ "   |  "+ paying[8]+"  ")




display()
def player():
    print("Entrer un nombre en 1 et 9 :")
    for j in range(1,9):
            if j % 2 == 0:
                payer_1 = int(input("Jouer 1: "))
                paying[payer_1 +1] = "X"
                display()
            else:
                payer_2 = int(input("Jouer 2: "))
                paying[payer_2 +1] = "0"
                display()
player()
