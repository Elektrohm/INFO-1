from linked_list import LinkedList


class OrderedLinkedList(LinkedList):
    """
    Implémentation d'une structure de données représentant une liste chainée ordonnée,
    c'est-à-dire une liste chainée normal mais où les élément stockées dans les noeuds
    sont ordonnées par leur valeur. Le noeud contenant la plus petite valeur se trouve
    en tête de la liste.
    """

    def __init__(self, lst=[]):
        """
        Initialises a new ordered linked list object, with a given list of elements lst.
        @pre:  lst is a list of elements, comparable by == and <
        @post: A new ordered linked list object has been initialised.
               Its length is equal to the number of elements in lst.
               The data elements stored in the ordered linked list's nodes correspond to
               those of the list lst, but appear in the ordered linked list from lowest
               to highest value.
               If no list lst is passed as argument, the newly created ordered linked list
               will have 0 length, contain no nodes and its head will point to None.
        """
        super().__init__(lst)

    # def size(self) : inherited from superclass
    # def inc_size(self) : inherited from superclass
    # def dec_size(self) : inherited from superclass
    # def first(self) : inherited from superclass
    # def print(self) : inherited from superclass
    # def set_first(self,n) : inherited from superclass

    def add_first(self, value):
        """
        Adds a new Node with given value to the front of this ordered linked list.
        This is an auxiliary method that is only supposed to be called if we know
        that the value is smaller than all the values already contained in the
        ordered linked list, so that the overall order is maintained.
        @pre: self is a (possibly empty) OrderedLinkedList.
        @post: A new Node object is created with the given value.
               This new Node is added to the front of the ordered linked list.
               The length counter has been incremented.
               The head of the list now points to this new node.
        """
        super().add(value)  # the add method on LinkedList adds to the front

    def remove_first(self):
        """
        Removes the node at the start of the list.
        Leaves the ordered list intact if already empty.
        """
        super().remove()  # the remove method on LinkedList removes the first node

    # def add(self,value) redefines method from superclass
    # NOTE : THIS IS IMPLEMENTATION IS THE SAME AS THE INSERT METHOD
    #        FOR LINKEDLIST THAT WAS ASKED IN ONE OF THE EXERCICES
    def add(self, s):
        """
        Adds a node with value s at the right position in an already sorted ordered linked list.
        """
        current = self.first()
        # case 1 : list is empty, add new node as first node
        if self.size() == 0:
            self.add_first(s)
            return
        # case 2 : list is not empty, element to be added is smaller than all existing ones
        elif s < current.value():
            self.add_first(s)
            return
        # case 3 : list is not empty, element is larger than value of current element
        else:
            self.inc_size()  # ne pas oublier d'incrémenter la taille de la liste
            nxt = current.next()
            # loop until we are at the end to find where to insert element
            while nxt is not None:
                # case 3a : we found the place where to insert
                if s < nxt.value():
                    # insérer entre current et next
                    n = self.Node(s, nxt)
                    current.set_next(n)
                    return
                # case 3b : we need to look further
                current = nxt
                nxt = nxt.next()
            # si on arrive ici on est au dernier élément
            current.set_next(self.Node(s, None))
            return

    # def remove(self,value) redefines method from superclass
    def remove(self, value):
        """
        Removes the first node with the given value from the ordered linked list.
        Leaves the list intact if already empty.
        @pre:  -
        @post: The first node with the given value as cargo was removed from the
               ordered linked list.
               The removed node, with next pointer set to None, is returned as result.
               In case multiple nodes with this value exist, only the first one is removed.
               The list is left intact if no such node exists or if the list is empty.
               In that case, None is returned as result.
        """
        node = self.first()
        # case 0 : in case value is None, nothing needs to be removed and return None
        if value is None:
            return None
        # case 1 : in case of empty list, do nothing and return None
        if node is None:
            return None
        # case 2 : list has at least one element and node to be removed is the first element
        if node.value() == value:
            self.set_first(node.next())  # set head of the ordered linked list to next node
            self.dec_size()  # decrease lenth of ordered linked list
            node.set_next(None)  # remove next pointer from the node to be removed
            return node  # return the removed node
        # case 3 : list has at least one element and node to be removed is not the first element
        previous = node
        node = node.next()
        while node is not None:
            # case 3a : the node contains the value to be removed
            if node.value() == value:
                previous.set_next(node.next())  # unlink the node to be removed
                self.dec_size()  # decrease lenth of ordered linked list
                node.set_next(None)  # remove next pointer from the node to be removed
                return node  # return the removed node
            # case 3b : loop to find first occurence further in list
            else:
                node = node.next()
        # case 4 : return None if value was not found in the list
        return None

    # nouvelle méthode qu'on n'utilise pas vraiment dans cette mission
    def find(self, value):
        """
        Finds the first node with given value and returns it.
        Returns None if no node with that value exists.
        """
        node = self.first()
        # case 1 : in case of empty list, do nothing and return None
        if node is None:
            return None
        # case 2 : in case of empty list, do nothing and return None
        while node is not None:
            # case 3a : the current node contains the value to be removed
            if node.value() == value:
                return node
            # case 3b : loop to find first occurence further in list
            else:
                node = node.next()
        # case 4 : return None if value was not found in the list
        return None
