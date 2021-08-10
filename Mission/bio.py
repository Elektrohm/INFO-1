# code fait par Nouhéila Bojabza
def is_adn(text):
    if text == "":
        return False
    i = 0
    while i < len(text):
        char_i = text[i]
        if  char_i != "a" and char_i != "t" and char_i != "c" and char_i != "g"\
           and char_i != "A" and char_i != "T" and char_i != "C" and char_i != "G":
            return False
        i += 1
    return True

# print(is_adn("acgac"))
# print(is_adn("AcaA"))
# print(is_adn(" aAaza"))
# print(is_adn(""))

def positions(text, car):
    positions = []
    if len(text) < len(car):
        return positions
    
    # on met les mots en majuscule parce qu'il faut que ça passe à la fois en majuscule et en minuscule
    s_uppercase = text.upper()
    p_uppercase = car.upper()
    
    i = 0
    while i < len(text):
        if s_uppercase[i] == p_uppercase[0]:
            j = 1
            while j < len(car) and i + j < len(text):
                if p_uppercase[j] == s_uppercase[i + j]:
                    j += 1
                else:
                    break
            if j == len(car):
                positions.append(i)              
        i += 1
    return positions

# print(positions("loliLol", "lol"))

def distance_h(text1, text2):
    if len(text1) != len(text2):
        return None
    distance = 0
    i = 0
    while i < len(text1):
        if text1_uppercase[i] != text2_uppercase[i]:
            distance += 1
        i += 1
    return distance

# print(distance_h("arn" , "adn"))
# print(distance_h("arrrrn" , "adn"))
# print(distance_h("ADN" , "adn"))

def distances_matrice(l):
    matrice = []
    list = []
    i = 0
    while i < len(l):
        x = l[i]
        j = 0
        while j < len(l):
            y = l[j]
            dist = distance_h(x.upper(), y.upper())
            list.append(dist)
            j += 1
        matrice.append(list)
        list = []
        i += 1
    return matrice
#print(distances_matrice(["AG", "AT", "GT", "ACG", "ACT" ]))


