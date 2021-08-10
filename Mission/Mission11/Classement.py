from ordered_linked_list_inheritance import OrderedLinkedList

""" DO NOT DISTRIBUTE THIS CODE TO STUDENTS ! """


class Classement:
    """
    Implémentation de classement sur base d'une liste ordonnée.
    @author Kim Mens
    @version 01 Décembre 2019
    """

    __maxcapacity = 10

    def __init__(self):
        """
        @pre: -
        @post: un classement vide a été créé
        """
        self.__resultats = OrderedLinkedList()  # liste ordonnée de résultats

    def first(self):
        return self.__resultats.first()

    def size(self):
        """
        Méthode accesseur.
        Retourne la taille de ce classement.
        @pre:  -
        @post: Le nombre de résultats actuellement stockés dans ce classement a été retourné.
        """
        return self.__resultats.size()

    def add(self, r):
        """
        Ajoute un résultat r dans ce classement.
        @pre:  r est une instance de la classe Resultat
        @post: Le résultat r a été inséré selon l'ordre du classement.
               En cas d'ex-aequo, r est inséré après les autres résultats de même ordre.
        """
        if self.size() >= self.__maxcapacity:
            raise ValueError("Capacity of classement exceeded")
        else:
            self.__resultats.add(r)

    def get(self, c):
        """
        Retourne le résultat d'un coureur donné.
        @pre c est un Coureur
        @post retourne le premier (meilleur) Resultat r du coureur c dans le
              classement. Retourne None si le coureur ne figure pas (encore)
              dans le classement.
        """
        r = None
        node = self.__resultats.first()
        while node is not None:
            res = node.value()
            if res.coureur() == c:
                r = res
                break
            node = node.next()
        return r

    def get_position(self, c):
        """
        Retourne la meilleure position d'un coureur dans ce classement.
        @pre c est un Coureur
        @post retourne un entier représentant la position du coureur c dans ce classement,
              à partir de 1 pour la tête de ce classement. Si le coureur figure plusieurs fois
              dans le classement, la première (meilleure) position est retournée.
              Retourne -1 si le coureur ne figure pas dans le classement.
        """
        pos = -1
        pos_ctr = 0
        node = self.__resultats.first()
        while node is not None:
            res = node.value()
            pos_ctr += 1
            if res.coureur() == c:
                pos = pos_ctr
                break
            node = node.next()
        return pos

    def remove(self, c):
        """
        Retire un résultat du classement.
        @pre  c est un Coureur
        @post retire le premier (meilleur) résultat pour le coureur c du classement.
              c est comparé au sens de __eq__. Retourne c si un résultat a été retiré,
              ou False si c n'est pas trouvé dans la liste.
        """
        r = self.__resultats.remove(c)
        if r is None:
            return False
        else:
            return r

    def print(self):
        self.__resultats.print_avec_separateur(" < ")

    def __str__(self):
        """
        Méthode magique
        Retourne une représentation string de cet objet.
        @pre:  -
        @post: Retourne une représentation de ce classement sous forme d'un string,
               avec une ligne par résultat.
        """
        s = ""
        d = self.__resultats
        for c in d:
            s += "  " + str(self.get_position(c)) + " > " + str(d[c]) + "\n"
        return s