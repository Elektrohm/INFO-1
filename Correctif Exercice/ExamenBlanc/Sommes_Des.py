def somme_des(n):    # Ne pas effacer cette ligne
    """
    @pre:  n est un nombre entier > 0
    @post: retourne un dictionnaire avec comme différentes clés
           chaque somme possible des valeurs des dés,
           et comme valeur associée à cette clé e,
           la liste des tuples des valeurs des dés qui addtionnées donnent e
    """
    dic_of_sum = {}
    for i in range(1, n+1):
        for j in range(1, n+1):
            dic_of_sum[i+j] = dic_of_sum.get(i+j, []) + [(i, j)]
    return dic_of_sum


if __name__ == '__main__':
    print(somme_des(4))
    print(somme_des(6))