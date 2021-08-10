class Article :
    __taux_tva = 0.21   # TVA a 21%
    
    def __init__(self,d,p):
        """
        Cree un article avec description d et prix p.
        """
        self.__description = d
        self.__prix = p
        
    def description(self):
        """
        Retourne la description de cet article.
        """
        return self.__description
        
    def prix(self):
        """
        Retourne le prix (HTVA) de cet article.
        """
        return self.__prix
        
    def taux_tva(self):
        """
        Retourne le taux de TVA (même valeur pour chaque article)
        """    
        return self.__taux_tva

    def tva(self):
        """
        Retourne la TVA sur cet article
        """    
        return self.prix() * self.taux_tva()
 
    def prix_tvac(self):
        """
        Retourne le prix de l'article, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self):
        """
        Retourne un texte decrivant cet article, au format: "{description}: {prix}"
        """
        return "{0}: {1:.2f}".format(self.description(), self.prix())
    
class ArticleReparation(Article):
    
    def __init__(self,d,p,duree):
        super().__init__(d,p)
        self.__duree = duree
    
    def description(self):
        return "Réparation ({} heures)".format(self.__duree)
    
    def prix(self):
        return 20 + 35*self.__duree
    
class Piece:
    
    def __init__(self,descriptif,prix_unitaire,poids_unitaire=None,fragile=None,TVA_reduit=None):
        self.__description = descriptif
        self.__prix = prix_unitaire
        self.__poids = poids_unitaire
        self.__fragile = fragile
        self.__TVA = TVA_reduit
        
    def description(self):
        return self.__description
    
    def prix(self):
        return self.__prix
    
    def poids(self):
        return self.__poids
    
    def fragile(self):
        return self.__fragile
    
    def tva_reduit(self):
        return self.__TVA
    
    def __eq__(self,other):
        if self.__description == other.__description and self.__prix == other.__prix:
            return True
        else:
            return False
    
    def __str__(self):
        return "{} : {}".format(self.__description,self.__prix)
        
class ArticlePiece(Article) :
    
    def __init__(self,nombre,Piece,d=None,p=None):
        super().__init__(d,p)
        self.__number = nombre
        self.__piece = Piece
    
    def nombre(self):
        return self.__number
    
    def piece(self):
        return self.__piece
    
    def description(self):
        return "{0} * {1} @ {2}".format(self.__number, self.__piece.description(), self.__piece.prix())  
    
    def prix(self):
        return self.__number * self.__piece.prix()
    
    def tva(self):
        d = self.piece()
        p = self.taux_tva()
        if d.tva_reduit():
            p = 0.06
            
class Facture :
    __facture_numero = 0
    
    def __init__(self, description, articles):
        self.__reference = description
        self.__articles = articles
        self.__numero = self.__facture_numero
        Facture.__facture_numero += 1

    def description(self):
        """
        Retourne la description de cette facture.
        """
        return self.__reference

    def articles(self):
        """
        Retourne la liste des articles de cette facture.
        """
        return self.__articles
        
    def entete_str(self):
        """
        Imprime l'entête de la facture, comprenant le descriptif et les têtes de colonnes.
        """
        e = "Livraison - " + "Facture No : "+ str(self.__numero) +" "+ self.description() + "\n"
        e += self.barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","poids/pce","nombre","poids")
        e += self.barre_str()
        return e

    def barre_str(self):
        """
        Retourne un string représentant une barre horizontale sur la largeur de la facture.
        """
        b = ""
        barre_longeur = 83
        for i in range(barre_longeur):
            b += "="
        return b + "\n"

    def article_str(self, art):
        """
        Retourne un string correspondant à une ligne de facture pour l'article art
        """
        attention = ''
        if art.piece().fragile() == True:
            attention = '(!)'
        return "| {0:40} | {1:8.2f}kg | {2:10} | {3:8.2f}kg |\n".format(art.piece().description() +' '+ str(attention), art.piece().poids(),art.nombre(),art.piece().poids()*art.nombre())
    
    def totaux_str(self):
        """
        Retourne un string représentant une ligne de facture avec les totaux prix et tva, Ã  imprimer en bas de la facture
        """
        nombre_article = 0
        poids_total = 0
        for art in self.__articles:
            nombre_article += art.nombre()
        for art in self.__articles:
            poids_total += art.piece().poids()*art.nombre()
        b = self.barre_str()
        b += "| {0:40} | {1:10} | {2:10} | {3:8.2f}kg |\n".format(str(len(self.articles())) +' articles','',nombre_article,poids_total )
        b += self.barre_str()
        return b
        
    # This method needs to be added during Etape 4 of the mission
    def nombre(self, pce) :
        """
        Retourne le nombre d'exemplaires de la piÃ¨ce pce dans la facture, en totalisant sur tous les articles qui concernent cette piÃ¨ce."
        """
        number = 0
        for art in self.__articles:
            if pce == art.piece():
                nombre = art.nombre()
                number += nombre
        return number

    # This method needs to be added during Etape 5 of the mission
    def livraison_str(self):
        tableau = self.entete_str()
        for art in self.__articles:
            tableau += self.article_str(art)
        tableau += self.totaux_str()
        if '(!)' in tableau:
            tableau += "(!) *** livraison fragile ***"
        return tableau
    
    def __str__(self):
        """
        Retourne la représentation string d'une facture, à imprimer avec la méthode print().
        """
        s = self.entete_fac_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.articles() :
            s += self.article_fac_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_fac_str(totalPrix, totalTVA)
        return s

    def entete_fac_str(self):
        """
        Imprime l'entête de la facture, comprenant le descriptif et les têtes de colonnes.
        """
        e = "Facture " + self.description() + "\n"
        e += self.barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","prix HTVA","TVA","prix TVAC")
        e += self.barre_str()
        return e
    
    def article_fac_str(self, art):
        """
        Retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(), art.prix_tvac())
    
    def totaux_fac_str(self, prix, tva):
        """
        Retourne un string représentant une ligne de facture avec les totaux prix et tva, à imprimer en bas de la facture
        """
        b = self.barre_str()
        b += "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix+tva)
        b += self.barre_str()
        return b
    
b = Article("ferfe",15)
print(b.prix_tvac())