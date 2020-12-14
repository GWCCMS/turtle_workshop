import turtle

def move_turtle( t, x, y ):
     t.penup()                #don't draw when turtle moves
     t.goto( x, y)       #move the turtle to a location
     t.pendown()


m = turtle.Turtle()
turtle_b = turtle.Turtle()

# set screen and drawing remain as it is. 
screen = turtle.Screen()
screen.title('Turtle Demo 1')
screen.bgcolor("#dcf2d5")

screen_x, screen_y = screen.screensize()

#screen.screensize(canvwidth=400, canvheight=400, bg="blue") 

m.showturtle()           #make the turtle visible
m.speed(2)

move_turtle( m, -screen_x+50, screen_y )

m.write("Click one of the instructions below to see their effect in memory", font=("Verdana", 18, "normal"))

move_turtle( m, -screen_x+50, 250)
m.write("1) x = 42", font=("Verdana", 18, "normal"))

move_turtle(m,-screen_x+50, 210)
m.write("2) x = \"hello\"", font=("Verdana", 18, "normal"))

move_turtle(m,-screen_x+50, 170)
m.write("3) x = 3.24", font=("Verdana", 18, "normal"))

# drawing a box with label X
def draw( v="" ):
    global turtle_b
    print(v)
    turtle_b.clear()
    turtle_b.setheading(0)
    
    move_turtle( turtle_b, -screen_x+320, 0)

    turtle_b.pencolor( "red" )
    turtle_b.pensize( 4 )

    turtle_b.right(90)
    turtle_b.forward(100)
    turtle_b.left(90)
    turtle_b.forward(80)
    turtle_b.left(90)
    turtle_b.forward(100)

    # drawing the label X
    move_turtle(turtle_b,-screen_x+350, -130)
    turtle_b.pencolor( "red" )
    turtle_b.write("X", font=("Verdana", 18, "bold"))

    move_turtle(turtle_b,-screen_x+330, -50)
    turtle_b.pencolor( "green" )
    turtle_b.write(v, font=("Verdana", 18, "bold"))

    
def find_click(x, y): 
    print(x, " ", y)
    if  -350 <= x <= -265 and 250 <= y <= 270:
        draw(42)
    elif -350 <= x <= -222 and 210 <= y <= 233:
        draw("hello")
    elif -350 <= x <= -250 and 170 <= y <= 190:
        draw(3.14)
    

draw()

screen.onscreenclick( find_click )

turtle.done()