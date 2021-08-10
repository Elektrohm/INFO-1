#Eline Nenin et Théo Denis, 17 octobre 2018
def is_adn(s):
    ''' pre : s donne une liste composée de lettres, chiffres, etc
    post : la fonction détermine s'il s'agit d'adn (composé uniquement de a,c,t,g)
    '''
    t = True
    for i in s:
        if i not in "aAcCtTgG":
            t = False
    return t

def positions(text,car):
    '''pre : s donne la suite, p donne ce qu'il faut chercher dans s
    post : la fonction renvoie dans une liste les positions d'occurrence de p dans s
    '''
    car=car.upper()
    l=[]
    for i in range(int(len(text))):
        if text[i]==car[0]:
            f=text[i:int(len(car))+i]
            if f==car:
                l.append(i)
    return(l)
        
def distance_h(text1,text2):
    '''pre : E et T donnent deux listes de base d'adn
    post : la fonction retourne none si E et T n'ont pas la même longueur. Sinon, la fonction renvoie le nombre de différence entre E et T.
    '''
    e = 0
    i = 0
    if len(text1) != len(text2) :
        return None
    else :
        while i < len(text1) :
            if text2[i] != text1[i] :
                e += 1
            i +=1
        return e

def is_palindrome(s,a,b):
    t = (b-a+1)//2
    for i in range(0,t):
        if s[a+i] != s[b-i]:
            return False
    return True

def plus_long_palindrome(te):
    po= ""
    if len(te) == 0:
        return "['']"
    if len(te) == 1:
        return "le caractère est un palindrome à lui seule"
    else :
        for i in range(0,len(te)-1):
            for j in range(i+1,len(te)):
                if is_palindrome(te,i,j) and j-i+1>len(po):
                    po = te[i:j+1]
        return po

        






    

