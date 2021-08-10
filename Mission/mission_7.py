#mission 7 : exercices
def equal(l,d):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if d.get((i,j),0) != l[i][j]:
                print(d.get((i,j),0))
                return False
    return True

def create_dict(l):
    d = {}
    for i in range(len(l)):
        if l[i][0] in d:
            d.get(l[i][0],[]).append(l[i][1])
        if l[i][0] not in d:
            d[l[i][0]] = [l[i][1]]
    return d

def create_dict_max(l):
    d = {}
    for i in range(len(l)):
        if l[i][0] in d:
            if l[i][1] >= d.get(l[i][0]):
                d[l[i][0]]=l[i][1]
        if l[i][0] not in d:
            d[l[i][0]] = l[i][1]
    return d

def create_dictionary(filename):
    global dictionary
    dictionary={}
    file = open(filename,'r')
    for i in file:
        b = i.split()
        for j in b:
            if j in dictionary:
                dictionary[j] += 1
            if j not in dictionary:
                dictionary[j] = 1
    file.close()
    return dictionary

def occ(dictionary,word):
    count = 0
    for k in dictionary.keys():
            if k == word:
                count = dictionary[k]
    return count

def get_country(l,name):
    for i in range(len(l)):
        if l[i]['City'] == name:
            return l[i]['Country']
    return False

def recreate_list():
    word = ""
    words = input("entrez votre liste")
    for i in range(len(words)):
        if words[i] == ",":
            word += ' '
        if words[i] in "azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN":
            word += words[i]
    l = word.split()
    return l

"bilan final"

def QBF(words,k):
    global d
    d = {}
    for i in words:
        if d.get(i,[]) == []:
            d[i] = 1
        elif d.get(i,[]) != []:
            d[i] += 1

def create_list(d,k):
    l = []
    final_lst = []
    for i in d:                                       
        l.append((d.get(i),i))
    l = sorted(l,reverse=True)
    comparatif = l[k-1][0]
    a = 0
    for i in range(k,len(l)):
        if l[i][0] == comparatif:
            a += 1
    if a > 0:
        return l
    if a == 0:
        for i in range(k):
            final_lst.append(l[i])
        return final_lst

def topk_words(words,k):
    QBF(words,k)
    l = create_list(d,k)
    return l

print(topk_words(["while", "the", "congress", "of", "the", "republic", "endlessly", "debates", "this", "alarming", "chain", "of", "events", "the", "supreme", "chancellor", "has", "secretly", "dispatched", "two", "jedi", "knights"],3))


    


    
    
    
    
    
    