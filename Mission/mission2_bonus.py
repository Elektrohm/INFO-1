#code avec la contrainte que les solutions ne doivent avoir aucun diviseur commun hormis 1
#je rejette les solutions du style : 5, 6, 10 car 6 et 10 ont un diviseur commun qui est 2
#le diviseur commun dans mon cas ne doit pas être strictement commun aux 3 nombres

a = int(input("Entrez la valeur de l'exposant a : "))                    #initialisation des variables 
b = int(input("Entrez la valeur de l'exposant b : "))
c = int(input("Entrez la valeur de l'exposant c : "))
maxi = int(input("Entrez la valeur maximale pour x, y et z : "))
solution = 0

for x in range(1,maxi):                                                   #recherche des solutions de l'équation
    for y in range(1,maxi):
        for z in range(1,maxi) :
            divcommun = False
            i = 2
            if x**a + y**b == z**c :
                while i <= max(x,y,z) and divcommun == False:                                 #vérification qu'aucune des solutions n'a de diviseurs commun
                    if (x%i==0 and y%i==0) or (x%i==0 and z%i==0) or (y%i==0 and z%i==0):
                        divcommun = True
                    i+=1
                if (divcommun != True):                                                       #augmentation en cas d'une solution trouvée
                    print("x =", x, "y =", y, "z =", z)
                    solution += 1
                    
if solution == 0:                                                        #affichage des solutions
    print("Aucune solution trouvee")
else:
    print(solution, "solutions trouvees")
                