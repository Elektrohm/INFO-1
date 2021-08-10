#dessine le drapeau soviétique et européen avec une banderole de drapeau tricolore ainsi que deux char d'assaut
#Réaliser par Nenin Eline et Denis Théo, remerciement à Xavier de Liedekerke pour le drapeau américain

def etoile(width):
    '''trace une étoile à 5 branches et la remplie
    pre: width détermine la taille que prendra l'étoile
    post: tess dessine une étoile à 5 branches'''
    tess.begin_fill()
    for e in range (5) :
        tess.forward(1/4*width)
        tess.left(144)
    tess.end_fill()
    

def placement(width):
    '''positionne les 12 étoiles du drapeaux et les trace
    pre: width détermine la distance à laquelle les étoiles seront placées
    post: tess dessine les 12 étoiles du drapeau tout en les plaçant'''
    theta = 0
    for i in range (12):
        tess.right(theta) #les étoiles se positionnent comme les points d'un dodécagone sur un cercle, l'angle doit donc augmenter à chaque nouveau point
        tess.forward(3/4*width)
        tess.left(theta) # permet à l'étoile d'être orienté vers le nord comme toutes celles d'avant
        tess.left(18) # permet que les étoiles soient droites et pas de travers
        etoile(width)
        tess.penup()
        tess.right(18)
        tess.right(theta)
        tess.backward(3/4*width)
        tess.left(theta)
        theta += 30 #augmente la valeur de l'angle à chaque passage

def cadre(width):
    '''dessine le fond bleu du drapeau européen
    pre: width détermine la taille du drapeau européen
    post: alexandre dessine le fond bleu du drapeau européen'''
    alexandre.forward(1.5*width)
    alexandre.left(90)
    alexandre.begin_fill()
    for i in range(2):
        alexandre.forward(1.1*width)
        alexandre.left(90)
        alexandre.forward(3.15*width)
        alexandre.left(90)
        alexandre.forward(9/10*width)
    alexandre.end_fill()
  
  
def european_flag(width):
    '''dessine le drapeau européen
    pre: width détermine tous les paramêtres présents dans les fonctions
    post: alexandre et tess dessine le drapeau européen'''
    cadre(width)
    placement(width)
    tess.color("#003399")
    alexandre.shape("blank")

def square(size, color):
    """Trace un carré plein de taille `size` et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(4):
        tortue.forward(size)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()


def rectangle(width, height, color):
    """ pre: 'width' spécifie la largeur et 'height' la hauteur
             'color' spécifie la couleur
             La tortue est placée à un sommet et orientée en direction
             d'un côté de rectangle.
        post: Le rectangle a été tracé sur la droite du premier côté.
              La tortue est à la même position et orientation qu'au départ.
              """
    
    tortue.hideturtle()
    tortue.color(color)
    tortue.begin_fill()
    tortue.penup()
    for i in [1,2]:
        tortue.forward(width)
        tortue.right(90)
        tortue.forward(height)
        tortue.right(90)
   
    tortue.end_fill()
    
def belgian_flag(width):
    """ pre: 'width' spécifie la largueur du drapeau
        post: le drapeau est d'abord noir puis jaune puis rouge et est
        tracé à droite du premier côté.
    """
    for color in ["black","yellow", "red"]:
        rectangle(width/3,2*width/3,color)
        tortue.color(color)
        tortue.forward(width/3)

def three_color_flag(width,color1,color2,color3,direction):
    """ pre: 'width' spécifie la largueur du drapeau
             'color1','color2','color3' spécifient les couleurs des bandes.
        post: le drapeau est d'abord de couleur 1 puis 2 puis 3 et est
        tracé à droite du premier côté.
    """
    if direction=="vertical":
        for color in [color1,color2,color3]:
            rectangle(width/3,2*width/3,color)
            tortue.color(color)
            tortue.forward(width/3)
    else:
        for color in [color1,color2,color3]:
            rectangle(width,2*width/9,color)
            tortue.color(color)
            tortue.right(90)
            tortue.forward(2*width/9)
            tortue.left(90)

def german_flag(width):
    three_color_flag(width,"black","red","yellow","horizontal")
    
def dutch_flag(width):
    three_color_flag(width,"red","white","dark blue","horizontal")

def luxemburg_flag(width):
    three_color_flag(width,"red","white","light blue","horizontal")
    
def french_flag(width):
    three_color_flag(width,"medium blue","white","red","vertical")

def italian_flag(width):
    three_color_flag(width,"green","white","red","vertical")


def fond_rouge(): #dessine le fond rouge du drapeau soviétique
    t.begin_fill()
    for i in range(2):
        t.forward(800)
        t.left(90)
        t.forward(400)
        t.left(90)
    t.end_fill()
    t.penup()
    t.home()
    t.backward(20)
    
def faucille(): #dessine la faucille du drapeau soviétique
    t.color("yellow")
    t.begin_fill()
    t.right(45)
    t.circle(10,450)
    t.forward(50)
    t.right(90)
    t.circle(50,200)
    t.left(160)
    t.forward(10)
    t.circle(-45,190)
    t.left(95)
    t.forward(60)
    t.end_fill()
    t.penup()
    t.home()

def marteau(): #dessine le marteau du drapeau soviétique
    t.forward(120)
    t.pendown()
    t.begin_fill()
    t.left(120)
    t.circle(8,365)
    for i in range(2):
        t.forward(100)
        t.left(90)
        t.forward(16)
        t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(20)
    t.left(135)
    t.forward(25)
    t.left(45)
    for i in range(2):
        t.forward(30)
        t.left(90)
        t.forward(20)
        t.left(95)
    t.end_fill()

def star(): #dessine l'étoile du drapeau soviétique et une deuxième à l'intérieur pour n'avoir qu'un contour jaune
    t.penup()
    t.home()
    t.forward(90)
    t.left(90)
    t.forward(130)
    t.left(18)
    t.begin_fill()
    for e in range (5) :
        t.forward(50)
        t.left(144)
    t.end_fill()
    t.penup()
    t.left(14)
    t.forward(10)
    t.right(14)
    t.color("red")
    t.begin_fill()
    for e in range (5) :
        t.forward(30)
        t.left(144)
    t.end_fill()
    t.shape("blank")

def sovietique_flag():#dessine l'ensemble du drapeau soviétique
    fond_rouge()
    faucille()
    marteau()
    star()

def position():#positionne alexandre et tess pour que le drapeau européen soit aligné avec le drapeau soviétique
    alexandre.backward(401)
    alexandre.left(90)
    alexandre.backward(20)
    alexandre.right(90)
    tess.right(90)
    tess.backward(401)
    tess.left(90)
    tess.backward(20)
def place():#positionne tortue pour qu'elle puisse dessiner la banderole au dessus du drapeau soviétique et européen
    tortue.left(90)
    tortue.forward(40)
    tortue.right(90)
    tortue.forward(60)
    
def banderole(): #dessine une banderole de drapeau à 3 bandes
    tortue.penup()
    tortue.backward(740)
    tortue.left(90)
    tortue.forward(240)
    tortue.right(90)
    tortue.pendown()
    for i in range(4):
        belgian_flag(60)
        dutch_flag(60)
        place()
        german_flag(60)
        place()
        luxemburg_flag(60)
        place()
        french_flag(60)
        italian_flag(60)

def char(): #dessine un char d'assaut 
    s.begin_fill()
    s.width(4)
    s.forward(400)
    s.right(90)
    s.forward(50)
    s.backward(50)
    s.left(90)
    s.backward(50)
    s.left(120)
    s.forward(50)
    s.right(90)
    s.forward(50)
    s.left(30)
    s.forward(10)
    s.right(60)
    s.forward(200)
    s.left(90)
    s.forward(20)
    s.left(90)
    s.forward(200)
    s.right(30)
    s.forward(50)
    s.left(30)
    s.forward(100)
    s.left(90)
    s.forward(50)
    s.right(90)
    s.forward(180)
    s.left(60)
    s.forward(82)
    s.right(60)
    s.end_fill()
    for i in range(7):
        s.begin_fill()
        if i == 0:
            s.circle(30,630)
        elif i % 2 == 0 and i != 0:
            s.circle(30,540)
        else :
            s.circle(-30,540)
        s.end_fill()
    s.left(180)
    s.circle(-30,90)
    s.forward(360)
    s.shape("blank")
    
def preparatif(): #positionne la tortue s pour qu'elle place correctement le char
    s.left(90)
    s.penup()
    s.backward(330)
    s.right(90)
    s.pendown()
    
def emplacement(): #positionne la tortue s pour qu'elle place correctement le deuxième char
    s.penup()
    s.home()
    preparatif()
    s.penup()
    s.backward(700)
    s.pendown()

def draw_star(pau,K): #dessine les étoiles du drapeau américain
    pau.color("white")
    pau.pendown()
    pau.begin_fill()
    for x in range (5):
        pau.forward(K)
        pau.left(72)
        pau.forward(K)
        pau.right(144)
    pau.end_fill()
    pau.penup()

def star_pattern(sam,F,H,K): #positionne les étoiles du drapeau américain
    for z in range(5):
        for i in range(6):
            draw_star(sam,K)
            sam.forward(2*H)
        sam.right(90)
        sam.forward(2*F)
        sam.left(90)
        sam.forward(-12*H)
    sam.left(90)
    sam.forward(9*F)
    sam.right(90)
    sam.forward(H)
    for y in range(4):
        for j in range(5):
            draw_star(sam,K)
            sam.forward(2*H)
        sam.right(90)
        sam.forward(2*F)
        sam.left(90)
        sam.forward(-10*H)

def draw_rectangle(xav,L,l): #dessine le fond bleau du drapeau américain
    xav.pendown()
    xav.begin_fill()
    for n in range (2):
        xav.forward(L)
        xav.right(90)
        xav.forward(l)
        xav.right(90)
    xav.end_fill()

def stripes(sam,L,B): #dessine les lignes du drapeau américain
    sam.color("#C30C3E")
    for i in range(7):
        sam.begin_fill()
        sam.pendown()
        sam.forward(B)
        sam.right(90)
        sam.forward(L)
        sam.right(90)
        sam.forward(B)
        sam.end_fill()
        sam.penup()
        sam.left(90)
        sam.forward(L)
        sam.left(90)
 
def american_flag(A):
    B=1.9*A
    C=A*7/13
    D=B*2/5
    F=C/10
    H=D/12
    L=A/13
    K=L/4
    stripes(sam,L,B)
    sam.left(90)
    sam.forward(14*L)
    sam.right(90)
    sam.color("#00204E")
    draw_rectangle(sam,D,C)
    sam.right(90)
    sam.forward(F*4/5)
    sam.left(90)
    sam.forward(H*4/7)
    sam.color("white")
    star_pattern(sam,F,H,K)
    
import turtle
#propriété de la tortue tess
tess = turtle.Turtle()
tess.color("#FFCC00")
tess.left(90)
tess.speed(0)

#propriété de la tortue alexandre
alexandre = turtle.Turtle()
alexandre.speed(0)
alexandre.color("#003399")
#propriété de la tortue tortue
tortue = turtle.Turtle()     
tortue.speed(0)
#propriété de la tortue s
s = turtle.Turtle()
s.speed(0)
#propriété de la tortue t
t = turtle.Turtle()
t.color("red")
t.speed(0)
#propriété de la tortue sam
sam = turtle.Turtle()
sam.color("#00204E")
sam.pensize(1)
sam.shape("blank")
sam.speed(0)

stalin = turtle.Turtle()
stalin.left(90)
stalin.penup()
stalin.backward(250)
stalin.right(90)
stalin.pendown()
stalin.write("for the mother russia")
t.backward(100)
t.left(90)
t.backward(200)
t.right(90)

sovietique_flag()
position()
european_flag(200)
banderole()
preparatif()
char()
emplacement()
char()
sam.penup()
sam.left(90)
sam.forward(395)
sam.right(90)
sam.backward(200)
sam.pendown()
american_flag(150)

wn = turtle.Screen()
wn.mainloop
