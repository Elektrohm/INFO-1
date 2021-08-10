#Théo Denis, Loris Deru, 1/11/2018
def file(name):
    try :
        data = open(name,"r")
        print('Loaded', name)
        data.close()
    except IOError:
        print("le fichier n'existe pas ou vous l'avez mal ortographié")

def info(name):
    i = 0
    j = 0
    data = open(name,'r')
    for line in data:
        i += 1
        for characters in line:
            j += 1
    data.close()
    print(i,"lines")
    print(j,"caractères")
    
def dictionary(name) :
    global ma_liste
    ma_liste=[]
    global data
    data = open(name,'r')
    for ligne in data:
        a=ligne.replace("<code>;</code>","")
        b=a.split()
        for i in range(len(b)):
            c=b[i]
            ma_liste.append(c)
    ma_liste.sort()
    if len(ma_liste)==0:
        print('le fichier ne contient pas de dictionnaire ou de mots dedans')
    if len(ma_liste) > 0:
        print('le fichier est lu comme un dictionnaire')
    
def search(word):
    try :
        first = 0
        last = len(ma_liste)-1
        found = False

        while first<=last and not found:
            middle = (first + last)//2
            if ma_liste[middle] == word:
                found = True
            else:
                if word < ma_liste[middle]:
                    last = middle-1
                else:
                    first = middle+1
        
        if found == False:
            lettre = True
            while lettre:
                if word[0] != ma_liste[first][0]:
                    first = first - 1
                if word[0] == ma_liste[first][0]:
                    lettre = False
            print('le mot le plus proche est', ma_liste[first].strip('0'))
        if found == True:
            print('le mot', ma_liste[middle],'est présent dans le dictionnaire')
    except:
        print("vous n'avez pas demandé de travailler avec le dictionnaire, entrer dictionary")
        
def sum(l): #a modifier pour nombre à deux chiffres et plus
    sum = 0
    for i in l:
        sum += int(i)
    return (sum)

def avg(l):
    sum = 0
    for i in l:
        sum += int(i)
    moyenne = sum/(len(l))
    return (moyenne)

def table(n):
    for i in range(11):
        print(("|{0:<{1}}|".format(int(n)*i,len(str(n))+1)))
        
def help():
    print('')
    print('les commandes comprises dans cet assistant sont les suivantes :')
    print("file name, cette commande permet d'ouvrir un fichier sur lequel vous voulez travailler")
    print("info, cette commande vous donne le nombre de lignes et de caractère dans le fichier")
    print("dictionary, vous permet d'utiliser le fichier comme dictionnaire à partir de maintenant")
    print("search word, vous trouve le mot le plus proche de celui que vous avez entré même s'il est mal ortographié")
    print("sum <number1>...<numbern>, calcule la somme des nombres que vous avez entré")
    print("avg <number1>...<numbern>, calcule la moyenne des nombres que vous avez entré")
    print("table <number>, affiche la table de multiplication jusqu'à 10 du nombre entré")
    print("exit, vous permet d'arrêter l'outil")
    print('')
    
def exit():
    try :
        data.close()
    except:
        print("il n'y avait rien à fermer comme fichier")

if __name__ == "__main__":
    i = 0
    t = True
    while t:
        if i == 0:
            print('bienvenu dans cet assistant')
        command = input('enter your command: ')
        if str(command.split()[0]) == 'file':
            try :
                global name
                name = str(command.split()[1])
                command = 'file'
            except :
                print("entrer la commande en entier")
        if str(command.split()[0]) == 'search':
            try :
                global word
                word = command.split()[1]
                command = 'search'
            except :
                print("vous n'avez pas entrez le mot à chercher")
        if str(command.split()[0]) == 'sum':
            global l
            global tableau
            l = []
            tableau = command.split()
            for i in range(1,len(tableau)):
                if str(i) in '123456789':
                    l.append(tableau[i])
            command = 'sum'
        if str(command.split()[0]) == 'avg':
            global k
            global chaise
            k = []
            chaise = command.split()
            for i in range(1,len(chaise)):
                if str(i) in '123456789':
                    k.append(chaise[i])
            command = 'avg'
        if str(command.split()[0]) == 'table':
            global n
            n = command.split()[1]
            command = 'table'
        try:
            if command == 'file':
                file(name)
            if command == 'info':
                info(name)
            if command == 'dictionary':
                dictionary(name)
            if command == 'search':
                search(word)
            if command == 'sum':
                print(sum(l))
            if command == 'avg':
                print(avg(k))
            if command == 'table':
                table(n)
            if command == 'help':
                help()
            if command == 'exit':
                exit()
                t = False
            if command != 'file'and command !='info' and command !='dictionary' and command !='search' and command !='sum' and command !='avg' and command !='help' and command != 'table' and command !='exit':
                print("cette commande n'existe pas")
            i +=1
        except NameError:
            print("vous n'avez pas demander de travailler avec un fichier auparavant, veuillez d'abord demander l'ouverture d'un fichier")
            i += 1
        except ValueError:
            print("ce que vous avez rentré après sum/avg/talbe n'est pas un chiffre, veuillez entrer un chiffre")
            i += 1
        except FileNotFoundError:
            print("vous n'avez toujours pas entré un nom valable de fichier pour pouvoir travailler avec info/dictionary")
        except IndexError:
            print("vous n'avez pas entrer la commande en entier")
        except:
            print("Une erreur s'est produite")




