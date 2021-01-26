import turtle

title_x = -380
title_y = 250

def move_turtle( t, x, y ):
     t.penup()                #don't draw when turtle moves
     t.goto( x, y)       #move the turtle to a location
     t.pendown()


# drawing a box with label X
def draw( v="" ):
    global turtle_b
    global title_x, title_y
    #print(v)   # for debigging only
    turtle_b.clear()
    turtle_b.setheading(0)
    
    move_turtle( turtle_b, title_x+210, title_y-250 )

    turtle_b.pencolor( "red" )
    turtle_b.pensize( 4 )

    turtle_b.right(90)
    turtle_b.forward(50)
    turtle_b.left(90)
    turtle_b.forward(80)
    turtle_b.left(90)
    turtle_b.forward(50)

    # drawing the label X and the value
    move_turtle(turtle_b, title_x+240, title_y-325)
    turtle_b.pencolor( "blue" )
    turtle_b.write("x", font=("Verdana", 18, "bold"))

    move_turtle(turtle_b, title_x+225, title_y-280)
    turtle_b.pencolor( "red" )
    turtle_b.write(v, font=("Verdana", 18, "bold"))

    
def find_click(x, y): 
    global screen
    global drawing
    if drawing == False:
        drawing = True
        print(x, " ", y) 
        if  -385 <= x <= -270 and 17 <= y <= 37:
            draw(42)
        elif -385 <= x <= -270 and -30 <= y <= -11:
            draw("hello")
        elif -385 <= x <= -270 and -67 <= y <= -49:
            draw(3.14)
        drawing = False

#    screen.update()


m = turtle.Turtle()
m.speed(2)
m.hideturtle() # hide the turtle writing instructions
turtle_b = turtle.Turtle()
turtle_b.hideturtle()

drawing = False


# set screen and drawing remain as it is. 
screen = turtle.Screen()
screen.title('Turtle Demo 1')
screen.bgcolor("#dcf2d5")
screen.tracer(0)

#screen_x, screen_y = screen.screensize()

screen.setup(800, 600)

#print( screen_x )
#print( screen_y )
#print( "*********" )

#print(turtle.window_height())
#print(turtle.window_width())
#print( "*********" )

####################################################################################
# interaction
####################################################################################

move_turtle( m, title_x, title_y )
m.write("How does a variable look like?", font=("Verdana", 32, "bold"))

move_turtle( m, title_x, title_y-30 )
m.write("Developer's instruction: x=12", font=("Verdana", 18, "normal"))

move_turtle( m, title_x, title_y-60 )
m.write("Computer memory:", font=("Verdana", 18, "normal"))

move_turtle( m, title_x+210, title_y-45 )
m.setheading(0)
m.pencolor( "red" )
m.pensize( 4 )

m.right(90)
m.forward(50)
m.left(90)
m.forward(80)
m.left(90)
m.forward(50)

# drawing the value
move_turtle(m,title_x+240, title_y-75)
m.pencolor( "red" )
m.write("12", font=("Verdana", 18, "bold"))

# drawing the label X
move_turtle(m,title_x+240, title_y-120)
m.pencolor( "blue" )
m.write("x", font=("Verdana", 18, "bold"))

m.pencolor( "black" )
m.pensize( 2 )

####################################################################################
# interaction
####################################################################################

move_turtle( m, title_x, title_y-200 )
m.write("Click on one of the instructions below to see their effect in memory", font=("Verdana", 18, "normal"))

move_turtle( m, title_x, title_y-240)
m.write("x = 42", font=("Verdana", 18, "normal"))

move_turtle(m, title_x, title_y-280)
m.write("x = \"hello\"", font=("Verdana", 18, "normal"))

move_turtle(m, title_x, title_y-320)
m.write("x = 3.24", font=("Verdana", 18, "normal"))

turtle.tracer(n=1, delay=10)

screen.onscreenclick( find_click )

screen.mainloop()