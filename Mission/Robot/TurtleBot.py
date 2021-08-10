import turtle  # une bibliothèque pour dessiner avec les turtle graphics


class TurtleBot:
    # ATTRIBUTES ADDED
    __drawcol = 'black'  # standard drawing colour
    __undrawcol = 'white'  # colour for undrawing

    def __init__(self, n):
        self.__nom__ = n  # nom du robot
        self.__t__ = turtle.Turtle()
        self.__history__ = []  # LINE ADDED

    # METHOD ADDED
    def getHistory(self):
        return self.__history__

    # METHOD ADDED
    def addHistory(self, action):
        self.__history__.append(action)

    def __str__(self):
        return str(self.getnom()) + "@" + str(self.getTurtle().position())

    def getnom(self):
        return self.__nom__

    def getTurtle(self):
        return self.__t__

    def position(self):
        return self.getTurtle().position()

    def moveforward(self, distance):
        self.addHistory(("forward", distance))  # LINE ADDED
        self.getTurtle().forward(distance)

    def movebackward(self, distance):
        self.addHistory(("backward", distance))  # LINE ADDED
        self.getTurtle().backward(distance)

    def turnright(self):
        self.addHistory(("right", 90))  # LINE ADDED
        self.getTurtle().right(90)

    def turnleft(self):
        self.addHistory(("left", 90))  # LINE ADDED
        self.getTurtle().left(90)

    # METHOD ADDED
    def __undoAction(self, action):
        # le paramtère action est un tuple comme ("right",90), etc.
        operation = action[0]
        parameter = action[1]
        if operation == "forward":
            self.movebackward(parameter)
        elif operation == "backward":
            self.moveforward(parameter)
        elif operation == "right":
            self.turnleft()
        elif operation == "left":
            self.turnright()

    # METHOD ADDED
    def unplay(self):
        self.getTurtle().color(self.__undrawcol)  # set color to undrawing colour
        undoactions = []
        history = self.getHistory()
        for i in range(len(self.getHistory()), 0, -1):  # go through list in opposite order
            undoactions.append(self.__undoAction(history[i - 1]))
        self.__history__ = []  # set history to empty after undoing
        self.getTurtle().color(self.__drawcol)  # set color back to standard drawing colour


c3powh = TurtleBot("C3-PO with history")
print(c3powh)
# prints:    C3-PO with history@(0.00,0.00)
c3powh.moveforward(50)
c3powh.turnleft()
print(c3powh)
#           C3-PO with history@(50.00,0.00)
c3powh.moveforward(50)
c3powh.turnleft()
print(c3powh)
#           C3-PO with history@(50.00,50.00)
c3powh.moveforward(50)
c3powh.turnleft()
print(c3powh)
#           C3-PO with history@(0.00,50.00)
c3powh.moveforward(50)
print(c3powh)
#           C3-PO with history@(-0.00,0.00)
c3powh.moveforward(50)
c3powh.turnright()
print(c3powh)
#           C3-PO with history@(-0.00,-50.00)
c3powh.moveforward(50)
c3powh.turnright()
print(c3powh)
#           C3-PO with history@(-50.00,-50.00)
c3powh.moveforward(50)
c3powh.turnright()
print(c3powh)
#           C3-PO with history@(-50.00,0.00)
c3powh.moveforward(50)
c3powh.turnright()
print(c3powh)
#           C3-PO with history@(-0.00,0.00)

print(c3powh.getHistory())
# [('forward', 50), ('left', 90), ('forward', 50), ('left', 90), ('forward', 50), ('left', 90), ('forward', 50), ('forward', 50), ('right', 90), ('forward', 50), ('right', 90), ('forward', 50), ('right', 90), ('forward', 50), ('right', 90)]
c3powh.unplay()
# undoes everything that was drawn by redrawing it in opposite order
print(c3powh)
# C3-PO with history@(0.00,-0.00)
print(c3powh.getHistory())
# []