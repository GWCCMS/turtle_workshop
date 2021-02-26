import turtle
import random

edna = turtle.Turtle()

lineSize = 20
boundX = 10
boundY = 10

screen = turtle.Screen()
screen.title("Drawing with a turtle!")
screen.bgcolor("orange")
screen.listen()

edna.penup()
edna.setpos(boundX, boundY)
edna.pendown()
edna.pencolor("green")
edna.pensize(5)
for i in range(4):
    edna.right(90)
    edna.forward(20)

edna.shape("turtle")
edna.penup()
edna.setpos(-100, 0)
edna.pendown()
edna.pencolor("black")
edna.pensize(1)

def isCollision():
    global edna
    if edna.xcor() <= boundX and edna.xcor() >= -boundX and edna.ycor() <= boundY and edna.ycor() >= -boundY:
        return True
    else:
        return False


def up():
    global edna
    edna.setheading(90)
    edna.forward(  lineSize )
    if isCollision():
        edna.color("red")
    
    

def down():
    global edna
    edna.setheading(270)
    edna.forward(  lineSize )
    if isCollision():
        edna.color("red")


def right():
    global edna
    edna.setheading(0)
    edna.forward(  lineSize )
    if isCollision():
        edna.color("red")


def left():
    global edna
    edna.setheading(180)
    edna.forward(  lineSize )
    if isCollision():
        edna.color("red")


screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.mainloop()