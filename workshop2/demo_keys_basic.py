import turtle

edna = turtle.Turtle()

screen = turtle.Screen()
screen.title("Drawing with a turtle!")
screen.bgcolor("orange")

# screen listening for events
screen.listen()

# boundaries 
boundX = 200
boundY = 200

# draw the perimeter of the baundaries 
edna.penup()
edna.pensize(5)
edna.setposition( boundX, boundY )
edna.pendown()

for i in range(4):
    edna.right(90)
    edna.forward(400)

# repositioning the turtle to the (0,0) coordinates
edna.penup()
edna.pensize(1)
edna.setposition( 0, 0 )
edna.shape("turtle")
edna.pendown()


# # moving the turtle up and checking for collisions
def moveUp():
    global edna
    global boundY
    edna.setheading( 90 )
    # is the turtle crossing the boundary ?
    if edna.ycor() < boundY: 
        edna.forward(27)
    else:   
        edna.forward(0)

# moving the turtle down
def moveDown():
    global edna
    edna.setheading( 270 )
    edna.forward(27)

# capturing user's input
# capturing when the user presses the UP arrow
screen.onkey( moveUp, "Up")
# capturing when the user presses the DOWN arrow
screen.onkey( moveDown, "Down")

screen.mainloop()