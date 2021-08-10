def mix(l):    # Ne pas effacer cette ligne
    """
    @pre:    l est une liste d'entiers
            la taille n de cette liste est un nombre pair
    @post:   retourne une liste r d’entiers
            la liste retournée r a la même taille n
            pour chaque index 0 ≤ i < n où i est pair on a la
            correspondance suivante entre les deux listes :
                r[i] = l[i//2]
                r[i+1] = l[n-1-(i//2)]
    """
    n = len(l)
    r = [0]*n
    for i in range(0, n, 2):
        r[i] = l[i//2]
        r[i+1] = l[n-1-(i//2)]
    return r

if __name__ == '__main__':
    print(mix([1, 2, 3, 4]))