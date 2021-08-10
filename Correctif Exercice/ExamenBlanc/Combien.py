def combien(n):    # Ne pas effacer cette ligne
    """
    @pre:  n est un nombre entier > 0
    @post: retourne le nombre de series d’entiers consecutifs
           strictement positifs dont la somme est egale a n
    """

    # special case of n = 0, 1 or 2.
    if n < 2:
        return 1

    # general case, obviously 1 for just the number itself
    compteur = 1
    for i in range(n+1):
        som = i
        for j in range(i+1, n+1):
            if som == n:
                compteur += 1
                break
            if som > n:
                break
            som += j
    return compteur

if __name__ == '__main__':
    print(combien(100))