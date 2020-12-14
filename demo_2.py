import turtle

def move_turtle( t, x, y ):
     t.penup()                #don't draw when turtle moves
     t.goto( x, y)       #move the turtle to a location
     t.pendown()


m = turtle.Turtle()

# set screen and drawing remain as it is. 
screen = turtle.Screen()
screen.title('Turtle Demo 1')
screen.bgcolor("#dcf2d5")

screen_x, screen_y = screen.screensize()

#screen.screensize(canvwidth=400, canvheight=400, bg="blue") 

m.showturtle()           #make the turtle visible
m.speed(2)

move_turtle( m, -screen_x+50, screen_y )

m.write("A variable is ... a container", font=("Verdana", 24, "normal"))

move_turtle( m, -screen_x+50, 250)

m.write("Declaring a variable and assigning a value to it", font=("Verdana", 18, "normal"))
move_turtle(m,-screen_x+50, 220)

# showing x=5
m.pencolor( "red" )
m.write("X = 5  => means that", font=("Verdana", 18, "bold"))

move_turtle(m, -screen_x+50, 190)

m.pencolor( "black" )
m.write("1) A container labelled X is created", font=("Verdana", 18, "normal"))

# drawing a box with label X
move_turtle( m, -screen_x+120, 180)

m.pencolor( "red" )
m.pensize( 4 )

m.right(90)
m.forward(100)
m.left(90)
m.forward(80)
m.left(90)
m.forward(100)

# drawing the label X
move_turtle(m,-screen_x+150, 50)

m.pencolor( "red" )
m.write("X", font=("Verdana", 18, "bold"))

# showing the value storedinside the box
move_turtle(m,-screen_x+50, 20)

m.pencolor( "black" )
m.write("2) The value 5 is stored inside the container", font=("Verdana", 18, "normal"))

move_turtle(m,-screen_x+120, -10)

m.pencolor( "red" )
m.pensize( 4 )

m.right(180)
m.forward(100)
m.left(90)
m.forward(80)
m.left(90)
m.forward(100)

# drawing the label X
move_turtle(m,-screen_x+150, -140)

m.pencolor( "red" )
m.write("X", font=("Verdana", 18, "bold"))

# drawing the value inside the container
move_turtle(m,-screen_x+150, -40)

m.pencolor( "red" )
m.write("5", font=("Verdana", 18, "bold"))

turtle.done()