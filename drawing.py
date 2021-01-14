# John Maher
# Gateway - Turtle Workshop
# Mirco Speretta
# drawing module
# 12/28/2020
#
# Taken from demo_3.py for consistent variable representation

import turtle

class Shape:
    

    def __init__(self, t, sides):
        self.sides = sides
        self.t = t #turlte

    def set_size(self, size):
        self.size = size
   
    def draw():

        angle = sides / 360

        for r in range(sides):
            t.fd(50)
            t.lt(angle)


class Variable:

    @staticmethod        
    def move_turtle( t, x, y ):
        t.penup()               #don't draw when turtle moves
        t.goto( x, y)           #move the turtle to a location
        t.pendown()
        
    # drawing a box with label and value
    @staticmethod
    def draw_container( t, x, y, n="", v="" ):

        turtle.tracer(0, 0)
        t.ht()
        Variable.move_turtle( t, x, y)

        t.pencolor( "red" )
        t.pensize( 4 )

        t.left(90)
        t.forward(100)
        t.right(90)
        t.forward(80)
        t.right(90)
        t.forward(100)
        t.left(90)

        # drawing the label
        Variable.move_turtle(t, x+30, y+130)
        t.pencolor( "blue" )
        t.write(n, font=("Verdana", 18, "bold"))

        # drawing the value
        Variable.move_turtle(t, x+10, y+50)
        t.pencolor( "green" )
        t.write(v, font=("Verdana", 18, "bold"))

        turtle.update()