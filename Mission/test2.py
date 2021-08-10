def chiffre_pair(n):
    compteur = longueur(n)
    boolean = is_even(compteur)
    return boolean

def longueur(n):
    compteur = 0
    for i in str(n):
        compteur+=1
    return compteur    
    
def is_even(long):
    print(long)
    return long%2==0

