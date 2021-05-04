import turtle
window = turtle.Screen()

turtle.speed(5)
turtle.pensize(5)

turtle.penup()
turtle.goto(0, 0)
turtle.penup()
turtle.color("black")

turtle.penup()
turtle.speed(3)
turtle.setposition(90, 50)
turtle.write("Parent Class ", True, align="right")

turtle.setposition(0, 0)
turtle.pendown()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.penup()


turtle.shape()
'classic'

turtle.goto(-170,-170)
turtle.color("blue")
turtle.pendown()
for i in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.penup()

turtle.setposition(-90, -50)
turtle.speed(3)
turtle.write("Child Class", True, align="right")
turtle.penup()


turtle.delay(2000)
turtle.clear()
turtle.speed(10)
turtle.setposition(0, 0)
turtle.write("This was an example of Inheritance in coding")

