import turtle  

edna = turtle.Turtle()
v = False

for i in range(20):
    if v :
        edna.color("blue")
        v = False
    else:
        edna.color("red")
        v = True
    edna.forward(i * 10)
    edna.right(90)

turtle.done()