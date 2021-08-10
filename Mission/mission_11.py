class Classement :
    """
    Une implÃ©mentation primitive de classement, non ordonnÃ©e et de capacitÃ© fixe.
    @author Kim Mens
    @version 02 DÃ©cembre 2018
    """

    __maxcapacity = 10

    def __init__(self):
        """
        @pre: -
        @post: un classement vide de taille 0 a Ã©tÃ© crÃ©Ã©
        """
        self.__resultats = {}   # dictionnaire de rÃ©sultats actuelle (clÃ© = coureur; valeur = rÃ©sultat)
        self.__size = 0         # nombre de rÃ©sultats actuel (initialement 0, maximum __maxcapacity)

    def size(self):
        """
        MÃ©thode accesseur.
        Retourne la taille de ce classement.
        @pre:  -
        @post: Le nombre de rÃ©sultats actuellement stockÃ©s dans ce classement a Ã©tÃ© retournÃ©.
        """
        return self.__size

    def add(self,r):
        """
        Ajoute un rÃ©sultat r dans ce classement.
        @pre:  r est une instance de la classe Resultat
        @post: Le rÃ©sultat r a Ã©tÃ© insÃ©rÃ© selon l'ordre du classement.
               En cas d'ex-aequo, r est insÃ©rÃ© aprÃ¨s les autres rÃ©sultats de mÃªme ordre.
        ATTENTION : L'implÃ©mentation actuelle ne respecte pas encore la post-condition!
                    Le rÃ©sultat est simplement ajoutÃ© Ã  la dictionnaire, sans tenir compte de l'ordre.
                    Une dictionnaire ne donne pas de garanties sur l'ordre des Ã©lÃ©ments.
        """
        if self.size() >= self.__maxcapacity :
            raise Error("Capacity of classement exceeded")
        else :
            self.__size += 1
            self.__resultats[r.coureur()] = r

    def get(self,c):
        """
        Retourne le rÃ©sultat d'un coureur donnÃ©.
        @pre c est un Coureur
        @post retourne le premier (meilleur) Resultat r du coureur c dans le
              classement. Retourne None si le coureur ne figure pas (encore)
              dans le classement.
        """
        return self.__resultats.get(c)

    def get_position(self,c):
        """
        Retourne la meilleure position d'un coureur dans ce classement.
        @pre c est un Coureur
        @post retourne un entier reprÃ©sentant la position du coureur c dans ce classement,
              Ã  partir de 1 pour la tÃªte de ce classement. Si le coureur figure plusieurs fois
              dans le classement, la premiÃ¨re (meilleure) position est retournÃ©e.
              Retourne -1 si le coureur ne figure pas dans le classement.
        ATTENTION : L'implÃ©mentation actuelle ne respecte pas encore la post-condition!
                    Etant donnÃ© que la dictionnaire de rÃ©sultats ne connaÃ®t pas de position,
                    pour le moment cette mÃ©thode retourne toujours "***position inconnue***".
                    A vous de la corriger en utilisant une liste chaÃ®nÃ©e ordonnÃ©e
                    comme structure de donnÃ©es, plutÃ´t qu'une simple dictionnaire.
        """
        return "***position inconnue***"

    def remove(self,c):
        """
        Retire un rÃ©sultat du classement.
        @pre  c est un Coureur
        @post retire le premier (meilleur) rÃ©sultat pour le coureur c du classement.
              c est comparÃ© au sens de __eq__. Retourne c si un rÃ©sultat a Ã©tÃ© retirÃ©,
              of False si c n'est pas trouvÃ© dans la liste.
        """
        self.__size -= 1
        return self.__resultats.pop(c,False)

    def __str__(self):
        """
        MÃ©thode magique
        Retourne une reprÃ©sentation string de cet objet.
        @pre:  -
        @post: Retourne une reprÃ©sentation de ce classement sous forme d'un string,
               avec une ligne par rÃ©sultat.
        """
        s = ""
        d = self.__resultats
        for c in d:
            s += "  " + str(self.get_position(c)) + " > " + str(d[c]) + "\n"
        return s
    
class Coureur() :
    """
    ReprÃ©sente un coureur cycliste.
    @author  Kim Mens, UCLouvain
    @version 02 DÃ©cembre 2018
    """
    
    def __init__(self,nom,age) :
        """
        @pre: nom est un string non-vide
              age est un entier > 0
        @post: un coureur nommÃ© nom et Ã¢gÃ© age a Ã©tÃ© crÃ©Ã©
        """
        self.__nom = nom    # Le nom du coureur
        self.__age = age    # L'age du coureur.

    def nom(self):
        """
        MÃ©thode accesseur
        @pre:  -
        @post: le nom du coureur a Ã©tÃ© retournÃ©
        """
        return self.__nom

    def age(self):
        """
        MÃ©thode accesseur
        @pre:  -
        @post: l'Ã¢ge du coureur a Ã©tÃ© retournÃ©
        """
        return self.__age
        
    def __eq__(self, other):
        """
        MÃ©thode magique
        Teste si ce coureur est Ã©gal a un objet quelconque.
        Le critÃ¨re d'Ã©galitÃ© porte sur le nom et l'Ã¢ge du coureur.
        @pre:  -
        @post: Retourne True si other est egal Ã  self (meme type et valeurs des attributs);
               retourne False sinon.
        """
        return (type(other) == Coureur) and (self.nom() == other.nom()) and (self.age() == other.age())
    
    def __hash__(self):
        """
        MÃ©thode magique
        Retourne un hash code pour cet objet. Ceci est nÃ©cessaire pour utiliser un objet de type
        Coureur comme clÃ© d'une dictionnaire, comme dans notre implÃ©mentation naÃ¯ve du classement.
        Remarque: Pour votre implÃ©mentation vous pouvez ignorer cette mÃ©thode; elle n'est pas importante
                  si on stocke les rÃ©sultats dans une liste chaÃ®nÃ©e plutÃ´t que dans une dictionnaire.
        """
        return hash(str(self))
        
    def __str__(self):
        """
        MÃ©thode magique
        Retourne une reprÃ©sentation string de cet objet.
        @pre:  -
        @post: Retourne un reprÃ©sentation avec le nom et l'Ã¢ge de ce coureur,
               dans le format "Coureur NOM (age AGE)" 
        """
        return "Coureur " + self.nom() + " (Ã¢ge " + str(self.age()) + ")"
    
import random
import time
from coureur    import Coureur
from classement import Classement
from temps      import Temps
from resultat   import Resultat

class Main :
    """
    Classe principale pour la mission 11.
    @author  Kim Mens, UCLouvain
    @version 02 DÃ©cembre 2018
    """

    coureurs = [ Coureur("Alfred", 24), \
                 Coureur("Bernard", 27), \
                 Coureur("Claude", 19), \
                 Coureur("Daniel", 31),  \
                 Coureur("Emile", 25),  \
                 Coureur("Fred", 28),  \
                 Coureur("Gerard", 25) ]

    @classmethod
    def main(cls) :
        # CrÃ©er un classement initialement vide pour la course
        cl = Classement()
        # Boucle infinie
        while True :      
            # Choisir alÃ©atoirement un coureur de la liste
            c = random.choice(cls.coureurs)
            # Lui assigner un temps entre 1000 et 5000 secondes
            t = Temps()
            t.add_secondes(random.randint(1000, 5000))
            # CrÃ©er un rÃ©sultat pour ce coureur avec ce temps
            r = Resultat(c, t)
            print(r)
            # Cherche le dernier rÃ©sultat de ce coureur dans le classement.
            r1 = cl.get(r.coureur())
            # Imprime le classement actuel de coureur dans le classement.
            if r1 is None :
                print("  Pas encore classÃ©")
            else:
                print("  Actuellement classÃ© " + str(cl.get_position(c)))
                print("  Dernier temps enregistrÃ© = " + str(r1.temps()))
            # Compare son dernier rÃ©sultat stockÃ© avec son nouveau rÃ©sultat
            if r1 is not None and r >= r1 :
                print("  Moins bon temps, ignorÃ©")
            else :
                print("  Nouveau temps est meilleur; sera enregistrÃ©")
                cl.remove(c)
                cl.add(r)
                print("  Maintenant classÃ© " + str(cl.get_position(c)));
                print()
                print("CLASSEMENT:")
                print(cl)
            # Attendre une seconde avant de recommencer la boucle while   
            time.sleep(1)

Main.main()

class Resultat() :
    """
    Le rÃ©sultat d'un Coureur sur une course cycliste: le coureur et son temps.
    @author  Kim Mens, UCLouvain
    @version 02 DÃ©cembre 2018
    """
    
    def __init__(self,c,t):
        """
        CrÃ©e un nouveau d'un Coureur sur une course cycliste: le coureur et son temps.
        @pre: c est une instance de Coureur
              t est une instance de Temps
        @post: cette instance de Resultat a Ã©tÃ© initialisÃ© avec coureur c et temps t
        """
        self.__coureur = c  # le coureur
        self.__temps = t    # le temps effectuÃ©

    def coureur(self):
        """
        MÃ©thode accesseur.
        Retourne le coureur.
        @pre:  -
        @post: Le coureur de ce rÃ©sultat a Ã©tÃ© retournÃ©.
        """
        return self.__coureur

    def temps(self):
        """
        MÃ©thode accesseur.
        Retourne le temps.
        @pre:  -
        @post: Le temps de ce rÃ©sultat a Ã©tÃ© retournÃ©.
        """
        return self.__temps

    def __eq__(self, autre):
        """
        MÃ©thode magique.
        VÃ©rifiÃ© si ce rÃ©sultat est Ã©gal Ã  un autre, sur base de leur temps.
        @pre:  autre est une autre instance de la classe Resultat
        @post: Retourne True si le temps de ce rÃ©sultat (self) est Ã©gale au temps du rÃ©sultat autre passÃ© en paramÃ¨tre;
               retourne False sinon.
        """
        return ( self.temps() == autre.temps() )

    def __ge__(self, autre):
        """
        MÃ©thode magique.
        VÃ©rifiÃ© si ce rÃ©sultat est plus grand ou Ã©gal au rÃ©sultat passÃ© en paramÃ¨tre, sur base de leur temps.
        @pre:  autre est une autre instance valide de la classe Resultat
        @post: Retourne True si ce temps de ce rÃ©sultat (self) est plus grand que ou Ã©gale au temps du rÃ©sultat autre passÃ© en paramÃ¨tre;
               retourne False sinon.
        """
        return ( self.temps() >= autre.temps() )

    def __str__(self):
        """
        MÃ©thode magique.
        Retourne une reprÃ©sentation string de cet objet.
        @pre:  -
        @post: une reprÃ©sentation string de ce temps a Ã©tÃ© retournÃ©
               sous la forme de texte "NomCoureur: heures:minutes:secondes"
        Par exemple, "Alfred    : 05:02:10"
        """
        return "{0: <10} : {1}".format(self.coureur().nom(),self.temps())
    
class Temps :
    """
    Un temps rÃ©alisÃ© par un Coureur, sous forme de trois nombres:
    heures, minutes, secondes.
    Un temps est valide si et seulement si les minutes et les
    secondes sont comprises entre 0 et 59.
    
    @auteur Kim Mens, UCLouvain
    @version 02 DÃ©cembre 2018
    """

    def __init__(self,h=0,m=0,s=0):
        """
        CrÃ©e un nouveau temps en h heures, m minutes et s secondes.
        @pre:  h est un entier >= 0
               m est un entier entre 0 et 59    
               s est un entier entre 0 et 59
               Si aucun paramÃ¨tre n'est fourni, h, m et s seront 0.
        @post: cette instance de Temps a Ã©tÃ© initialisÃ© avec
               h heures, m minutes et s secondes
        """
        self.__heures = h	# le nombre d'heures
        self.__minutes = m	# le nombre de minutes, entre 0 et 59.
        self.__secondes = s  # le nombre de secondes, entre 0 et 59.

    def heures(self):
        """
        MÃ©thode accesseur.
        Retourne les heures.
        @pre:  -
        @post: le nombre d'heures de ce temps a Ã©tÃ© retournÃ©
        """
        return self.__heures

    def minutes(self):
        """
        MÃ©thode accesseur.
        Retourne les minutes.
        @pre:  -
        @post: le nombre de minutes de ce temps a Ã©tÃ© retournÃ©
        """
        return self.__minutes

    def secondes(self):
        """
        MÃ©thode accesseur.
        Retourne les secondes.
        @pre:  -
        @post: le nombre de secondes de ce temps a Ã©tÃ© retournÃ©
        """
        return self.__secondes

    def __str__(self):
        """
        MÃ©thode magique.
        Retourne une reprÃ©sentation string de cet objet.
        @pre:  -
        @post: une reprÃ©sentation string de ce temps a Ã©tÃ© retournÃ©
               sous la forme de texte "heures:minutes:secondes"
        Par exemple, "05:02:10" pour 5 heures, 2 minutes et 10 secondes.
        Astuce: l'expression "{:02}:{:02}:{:02}".format(heures,minutes,secondes)
        retourne le String dÃ©sirÃ© avec les nombres en deux chiffres en ajoutant
        les zÃ©ros nÃ©cessaires.
        """
        return '{:02}:{:02}:{:02}'.format(self.heures(), self.minutes(), self.secondes())

    def to_secondes(self):
        """
        Convertit ce temps en secondes.
        @pre:  -
        @post: Retourne ce temps convertit en secondes, sachant qu'une heure dure
               60 minutes et une minute dure 60 secondes.
        """
        return self.secondes() + 60 * (self.minutes() + 60 * self.heures())

    def delta(self, autre):
        """
        MÃ©thode auxiliaire pour les mÃ©thodes magiques de comparaison comme __eq__ ou __ge__.
        Retourne la diffÃ©rence entre ce temps (self) et le temps (autre) passÃ© en paramÃ¨tre,
        en secondes (positif si ce temps-ci est plus grand).
        @pre:  autre est une instance valide de la classe Temps
        @post: Retourne ce temps convertit en secondes, sachant qu'une heure dure
               60 minutes et une minute dure 60 secondes.
        """
        return self.to_secondes() - autre.to_secondes()

    def __eq__(self, autre):
        """
        MÃ©thode magique.
        VÃ©rifiÃ© si ce temps est Ã©gal au temps passÃ© en paramÃ¨tre.
        @pre:  autre est une instance valide de la classe Temps
        @post: Retourne True si ce temps (self) est Ã©gale au temps autre passÃ© en paramÃ¨tre;
               retourne False sinon.
        """
        return ( self.delta(autre) == 0 )

    def __ge__(self, autre):
        """
        MÃ©thode magique.
        VÃ©rifiÃ© si ce temps est plus grand ou Ã©gal au temps passÃ© en paramÃ¨tre.
        @pre:  autre est une instance valide de la classe Temps
        @post: Retourne True si ce temps (self) est plus grand que ou Ã©gal au temps autre passÃ© en paramÃ¨tre;
               retourne False sinon.
        """
        return ( self.delta(autre) > 0 )

    def add_secondes(self, temps_en_secondes):
        """
        Ajoute un nombre de secondes Ã  ce temps.
        Cette mÃ©thode sert comme mÃ©thode auxiliaire Ã  la mÃ©thode add(autre).
        @pre:  temps_en_secondes est un entier > 0
        @post: Un temps en secondes (temps_en_secondes, paramÃ¨tre de cette mÃ©thode)
               a Ã©tÃ© ajoutÃ© Ã  ce temps (self).
               Le temps sera normalisÃ© de maniÃ¨re Ã  ce que les minutes et les secondes du
               nouveau temps soient dans l'intervalle [0..60[, en reportant au besoin les
               valeurs hors limites sur les unitÃ©s supÃ©rieures
               (60 secondes = 1 minute, 60 minutes = 1 heure).
        """
        time = self.to_secondes() + temps_en_secondes
        self.__secondes = time % 60
        self.__minutes = (time//60) % 60
        self.__heures = (time//3600) % 24

    def add(self, autre):
        """
        Ajoute un autre temps Ã  ce temps.
        @pre:  autre est une instance valide de Temps
        @post: Un autre temps (autre, paramÃ¨tre de cette mÃ©thode)
               a Ã©tÃ© ajoutÃ© Ã  ce temps (self).
               Le temps sera normalisÃ© de maniÃ¨re Ã  ce que les minutes et les secondes du
               nouveau temps soient dans l'intervalle [0..60[, en reportant au besoin les
               valeurs hors limites sur les unitÃ©s supÃ©rieures
               (60 secondes = 1 minute, 60 minutes = 1 heure).
        """
        self.add_secondes(autre.to_secondes())
        
import unittest
from coureur import Coureur

class CoureurTest(unittest.TestCase):

    def setUp(self):
        self.coureur1 = Coureur('Kim',45)
        self.coureur2 = Coureur('Charles',50)
        self.coureur3 = Coureur('Siegfried',35)

    def test_age(self):
        self.assertEqual(self.coureur1.age(),45)
        self.assertEqual(self.coureur2.age(),50)
        self.assertEqual(self.coureur3.age(),35)
        self.assertNotEqual(self.coureur3.age(),'35') # string instead of int for age
        self.assertNotEqual(self.coureur3.age(),50)

    def test_nom(self):
        self.assertEqual(self.coureur1.nom(),'Kim')
        self.assertEqual(self.coureur2.nom(),'Charles')
        self.assertEqual(self.coureur3.nom(),'Siegfried')
        self.assertNotEqual(self.coureur3.nom(),'Kim')

    def test_different(self):
        self.assertNotEqual(self.coureur1, self.coureur2)
        self.assertNotEqual(self.coureur2, self.coureur3)
        self.assertNotEqual(self.coureur1, 2)
        self.assertNotEqual(self.coureur1, 'Kim')
        self.assertNotEqual(self.coureur1, Coureur('Kim','45')) # string instead of int for age
        self.assertNotEqual(self.coureur1, Coureur('Kim',50))
        self.assertNotEqual(self.coureur1, Coureur('Charles',45))

    def test_equal(self):
        self.assertEqual(self.coureur1, self.coureur1)
        self.assertEqual(self.coureur1, Coureur('Kim',45))
        self.assertEqual(Coureur('Kim',45),self.coureur1)
        self.assertEqual(Coureur('Kim',45), Coureur('Kim',45))
        self.assertNotEqual(Coureur('Kim',45), Coureur('Kim','45')) # string instead of int for age

# To automatically launch this test when executing this file
if __name__ == '__main__':
    unittest.main()

# To run this test from the command prompt:
#   python -m unittest test_coureur.py
#   python -m unittest test_coureur.CoureurTest
#   python -m unittest test_coureur.CoureurTest.test_equal
# or with more detail (higher verbosity) by passing in the -v flag:
#   python -m unittest -v test_coureur.py


    
