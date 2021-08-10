#affiche un tableau des carrés et de la somme des carrés de 1 à 10
import math
a = 1 #valeur de départ
addition = 1

while a >=1 and a <= 10:
    print(a, "\t", a**2, "\t", addition,"\t", a*(a + 1)*(2*a + 1)//6)
    a = a + 1
    addition = addition + a**2
"""print("réussi")

i,n,sum = 1,10,0
while i <= 10 :
    sum += i**2
    print(i, "\t", i**2, "\t", sum, "\t", i*(i+1)*(2*i+1)//6)
    i+=1
"""