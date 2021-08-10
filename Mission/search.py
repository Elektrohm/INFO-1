#Theo Denis, Eline Nenin, 04/11/2018
#mission 7, travaille sur le programme search
import string
def readfile(filename):
    """pre : filename est le nom d'un fichier présent sur le pc
    post : retourne une liste de chaque ligne du fichier avec tous les éléments de la ligne"""
    l = []
    file = open(filename,'r')
    for line in file:
        l.append(line)
    file.close()
    return l

def remove_punctuation(line):
    """pre : line est une chaine de caractères
    post : retourne une chaine de caractères sans les ponctuations"""
    s_without_punct = ""
    for letter in line:
        if letter == "'":                         #cette ligne permet de ne pas coller un mot comme c'est, sans ceci "c'est" deviendrai "cest" or ce n'est pas un mot
            s_without_punct += " "
        if letter not in string.punctuation:
            s_without_punct += letter             
    return s_without_punct


def get_words(line):
    """pre : line est une chaine de caractères
    post : retourne une liste des mots sans la ponctuation"""
    new_line = remove_punctuation(line)
    new_line = new_line.lower()
    k = (new_line.split())  
    return k

def create_index(filename):
    """pre : filename est un fichier présent sur l'ordinateur
    post : retourne un dictionnaire avec les mots du fichier pour chaque mot un dictionnaire imbriqué avec les lignes où il se trouve
           et le nombre d'occurence dans chaque ligne'"""
    global index
    index = {}
    j = -1                                         #permet de commencer la ligne à 0 au premier passage dans la boucle
    file = open(filename,'r')
    for line in file:
        b = get_words(line)
        j += 1                                     #permet qu'à chaque passage dans la boucle le numéro de la ligne augmente de 1 comme il doit le faire
        for i in b:
            if index.get(i,[]) == []:
                index[i] = {j:1}
            elif index.get(i,[]) != [] :
                if j in index.get(i,0):            #permet d'augmenter la valeur de 1 si le mot est déjà présent dans le dictionnaire est qu'on est toujours sur la même ligne 
                    index.get(i,0)[j] += 1
                if j not in index.get(i,0):        #permet de créer une nouvelle relation dans le dictionnaire si le mot est déjà présent dans le dictionnaire mais qu'on 
                    p = index.get(i,0)             # n'est plus sur la même ligne
                    p[j] = 1
                    index[i] = p
    file.close()
    return index
    

def get_index(word):
    """pre : word est un mot
    post : retourne le dictionnaire des lignes où il se trouve et le nombre d'occurence dans chaque ligne'"""
    lst_index = index.get(word)
    return lst_index
    
def all_index(words):
    """pre : words est une liste de mots
    post : retourne un dictionnaire dans lequel se trouve les numéro des lignes auxquels correspondent le nombre de mots de words dans cette ligne, chaque mot compte pour 1"""
    try :
        global dic_of_indexes
        dic_of_indexes = {}
        for i in words:
            n = get_index(i)
            for k in n:
                if dic_of_indexes.get(k,[]) == []:
                    dic_of_indexes[k] = 1
                elif dic_of_indexes.get(k,[]) != [] :        #permet d'augmenter la valeur de 1 à l'occurence de la ligne dans les éléments  
                    new = dic_of_indexes.get(k,0)            #si le n° de ligne est déjà présent dans le dictionnaire
                    new += 1
                    dic_of_indexes[k] = new
        return dic_of_indexes
    except TypeError:
        print("le mot", i,"n'est pas présent dans le fichier")
        return {}
        

def final_lst(words):
    """pre: words est une liste de mots
    post : retourne la liste des lignes où tous les éléments de words se trouvent si all_index(words) s'est exécuté avant'"""
    length = len(words)
    lst = []
    for k in dic_of_indexes:
        if dic_of_indexes[k] == length:
            lst.append(k)
    return lst
    
def get_lines(words, index):
    """pre : words est une liste de mots, index est un dictionnaire avec les mots du fichier pour chaque mot un dictionnaire imbriqué avec les lignes où il se trouve
             et le nombre d'occurence dans chaque ligne
       post : retourne la liste des lignes où tous les éléments de words se trouvent '''"""
    all_index(words)
    p = final_lst(words)
    return p

def recreate_list(lst):
    """pre : lst est un string composé d'une liste avec des mots dedans
    post : retourne la liste avec les mots """""
    words = lst
    word = ""
    for i in range(len(words)):
        if words[i] == ",":
            word += ' '
        if words[i] in "azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBNéîè":
            word += words[i]
    l = word.split()
    return l

t = True
i = 0
j = 0
while t:
    if i == 0:
        try:
            if j == 0:
                print("si vous voulez sortir après avoir chercher vos listes, entrez exit")
                j += 1
            if j>0:
                filename = input('quel est le nom du fichier ? ')
                create_index(filename)
                i += 1
        except:
            print("veillez à donner un nom de fichier valide, vérifiez que vous l'avez bien ortographié")
    if i == 1:
        try :
            lst = input("entrez une liste de mots par exemple ['bonjour','ça'] , svp : ")
            words = recreate_list(lst)
            if words[0] != 'exit':
                print(get_lines(words,index))
            if words[0] == 'exit':
                t = False
        except IndexError :
            print("vous n'avez pas rentré de mots, ou bien vous avez accidentellement appuyé sur enter")
        except:
            print("erreur, et merde")
    
    
