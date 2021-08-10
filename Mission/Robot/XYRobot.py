from graphics import *  # un bibliothèque pour dessiner des figures simple sur un plan XY
import math  # nous avoins besoin des fonctions cos et sin pour notre calcul de la position d'un point


class XYRobot:
    # ATTRIBUTES ADDED
    __drawcol = 'black'  # standard drawing colour
    __undrawcol = 'yellow'  # colour for undrawing

    def __init__(self, n):
        self.__nom = n  # nom du robot
        self.__x = 0  # position x du robot
        self.__y = 0  # position y du robot
        self.__angle = 0  # angle en degres radius
        self.__win = GraphWin()  # fenêtre graphique sur le chemin du robot sera tracé
        self.__history = []  # LINE ADDED
        self.__col = self.__drawcol  # LINE ADDED (setting the colour to the standard drawing colour)

    # METHOD ADDED
    def getHistory(self):
        return self.__history

    # METHOD ADDED
    def addHistory(self, action):
        self.__history.append(action)

    # METHOD ADDED
    def clearHistory(self):
        self.__history = []

    def __str__(self):
        """Imprime un string du type "R2-D2@(100,100) angle: 0.0" représentant les coordonnées position du robot."""
        return str(self.getnom()) + "@(" + str(round(self.getx())) + "," + str(round(self.gety())) + ") angle: " + str(
            self.getangle())

    def getnom(self):
        return self.__nom

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

    def __drawFrom(self, oldx, oldy):
        line = Line(Point(oldx, oldy), Point(self.getx(), self.gety()))
        line.setOutline(self.__col)  # LINE ADDED (setting the drawing colour)
        line.draw(self.__win)

    def __move(self, distance, sense):
        """ méthode auxiliaire pour faire avancer ou reculer le robot en dessinant sa trace
            si sense = 1  il avance de distance pixels
            si sense = -1 il recule de distance pixels
        """
        oldx = self.getx()
        oldy = self.gety()
        orientationx = math.cos(self.getanglerad())
        orientationy = math.sin(self.getanglerad())
        self.setx(oldx + orientationx * distance * sense)
        self.sety(oldy + orientationy * distance * sense)
        self.__drawFrom(oldx, oldy)

    def moveforward(self, distance):
        """ fait avancer le robot de distances pixels et trace une ligne lors de ce mouvement """
        self.addHistory(("forward", distance))  # LINE ADDED
        self.__move(distance, 1)

    def movebackward(self, distance):
        """ fait reculer le robot de distances pixels et trace une ligne lors de ce mouvement """
        self.addHistory(("backward", distance))  # LINE ADDED
        self.__move(distance, -1)

    def __turn(self, direction):
        """ méthode auxiliaire pour les méthodes turnright() et turnleft()
            si direction = 1 elle change l'angle du robot de 90 degrés vers la droite (dans le sens des aiguilles d'une montre)
            si direction = -1 elle change l'angle du robot de 90 degrés vers la gauche (dans le sens contraire des aiguilles d'une montre)
        """
        self.__angle = self.__angle + direction * math.pi / 2

    def turnright(self):
        """ fait tourner le robot de 90 degrés vers la droite (dans le sens des aiguilles d'une montre)
        """
        self.addHistory(("right", 90))  # LINE ADDED
        self.__turn(1)

    def turnleft(self):
        """ fait tourner le robot de 90 degrés vers la gauche (dans le sens contraire des aiguilles d'une montre)
        """
        self.addHistory(("left", 90))  # LINE ADDED
        self.__turn(-1)

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
        self.__col = self.__undrawcol  # set colour to undrawing colour
        undoactions = []
        history = self.getHistory()
        for i in range(len(self.getHistory()), 0, -1):  # go through list in opposite order
            undoactions.append(self.__undoAction(history[i - 1]))
        self.clearHistory()  # clear history after undoing
        self.__col = self.__drawcol  # set colour back to standard drawing colour


# Exemple d'utilisation de cette classe (il suffit d'exécuter ce fichier)

r2d2 = XYRobot("R2-D2")

# first move to position (100,100) facing East, to be more or less in the center of the window
r2d2.moveforward(100)
r2d2.turnright()
r2d2.moveforward(100)
r2d2.turnleft()

print(r2d2)
# prints:    R2-D2@(100, 100) facing: East
r2d2.moveforward(50)
# prints:    Drawing R2-D2 from (100, 100) to (150, 100)
r2d2.turnleft()
print(r2d2)
#           R2-D2@(150, 100) facing: North
r2d2.moveforward(50)
#           Drawing R2-D2 from (150, 100) to (150.0, 50.0)
r2d2.turnleft()
print(r2d2)
#           R2-D2@(150.0, 50.0) facing: West
r2d2.moveforward(50)
#           Drawing R2-D2 from (150.0, 50.0) to (100.0, 50.0)
r2d2.turnleft()
print(r2d2)
#           R2-D2@(100.0, 50.0) facing: North  <<<--- should be South
r2d2.moveforward(50)
#           Drawing R2-D2 from (100.0, 50.0) to (100.0, 100.0)
print(r2d2)
#           R2-D2@(100, 100) facing: South(0, 1)
r2d2.moveforward(50)
r2d2.turnright()
print(r2d2)
r2d2.moveforward(50)
r2d2.turnright()
print(r2d2)
r2d2.moveforward(50)
r2d2.turnright()
print(r2d2)
r2d2.moveforward(50)
r2d2.turnright()
print(r2d2)

print(r2d2.getHistory())
# [('forward', 50), ('left', 90), ('forward', 50), ('left', 90), ('forward', 50), ('left', 90), ('forward', 50), ('forward', 50), ('right', 90), ('forward', 50), ('right', 90), ('forward', 50), ('right', 90), ('forward', 50), ('right', 90)]
r2d2.unplay()
# undoes everything that was drawn by redrawing it in opposite order
print(r2d2)
# C3-PO with history@(0.00,-0.00)
print(r2d2.getHistory())
# []
