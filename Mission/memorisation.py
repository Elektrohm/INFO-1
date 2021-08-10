#Eline Nenin, Théo Denis, 15/11/18
import time
import turtle

c4=0
def fib1(n):
    """
      pre: n est un nombre natural
      post: retourne le nième nombre de Fibonacci
    """
    global c4
    c4+=1
    if n <= 1:
        return n
    t = fib1(n-1) + fib1(n-2)
    return t

def second(f,n):
    t0=time.clock()
    a=f(n)
    print(time.clock()-t0)

c3=0
def fib2(n):
    global c3
    c3+=1
    a=0
    b=1
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(n):
            c=a
            a=b+a
            b=c
        return a
    
def comparison(n):
    t0 = time.clock()
    result = fib1(n)
    t1 = time.clock()
    result1 = fib2(n)
    t2 = time.clock()
    return ("fib1{0} took {1}secs to calculate and fib2{0} took {2}secs to calculate".format(n,t1-t0,t2-t1))

        
dict_mapping={}
c1=0
def memoization(fun_mem, n):
    global c1
    c1+=1
    if fun_mem.__name__ not in dict_mapping:
        dict_mapping[fun_mem.__name__]={}
    if n not in dict_mapping[fun_mem.__name__]:
        dict_mapping[fun_mem.__name__][n]=fun_mem(n)
    return dict_mapping[fun_mem.__name__][n]

c2=0
def fibo_mem(n):
    global c2
    c2+=1
    if n <= 1:
        return n
    else:
        t = memoization(fibo_mem, n-1) + memoization(fibo_mem, n-2)
    return t

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
    t.forward(10)
    t.penup()
    
def draw_bar_time(t, height):
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
    t.forward(50)
    t.penup()

wn = turtle.Screen()         
wn.bgcolor("lightgreen")
       
       
       
tess = turtle.Turtle()       
tess.color("blue", "red")
tess.pensize(3)
tess.speed(0)
tess.penup()
tess.left(90)
tess.backward(220)
tess.right(90)
tess.pendown()

lst=[]
for a in range(10):
    lst.append(fib1(a))
    
for a in lst:
    draw_bar(tess, a)
tess.write('valeur de fibonnaci')
       
alex = turtle.Turtle()       
alex.color("blue", "red")
alex.pensize(3)
alex.right(-90)
alex.backward(170)
alex.right(90)
alex.speed(0)

k=[]
for a in range(10):
    fib1(a)
    k.append(c4)
    
for a in k:
    draw_bar(alex, a)
alex.write('nombre de fois que la récursive a été appelé')

eline = turtle.Turtle()       
eline.color("blue", "red")
eline.pensize(3)
eline.speed(0)
eline.penup()
eline.backward(700)
eline.right(-90)
eline.backward(220)
eline.right(90)
eline.pendown()

g=[]
for a in range(10):
    fib2(a)
    g.append(c3)
    
for a in g:
    draw_bar(eline, a)
eline.write("nombre de fois que l'itérative a été appelé")
                    
theo = turtle.Turtle()       
theo.color("blue", "red")
theo.pensize(3)
theo.speed(0)
theo.penup()
theo.backward(700)
theo.left(90)
theo.backward(180)
theo.right(90)
theo.pendown()

r=[]
for a in range(10):
    h=fibo_mem(a)
    r.append(c2)   

for a in r:
    draw_bar(theo, a)
theo.write('nombre de fois que la memoïsation à été appelé')

def exec_time(f):
    def exec_fun(n):
        t0=time.clock()
        a=f(n)
        return (time.clock()-t0)
    return exec_fun
       
emma = turtle.Turtle()       
emma.color("blue", "red")
emma.pensize(3)
emma.speed(0)
emma.penup()
emma.backward(700)
emma.pendown()


e=[]
d=exec_time(fib1)
for a in range(15,20):
    e.append(d(a)*10**3)

for a in e:
    draw_bar_time(emma, a)
emma.forward(30)
emma.write('temps pour la récursive (en 10**3)')

lea = turtle.Turtle()       
lea.color("blue", "red")
lea.pensize(3)
lea.speed(0)
lea.penup()
lea.backward(700)
lea.right(-90)
lea.forward(50)
lea.right(90)
lea.pendown()

b=[]
d=exec_time(fib2)
for a in range(15,20):
    b.append(d(a)*10**3)
    
for a in b:
    draw_bar_time(lea, a)
lea.forward(50)
lea.write("temps pour l'itérative (en 10**3)")       
       
john = turtle.Turtle()       
john.color("blue", "red")
john.speed(0)
john.penup()
john.backward(700)
john.left(90)
john.forward(200)
john.right(90)
john.pendown()
john.pensize(3)


p=[]
d=exec_time(fibo_mem)
for a in range(15,20):
    p.append(d(a)*10**3)
    
for a in p:
    draw_bar_time(john, a)
john.forward(50)
john.write('temps pour la mémoïser (en 10**3)')

wn.mainloop()



        
        
        


    
        
            