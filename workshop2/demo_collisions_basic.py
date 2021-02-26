import turtle
import random

lineSize = 50
boundX = 200
boundY = 200

edna = turtle.Turtle()
edna.shape("turtle")

screen = turtle.Screen()
screen.title("Drawing with a turtle!")
screen.bgcolor("orange")
screen.listen()

edna.penup()
edna.setpos(-boundX, boundY)
edna.pendown()
edna.pencolor("green")
edna.pensize(5)
edna.forward(400)

edna.penup()
edna.setpos(0, 0)
edna.pendown()
edna.pencolor("black")
edna.pensize(1)

def up():
    global edna
    edna.setheading(90)
    movedY = edna.ycor() + lineSize
    if movedY < boundY:
        edna.forward(  lineSize )
    else:
        edna.forward( boundY - edna.ycor() )

screen.onkey(up, "Up")

screen.mainloop()