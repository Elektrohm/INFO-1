import turtle
def sum(list):    
    if len(list) >= 1:
        l = list[0]
        if type(l) == type(1) or type(l)== type(1.2):
            return l + sum(list[1:])
        else:
            return 0
    else:
        return 0
    
print(sum([1,2,'a',4]))
          
def flatten(l):
    new_l = []
    for element in l:
        if isinstance(element,list):
            new_l += flatten(element)
        else:
            new_l += [element]
    return new_l

def asked_fun(fun_name):
    if fun_name == "square":
        return lambda x: x*x
    if fun_name == "add2":
        return lambda x: x+2
    if fun_name == "mul3":
        return lambda x: x*3

def map(f,l):
    new_l = []
    for i in l:
        new_l.append(f(i))
    return new_l

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.pendown()
    t.begin_fill()           
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       
tess.color("blue", "red")
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()

    


