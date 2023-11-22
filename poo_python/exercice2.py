
class Point:
    ## le construicteur
    ### pour ecrire les attributs en private on utilise __
    ### self = this
    def __init__(self,x:float,y:float):
        self.__x = x
        self.__y = y

    ###### les modoficateur #####
    #setter de X
    def setX(self,otherX):
        self.__x = otherX
    
    # getter de X
    def getX(self):
        return self.__x
    def setY(self,otherY):
        self.__Y = otherY
    def getY(self):
        return self.__x
    #### methode deplacer
    def membre_deplace(self,dx,dy):
        self.setX( self.getX() +dx)
        self.setY(self.getY() +dy)