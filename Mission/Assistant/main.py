def line_count(filename):
    file = open(filename, 'r')
    count = 0
    for line in file:
        count += 1
    return count


def char_count(filename):
    file = open(filename, "r")
    return len(file.read())


def loaded_file(filename):
    file = open(filename, "r")



if __name__ == "__main__":
    command = ""
    while command != "exit":
        command = input('Enter your command: ')
        parameters = command.split()

        if parameters[0] == "file":
            filename = parameters[1]
            loaded_file(filename)
            print("Loaded " + parameters[1])

        elif parameters[0] == "info":
            print(str(line_count(filename)) + " lines")
            print(str(char_count(filename)) + " caracters")

        elif parameters[0] == "dictionary":
            print("Read file as dictonary")

        elif parameters[0] == "search":
            if True:
                print(parameters[1] + " is in the dictionnary")
            else:
                print(parameters[1] + " is not in the dictionnary")



