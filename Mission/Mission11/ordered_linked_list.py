class OrderedLinkedList:
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
        self.__length = 0  # current length of the linked list
        self.__head = None  # pointer to the first node in the list
        for e in lst:  # initialize the list,
            self.add(e)  # by adding elements one by one

    def size(self):
        """
        Accessor method which returns the number of nodes contained in this ordered linked list.
        @pre:  -
        @post: Returns the number of nodes (possibly zero) contained in this ordered linked list.
        """
        return self.__length

    def first(self):
        """
        Accessor method which returns the first node of this ordered linked list,
        that is, the node which contains the smallest value.
         @pre:  -
        @post: Returns a reference to the head of this ordered linked list,
               or None if the ordered linked list contains no nodes.
        """
        return self.__head

    def __add_first(self, value):
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
        node = self.Node(value, self.__head)
        if self.__head == None:  # when this is the first element being added,
            self.__last = node  # set the last pointer to this new node
        self.__head = node
        self.__length += 1

    def print(self):
        """
        Prints the contents of this ordered linked list and its nodes.
        @pre:  self is a (possibly empty) OrderedLinkedList
        @post: Has printed a space-separated list of the form "[ a b c ... ]",
               where "a", "b", "c", ... are the string representation of each
               of the linked list's nodes.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]".
        """
        self.print_avec_separateur(" ")

    def print_backward(self):
        """
        Prints the contents of this ordered linked list and its nodes, back to front.
        @pre:  self is a (possibly empty) OrderedLinkedList.
        @post: Has printed a space-separated list of the form "[ ... c b a ]",
               where "a", "b", "c", ... are the string representation of each
               of the ordered linked list's nodes. The nodes are printed in opposite order:
               the last nodes' value are printed first.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]".
        """
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_backward()
        print("]")

    def print_avec_separateur(self, separateur):
        print("[", end=" ")
        if self.__head is not None:
            self.__head.print_list_avec_separateur(separateur)
        print("]")

    def print_avec_virgule(self):
        self.print_avec_separateur(", ")

    def __remove_first(self):
        """
        Removes the node at the start of the list.
        Leaves the ordered list intact if already empty.
        """
        if self.__head is not None:
            self.__length -= 1
            self.__head = self.__head.next()
        if self.__length == 0:  # when there are no more elements in the list,
            self.__last = None  # remove the pointer to the last element

    def add(self, s):
        """
        Adds a node with value s at the right position in an already sorted ordered linked list.
        """
        current = self.first()
        # case 1 : list is empty, add new node as first node
        if self.size() == 0:
            self.__add_first(s)
            return
        # case 2 : list is not empty, element to be added is smaller than all existing ones
        elif s < current.value():
            self.__add_first(s)
            return
        # case 3 : list is not empty, element is larger than value of current element
        else:
            self.__length += 1
            nxt = current.next()
            # loop until we are at the end to find where to insert element
            while nxt is not None:
                if s < nxt.value():
                    n = self.Node(s, nxt)
                    current.set_next(n)
                    return
                current = nxt
                nxt = nxt.next()
            current.set_next(self.Node(s, None))
            return

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
        # case 1 : in case of empty list, do nothing and return None
        if node is None:
            return None
        # case 2 : list has at least one element and node to be removed is the first element
        if node.value() == value:
            self.__head = node.next()
            self.__length -= 1
            node.set_next(None)
            return node
        # case 3 : list has at least one element and node to be removed is not the first element
        previous = node
        node = node.next()
        while node is not None:
            if node.value() == value:
                previous.set_next(node.next())
                self.__length -= 1
                node.set_next(None)
                return node
            else:
                node = node.next()
        return None

        ##############

    # Node class #
    ##############

    class Node:

        def __init__(self, cargo=None, next=None):
            """
            Initialises a new Node object.
            @pre:  -
            @post: A new Node object has been initialised.
                   A node can contain a cargo and a reference to another node.
                   If none of these are given, the node is initialised with empty cargo (None) and no reference (None).
            """
            self.__cargo = cargo
            self.__next = next

        def value(self):
            """
            Returns the value of the cargo contained in this node.
            @pre:  -
            @post: Returns the value of the cargo contained in this node, or None if no cargo  was put there.
            """
            return self.__cargo

        def next(self):
            """
            Returns the next node to which this node links.
            @pre:  -
            @post: Returns the node to which this node is linked with its next pointer, or None if that pointer is None.
            """
            return self.__next

        def set_next(self, node):
            """
            Sets the next node to which this node links to a new node.
            @pre:  -
            @post: The node to which this node is linked next, has been set to the new node passed as parameter.
                   Can also be set to None by passing None as parameter.
            """
            self.__next = node

        def __str__(self):
            """
            Returns a string representation of the cargo of this node.
            @pre:  self is a (possibly empty) Node object.
            @post: Returns a print representation of the cargo contained in this Node.
            """
            return str(self.value())

        def __eq__(self, other):
            if other is not None:
                return self.value() == other.value()
            else:
                return False

        def print_list(self):
            """
            Prints the cargo of this node and then recursively of each node connected to this one.
            @pre:  self is a node (possibly connected to a next node).
            @post: Has printed a space-separated list of the form "a b c ... ",
                   where "a" is the string-representation of this node,
                   "b" is the string-representation of my next node, and so on.
                   A space is printed in-between the printed value.
            """
            self.print_avec_separateur(" ")

        def print_backward(self):
            """
            Recursively prints the cargo of each node connected to this node (in opposite order),
            and then prints the cargo of this node as last value.
            @pre:  self is a node (possibly connected to a next node).
            @post: Has printed a space-separated list of the form "... c b a",
                   where a is my cargo (self), b is the cargo of the next node, and so on.
                   The nodes are printed in opposite order: the last nodes' value is printed first.
            """
            head = self
            tail = self.__next  # go to my next node
            if tail is not None:  # as long as the end of the list has not been reached
                tail.print_backward()  # recursively print remainder of the list backwards
            print(head, end=" ")  # print my head

        def print_avec_separateur(self, separateur):
            print("[", end=" ")
            if self.__head is not None:
                self.head.print_list_avec_separateur(separateur)
            print("]")

        def print_list_avec_separateur(self, separateur):
            head = self
            tail = self.__next  # go to my next node
            if tail is not None:  # as long as the end of the list has not been reached
                print(head, end=separateur)  # print my head, with separateur
                tail.print_list_avec_separateur(separateur)  # recursively print remainder of the list
            else:  # print the last element
                print(head, end=" ")  # print my head, with a space


##########################################
# Creating and using LinkedList and Node #
##########################################

l = OrderedLinkedList()
l.print()
# [ ]
l.print_backward()
# [ ]
print(l.size())
# 0
l = OrderedLinkedList()
l.add(3)
l.add(2)
l.add(1)
l.print()
# [ 1 2 3 ]
l.print_backward()
# [ 1 2 3 ]
print(l.size())
# 3

###############################
# Question préparatoire 2 + 3 #
###############################

l = OrderedLinkedList()
l.add(3)
l.add(2)
l.add(1)

l.print()
# [ 1 2 3 ]
l.print_avec_virgule()
# [ 1, 2, 3 ]
l.print_avec_separateur(", ")
# [ 1, 2, 3 ]
l.print_avec_separateur(" ")
# [ 1 2 3 ]
l.print_avec_separateur(" - ")
# [ 1 - 2 - 3 ]

l = OrderedLinkedList()

l.print()
# [ ]
l.print_avec_virgule()
# [ ]
l.print_avec_separateur(", ")
# [ ]
l.print_avec_separateur(" ")
# [ ]

###########################
# Question préparatoire 4 #
###########################

l = OrderedLinkedList([1])
l.print()
# [ 1 ]
l = OrderedLinkedList([2, 1])
l.print()
# [ 1 2 ]
l = OrderedLinkedList([1, 2])
l.print()
# [ 1 2 ]
l = OrderedLinkedList([1, 2, 3])
l.print()
# [ 1 2 3 ]
l = OrderedLinkedList([])
l.print()
# [ ]
l = OrderedLinkedList([1, 17, 5, 4, 16, 100, 0, -1])
l.print()
# [ -1 0 1 4 5 16 17 100 ]


###########################
# Question préparatoire 5 #
###########################

l = OrderedLinkedList([1, 2, 3])
l.print()
l.remove(1)
l.print()
# [ 2 3 ]
l.remove(3)
print(l.size())
# 1
l.print()
# [ 2 ]
l.remove(3)
l.print()
# [ 2 ]
l.remove(2)
l.print()
# [ ]
print(l.size())
# 0
l.remove(2)
l.print()
# [ ]
print(l.size())
# 0


###########################
# Question préparatoire 6 #
###########################

l = OrderedLinkedList([1, 2, 3])
l.print()
# [ 1 2 3 ]

l.add(4)
l.print()
# [ 1 2 3 4 ]
print(l.size())
# 4

l.add(0)
l.add(5)
l.print()
# [ 0 1 2 3 4 5 ]
print(l.size())
# 6

l = OrderedLinkedList([1, 2])
l.remove(2)
l.remove(1)
l.add(1)
l.add(2)
l.print()
# [1, 2]

###########################
# Question préparatoire 9 #
###########################

l = OrderedLinkedList(["abc", "def", "xyz"])
l.add("aaa")
l.add("ghi")
l.add("def")
l.add("zzz")
l.print()
