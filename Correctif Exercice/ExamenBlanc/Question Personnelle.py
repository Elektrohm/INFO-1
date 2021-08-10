class Node:
    def __init__(self, cargo, next=None, previous=None):
        self.__cargo = cargo
        self.__next = next
        self.__previous = previous

    def get_cargo(self):
        return self.__cargo

    def get_next(self):
        return self.__next

    def get_previous(self):
        return self.__previous

    def set_next(self, next):
        self.__next = next

    def set_previous(self, previous):
        self.__previous = previous

    def __str__(self):
        return f"<-{self.get_cargo()}->"


class DoubleLinkedList:
    def __init__(self, head=None):
        if head == None:
            self.__length = 0
        else:
            self.__length = 1
        self.__head = head

    def add(self, cargo):
        node = Node(cargo)
        if self.__length == 0:
            self.__head = node
        else:
            self.__head.set_previous(node)
            node.set_next(self.__head)
            self.__head = node
        self.__length += 1

    def __str__(self):
        courreur = self.__head
        stringbuilder = []
        stringbuilder.append(str(courreur))
        while courreur.get_next() != None:
            print(stringbuilder)
            courreur = courreur.get_next()
            stringbuilder.append(str(courreur))
        return "".join(stringbuilder)


if __name__ == '__main__':

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    test = DoubleLinkedList(n1)

    print(n1)

    test.add(n1)
    test.add(n2)
    test.add(n3)

    print(test)

