#recherche des racines de l'équation x**a + y**b = z**c
# Théo Denis, 2018

#code pour la question de mission globale
solutions = 0 #valeur de départ du nombre de solutions
a = int(input("Entrez la valeur de l'exposant a : "))
b = int(input("Entrez la valeur de l'exposant b : "))
c = int(input("Entrez la valeur de l'exposant c : "))
maxi = int(input("Entrez la valeur maximale pour x, y et z : "))

for x in range(1,maxi):
    for y in range(1,maxi):
        for z in range(1,maxi) :
            if x**a + y**b == z**c :
                print("x =", x, "y =", y, "z =", z)
                solutions += 1 

if solutions == 0:
    print("Aucune solution trouvee")
else:
    print(solutions, "solutions trouvees")
   