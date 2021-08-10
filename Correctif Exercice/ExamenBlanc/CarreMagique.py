
def same_ligne(carre):
    val = sum(carre[0])
    for i in carre:
        if sum(i) != val:
            return val, False
    return val, True


def same_colonne(carre, val):
    for c in range(len(carre)):
        sum = 0
        for l in carre:
            sum += l[c]
        if sum != val:
            return False
    return True


def same_diag(carre,val):
    sum = 0
    for i in range(len(carre)):
        sum += carre[i][i]
    if sum != val:
        return False
    sum = 0
    for j in range(len(carre)):
        sum += carre[j][-j-1]
    if sum != val:
        return False
    return True


def is_magic(carre):
    val, l = same_ligne(carre)
    c = same_colonne(carre, val)
    d = same_diag(carre, val)
    return l and c and d


if __name__ == '__main__':
    carree = [[2,7,6],[9,5,1],[4,3,8]]
    pas_carree = [[2,7,3],[9,5,1],[4,3,8]]

    carre_4 = [[8,11,14,1],[13,2,7,12],[3,16,9,6],[10,5,4,15]]
    print(is_magic(carree))
    print(is_magic(pas_carree))
    print(is_magic(carre_4))