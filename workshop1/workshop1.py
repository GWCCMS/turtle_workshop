import turtle

# finding the size of the window that you are working with
print( "the width of the window is ", turtle.window_width())
print( "the height of the windows is", turtle.window_height())

# creating an instance of a turtle
edna = turtle.Turtle()

# giving a shape to the turtle
edna.shape("turtle")

# hiding the drawing animation
turtle.tracer(0)

# getting the current position of the turtle
print("Edna is resting at position: " , edna.position())

# drawing a sqaure
for i in range(4):
  edna.forward( 50 )
  edna.left( 90 )

print("Edna is resting at position: " , edna.position())

# moving the turtle
edna.penup()
edna.goto( -40, 0 )
edna.pendown()

# drawing another sqaure
edna.pencolor("red")
for i in range(4):
  edna.right( 90 )
  edna.forward( 50 )
  
edna.penup()
edna.goto( 0, -50 )
edna.pendown()

# writing some text
edna.write("Testing string", font=("Verdana", 12) )
  
edna.penup()
edna.goto( 25, 25 )
edna.pendown()

edna.pencolor("black")
edna.circle( 25 )

edna.penup()
edna.goto( 0, -100 )
edna.pendown()

# restarting the drawing animation
turtle.tracer(1)

# edna.clear() # clears the screen from Edna's drawings

# drawing a filled triangle
edna.begin_fill()
for i in range(3):
  edna.forward(50)
  edna.right(120)
edna.end_fill()
