import turtle

m = turtle.Turtle()

# set screen and drawing remain as it is. 
screen = turtle.Screen()
screen.title('Turtle Demo 1')
screen.bgcolor("#dcf2d5")

screen_x, screen_y = screen.screensize()

#screen.screensize(canvwidth=400, canvheight=400, bg="blue") 

#question = screen.textinput("Window name", "Question to ask")

m.showturtle()           #make the turtle visible
m.speed(2)

m.penup()                #don't draw when turtle moves
m.goto( -screen_x+50, screen_y)       #move the turtle to a location
m.pendown()

m.write("A variable is ... a container", font=("Verdana", 24, "normal"))

m.penup()
m.goto(-screen_x+50, 250)
m.pendown()

m.write("Declaring a variable ", font=("Verdana", 18, "normal"))
m.penup()
m.goto(-screen_x+20, 250)
m.pendown()
m.write("X", font=("Verdana", 18, "bold"))
m.penup()
m.goto(-210, 20)
m.pendown()
m.write(" produces", font=("Verdana", 18, "normal"))

"""
m.pencolor( "red" )
m.pensize( 4 )

m.right(90)
m.forward(100)
m.left(90)
m.forward(80)
m.left(90)
m.forward(100)

m.penup()
m.goto(-300, 20)
m.pendown()

m.write("Declaring a variable ", font=("Verdana", 18, "normal"))
m.write("X", font=("Verdana", 18, "bold"))
m.write(" produces", font=("Verdana", 18, "normal"))

m.pencolor( "red" )
m.pensize( 4 )

m.right(90)
m.forward(100)
m.left(90)
m.forward(80)
m.left(90)
m.forward(100)


#for i in range(50):
#    m.forward(50)
#    m.right(144)
     
     """

screen.mainloop()