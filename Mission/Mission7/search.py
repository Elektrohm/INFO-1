import string


def readfile(filename):
    """
    retourne une liste des lignes dans le fichier avec le nom filename
    :param filename: string, chemin du fichier dans l'ordi
    :return: liste, lignes dans le fichier
    """
    try:
        with open(filename, 'r') as file:
            l = []
            for line in file:
                l.append(line.strip())
            return l
    except FileNotFoundError:
        return None


def remove_punctuation(line):
    """pre : line est une chaine de caractères
    post : retourne une chaine de caractères sans les ponctuations"""
    s_without_punct = ""
    for letter in line:
        if letter == "'":
            s_without_punct += ""
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct


def get_words(line):
    """
    retourne une liste des mots dans la chaîne line, en minuscules, et sans ponctuation.
    :param line: string, une chaine de caractères qu'on veut récupérer en liste
    :return: list, listes des mots dans line, en minuscules et sans ponctuation
    """
    new_line = remove_punctuation(line)
    new_line = new_line.lower()
    k = new_line.split()
    return k


def create_index(filename):
    """
    Crée un index pour le fichier filename de la forme : {mot : {ligne : occurence mot}}
    :param filename: string, chemin où se trouve le fichier
    :return: dictionary, dictionnaire index
    """
    with open(filename, 'r') as file:
        index = {}
        ListOfLines = readfile(filename)
        for i in range(len(ListOfLines)):               # i, indice de la ligne
            words = get_words(ListOfLines[i])
            for word in words:
                if index.get(word, 'IsNotPresent') == 'IsNotPresent':
                    index[word] = {i: 1}
                else:
                    if i in index.get(word, 'ExistingLine'):      # si la ligne existe déjà alors occurs +1
                        index.get(word)[i] += 1
                    else:
                        index.get(word)[i] = 1
        return index


def get_lines(words, index):
    """
    Retourne la liste des lignes où tous les mots dans words sont présent
    :param words: liste, mots dont on cherche la co-présence
    :param index: dictionary, flemme
    :return: flemme
    """
    dicofIndex = {}
    commonIndex = []
    for word in words:
        if index.get(word, 'NotPresent') == 'NotPresent':
            return []
        else:
            for i in index.get(word):
                if dicofIndex.get(i, 'NotPresent')=='NotPresent':
                    dicofIndex[i] = 1
                else:
                    dicofIndex[i] += 1

    for key, value in dicofIndex.items():
        if value == len(words):
            commonIndex.append(key)
    return commonIndex


if __name__ == '__main__':
    print(readfile("nope.txt"))
    print(readfile("text_example_2.txt"))
    print(get_lines(['the','republic'], create_index('text_example_2.txt')))
