def create_file(lst):
    file = open('test.txt', 'w')
    for line in lst:
        file.write(line + "\n")


def acrostiche(file_name): # Ne pas effacer cette ligne
    """
    @pre:  file_name est le nom d'un fichier de texte
    @post: Retourne une chaîne de caractères contenant la première lettre
          de chaque ligne dans le fichier de texte,
          pour les lignes qui contiennent au moins un caractère.
          Retourne -1 en cas d'erreur d'accès au fichier.
    """
    try:
        with open(file_name, 'r') as file:
            lst_of_lines = file.readlines()
            string_builder = []
            for line in lst_of_lines:
                for char in line:
                    if char.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        string_builder.append(char)
                        break
            return "".join(string_builder)
    except FileNotFoundError:
        return -1


if __name__ == '__main__':

    create_file(["","Elizabeth it is in vain you say.","'Love not'-thou sayest it in so sweet a way:","In vain those words from thee or L.E.L.","Zantippe's talents had enforced so well:","Ah! if that language from thy heart arise,","Breath it less gently forth-and veil thine eyes.","Endymion, recollect, when Luna tried","To cure his love-was cured of all beside-","His follie-pride-and passion-for he died.",""])

    print(acrostiche('test.txt'))
    # ELIZABETH
    print(acrostiche("gregerg"))
    # -1