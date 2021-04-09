# setup, turning off animation
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
#wn.tracer(0)
t.hideturtle()

# set some global variables for the
x, y = 0, 0

def next_frame():
    # use global keyword so that x can be modified
    global x
    t.clear()
    t.up()
    t.goto(x, y)
    t.down()
    t.circle(100)
    x += 5 
    # this will cause next_frame to be called again!
    wn.ontimer(next_frame, 50)
    # don't forget to force a window update!
    wn.update()

# call function once
#next_frame()

x = 0
y = 0
for i in range(50):
    # drawing a filled triangle
    t.begin_fill()
    for i in range(3):
        t.circle(10)
        #t.forward(50)
        #t.right(120)
    t.end_fill()
    t.clear()
    x += 5 
    t.up()
    t.goto(x, y)
    t.down()
    



wn.mainloop()