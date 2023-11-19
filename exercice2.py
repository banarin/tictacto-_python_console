#fonction qui calcule le factoriel
def fact(n):
    fac = 1
    if(n == 0):
        return 1
    for j in range(1,n+1):
        fac = fac * j
    return fac
## fonction pour returner la liste des factoriel

def factoriel(liste):
    ##
    # value = []
    # for i in liste:
    #     value.append(fact(i))
    # return value
    ####### liste en comprehension
    return [fact(i) for i in liste]
# afficher la liste 
print(factoriel([2,6]))