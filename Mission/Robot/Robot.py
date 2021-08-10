import turtle  # une bibliothèque pour dessiner avec les turtle graphics
from graphics import *  # une bibliothèque pour dessiner des figures simple sur un plan XY
import math  # nous avoins besoin des fonctions cos et sin pour notre calcul de la position d'un point


# Cette classe contient le code commun aux classes XYRobot et TurtleBot
# en particulier le code pour gérer le mémoire qui retient les actions
# déjà exécutées.
class Robot:
    __drawcol = 'black'  # couleur standard pour dessiner
    __undrawcol = 'yellow'  # couleur pour effacer

    def __init__(self, n):
        self.__nom = n  # nom du robot
        self.__history = []  # mémoire du robot

    @classmethod
    def getdrawcol(cls):
        return cls.__drawcol

    @classmethod
    def getundrawcol(cls):
        return cls.__undrawcol

    def getnom(self):
        return self.__nom

    def __str__(self):
        return str(self.getnom())

    def getHistory(self):
        return self.__history

    def addHistory(self, action):
        self.__history.append(action)

    def clearHistory(self):
        self.__history = []

    def moveforward(self, distance):
        self.addHistory(("forward", distance))

    def movebackward(self, distance):
        self.addHistory(("backward", distance))

    def turnright(self):
        self.addHistory(("right", 90))

    def turnleft(self):
        self.addHistory(("left", 90))

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

    def unplay(self):
        undoactions = []
        history = self.getHistory()
        for i in range(len(self.getHistory()), 0, -1):  # go through list in opposite order
            undoactions.append(self.__undoAction(history[i - 1]))
        self.clearHistory()  # set history to empty after undoing


# Exemple d'utilisation de cette classe (il suffit d'exécuter ce fichier)
if __name__ == '__main__':
    robby = Robot("Robby the robot")
    robby.moveforward(100)
    # nothing happens
    robby.turnright()
    # nothing happens
    robby.moveforward(100)
    # nothing happens
    print(robby)
    print(robby.getHistory())


# La classe XYRobot hérite de la classe Robot qui contient le
# code commun avec la classe TurtleBot

class XYRobot(Robot):

    # CLASS ATTRIBUTES MOVED TO SUPER CLASS

    # MODIFIED TO MAKE SUPER CALL
    def __init__(self, n):
        super().__init__(n)
        self.__x = 0  # position x du robot
        self.__y = 0  # position y du robot
        self.__angle = 0  # angle en degres radius
        self.__win = GraphWin()  # graphics window sur laquelle on va tracer le robot
        self.__col = self.getdrawcol()  # setting the colour to the standard drawing colour

    # MODIFIED TO MAKE SUPER CALL
    def __str__(self):
        return super().__str__() + "@" + str(self.position()) + " angle: " + str(self.getangle())

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def getanglerad(self):
        """returns the angle in radials"""
        return self.__angle

    def getangle(self):
        """returns the angle in degrees"""
        return (self.__angle * 180 / math.pi) % 360

    def setx(self, x):
        self.__x = x

    def sety(self, y):
        self.__y = y

    def position(self):
        return (self.getx(), self.gety())

    def drawFrom(self, oldx, oldy):
        # print("Drawing "+self.getnom()+" from "+str((oldx,oldy))+" to "+str(self.position()))
        line = Line(Point(oldx, oldy), Point(self.getx(), self.gety()))
        line.setOutline(self.__col)  # setting the drawing colour
        line.draw(self.__win)

    def move(self, distance, sense):
        oldx = self.getx()
        oldy = self.gety()
        orientationx = math.cos(self.getanglerad())
        orientationy = math.sin(self.getanglerad())
        self.setx(oldx + orientationx * distance * sense)
        self.sety(oldy + orientationy * distance * sense)
        self.drawFrom(oldx, oldy)

    # MODIFIED TO MAKE SUPER CALL
    def moveforward(self, distance):
        super().moveforward(distance)  # appeler la méthode sur super() pour retenir cette action
        self.move(distance, 1)

    # MODIFIED TO MAKE SUPER CALL
    def movebackward(self, distance):
        super().movebackward(distance)  # appeler la méthode sur super() pour retenir cette action
        self.move(distance, -1)

    def turn(self, direction):
        self.__angle = self.__angle + direction * math.pi / 2

    # MODIFIED TO MAKE SUPER CALL
    def turnright(self):
        super().turnright()  # appeler la méthode sur super() pour retenir cette action
        self.turn(1)

    # MODIFIED TO MAKE SUPER CALL
    def turnleft(self):
        super().turnleft()  # appeler la méthode sur super() pour retenir cette action
        self.turn(-1)

    # MODIFIED TO USE METHOD ON SUPER CLASS
    def unplay(self):
        self.__col = self.getundrawcol()  # set colour to undrawing colour
        super().unplay()  # appeler la méthode sur super() pour rejouer les actions
        self.__col = self.getdrawcol()  # set colour back to standard drawing colour


# Exemple d'utilisation de cette classe (il suffit d'exécuter ce fichier)
if __name__ == '__main__':
    r2d2 = XYRobot("R2-D2")
    # first move to position (100,100) facing East, to be more or less in the center of the window
    r2d2.moveforward(100)
    r2d2.turnright()
    r2d2.moveforward(100)
    r2d2.turnleft()
    # ok, now the robot is more or less in the center of the window
    r2d2.moveforward(50)
    r2d2.turnleft()
    r2d2.moveforward(50)
    r2d2.turnleft()
    r2d2.moveforward(50)
    r2d2.turnleft()
    r2d2.moveforward(50)
    r2d2.moveforward(50)
    r2d2.turnright()
    r2d2.moveforward(50)
    r2d2.turnright()
    r2d2.moveforward(50)
    r2d2.turnright()
    r2d2.moveforward(50)
    r2d2.turnright()
    print(r2d2)
    # R2-D2@(99.99999999999997, 100.0) angle: 90.0
    print(r2d2.getHistory())
    # [('forward', 50), ('left', 90), ('forward', 50), ('left', 90), ('forward', 50), ('left', 90), ('forward', 50), ('forward', 50), ('right', 90), ('forward', 50), ('right', 90), ('forward', 50), ('right', 90), ('forward', 50), ('right', 90)]
    r2d2.unplay()
    # undoes everything that was drawn by redrawing it in opposite order
    print(r2d2)
    # R2-D2@(100.0, 100.0) angle: 0.0
    print(r2d2.getHistory())
    # []


class TurtleBot(Robot):

    # CLASS ATTRIBUTES MOVED TO SUPER CLASS

    # MODIFIED TO MAKE SUPER CALL
    def __init__(self, n):
        super().__init__(n)
        self.__t__ = turtle.Turtle()

    # MODIFIED TO MAKE SUPER CALL
    def __str__(self):
        return super().__str__() + "@" + str(self.getTurtle().position())

    def getTurtle(self):
        return self.__t__

    def getx(self):
        return self.getTurtle().xcor()

    def gety(self):
        return self.getTurtle().ycor()

    def setx(self, x):
        self.getTurtle().setx(x)

    def sety(self, y):
        self.getTurtle().sety(y)

    def position(self):
        return self.getTurtle().position()

    # MODIFIED TO MAKE SUPER CALL
    def moveforward(self, distance):
        super().moveforward(distance)  # appeler la méthode sur super() pour retenir cette action
        self.getTurtle().forward(distance)

    # MODIFIED TO MAKE SUPER CALL
    def movebackward(self, distance):
        super().movebackward(distance)  # appeler la méthode sur super() pour retenir cette action
        self.getTurtle().backward(distance)

    # MODIFIED TO MAKE SUPER CALL
    def turnright(self):
        super().turnright()  # appeler la méthode sur super() pour retenir cette action
        self.getTurtle().right(90)

    # MODIFIED TO MAKE SUPER CALL
    def turnleft(self):
        super().turnleft()  # appeler la méthode sur super() pour retenir cette action
        self.getTurtle().left(90)

    # MODIFIED TO USE METHOD ON SUPER CLASS
    def unplay(self):
        self.getTurtle().color(self.getundrawcol())  # set colour to standard drawing colour
        super().unplay()
        self.getTurtle().color(self.getdrawcol())  # set colour to standard drawing colour


# Exemple d'utilisation de cette classe (il suffit d'exécuter ce fichier)
if __name__ == '__main__':
    c3po = TurtleBot("C3-PO")
    # C3-PO@(0.00,0.00)
    c3po.moveforward(50)
    c3po.turnleft()
    c3po.moveforward(50)
    c3po.turnleft()
    c3po.moveforward(50)
    c3po.turnleft()
    c3po.moveforward(50)
    c3po.moveforward(50)
    c3po.turnright()
    c3po.moveforward(50)
    c3po.turnright()
    c3po.moveforward(50)
    c3po.turnright()
    c3po.moveforward(50)
    c3po.turnright()
    print(c3po)
    # C3-PO@(-0.00,0.00)
    print(c3po.getHistory())
    # [('forward', 50), ('left', 90), ('forward', 50), ('left', 90), ('forward', 50), ('left', 90), ('forward', 50), ('forward', 50), ('right', 90), ('forward', 50), ('right', 90), ('forward', 50), ('right', 90), ('forward', 50), ('right', 90)]
    c3po.unplay()
    print(c3po)
    # C3-PO@(0.00,-0.00)
    print(c3po.getHistory())
    # []