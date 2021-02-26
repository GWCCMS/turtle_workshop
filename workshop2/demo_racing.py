import turtle
from random import randint  

turtle.tracer(0)
edna = turtle.Turtle()
edna.shape("turtle")
#edna.speed(1)



bob = turtle.Turtle()
bob.hideturtle()
bob.shape("turtle")
bob.color("green")
bob.penup()
bob.setpos(-250,-40)
bob.pendown()

def race():
    global edna, bob
    bob.showturtle()
    for i in range(175):
        edna.forward(randint(1,5))
        bob.forward(randint(1,5))

def drawLine(x, y, l):
    edna.penup()
    edna.setpos(x, y)
    edna.pendown()
    edna.forward(l)

drawLine(-250, 100, 500)
drawLine(-250, -100, 500)

# finish line
edna.right(90)

drawLine(250, 100, 200)
drawLine(220, 100, 200)
drawLine(-250, 100, 200)

strfl = "FINISH LINE"
x = 60
for c in strfl:
    edna.penup()
    edna.setpos(230, x)
    x = x -15
    edna.pendown()
    edna.write(c, font=("Arial", 14, "normal"))


edna.right(-90)

edna.penup()
edna.setpos(-250,40)
edna.pendown()
edna.color("red")

turtle.tracer(1)


race()

turtle.done()