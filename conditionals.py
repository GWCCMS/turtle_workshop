# John Maher
# Gateway - Turtle Workshop
# Mirco Speretta
# 12/20/2020


import turtle
import winsound
from enum import Enum
from drawing import Variable


class LANGUAGE(Enum):
  CPP = 1
  CSHARP = 2
  JAVA = 3
  JAVASCRIPT = 4
  PHP = 5
  PYTHON = 6
  TYPESCRIPT = 7

class COMPARE(Enum):
  EQUAL = 1
  LESS = 2
  LESSOREQUAL = 3
  GREATER = 4
  GREATEROREQUAL = 5
  NOTEQUAL = 6

  @staticmethod
  def get_sigh(which):

    if which == COMPARE.EQUAL:
      return "=="

class Condition():

  def __init__(self):
    self.variable = variable
    self.compare = compare
    self.value = randint(0, 9)

  def __init__(self, variable):
    self.variable = variable
    self.compare = compare
    self.value = randint(0, 9)

  def __init__(self, variable, compare):
    self.variable = variable
    self.compare = compare
    self.value = randint(0, 9)

  def __init__(self, variable, compare, value):
    self.variable = variable
    self.compare = compare
    self.value = value

  def get_variable(self):
    return self.variable
  def set_variable(self, variable):
    self.variable = variable

  def get_compare(self):
    return self.compare
  def set_compare(self, compare):
    self.compare = compare

  def get_value(self):
    return self.value
  def set_value(self, value):
    self.value = value


h = 50
language = LANGUAGE.CPP
test = []

bottom_margin = 20
container_height = 100
indent = 50

s = turtle.getscreen()
s.setup(820, 620) # 20 px for window sides
s.setworldcoordinates(0, 600, 800, 0)
s.mode('world') 
s.title("Conditionals Demonstration")
s.bgcolor("cyan")

screenHeight = s.screensize()[1]
screenWidth = s.screensize()[0]
col1 = screenWidth * .3

shape =((0, 0), (0, 150), (40, 150), (40, 0))
turtle.register_shape('button', shape)
answer1 = turtle.Turtle()
answer1.shape('button')
answer2 = turtle.Turtle()
answer2.shape('button')
answer3 = turtle.Turtle()
answer3.shape('button')
answer4 = turtle.Turtle()
answer4.shape('button')



if (language == LANGUAGE.CPP):
  if_begin = "if ({0}) {{"
  if_middle = "}} else if ({0}) {{"
  if_last = "} else {"
  if_end = "}"

if (language == LANGUAGE.CSHARP):
  if_begin = "if ({0}) {{"
  if_middle = "}} else if ({0}) {{"
  if_last = "} else {"
  if_end = "}"

if (language == LANGUAGE.JAVA):
  if_begin = "if ({0}) {{"
  if_middle = "}} else if ({0}) {{"
  if_last = "} else {"
  if_end = "}"

if (language == LANGUAGE.JAVASCRIPT):
  if_begin = "if ({0}) {{"
  if_middle = "}} else if ({0}) {{"
  if_last = "} else {"
  if_end = "}"

if (language == LANGUAGE.PHP):
  if_begin = "if ({0}) {{"
  if_middle = "}} elseif ({0}) {{"
  if_last = "} else {"
  if_end = "}"

if (language == LANGUAGE.PYTHON):
  if_begin = "if {0}:"
  if_middle = "elif {0}:"
  if_last = "else:"
  if_end = ""

if (language == LANGUAGE.TYPESCRIPT):
  if_begin = "if ({0}) {"
  if_middle = "} else if ({0}) {"
  if_last = "} else {"
  if_end = "}"


def drawBackground(s):

# _________________________
# |  1  |        2        |
# |     |                 |
# |     |                 |
# |     |                 |
#
# Section 1 presents the value
# Section 2 displays the statement

  offsetx2ndSection = screenWidth * .25
  x2ndSectionWidth = screenWidth * .75
  y2ndSectionHeight = screenHeight * .75
  margin = screenWidth * .025
  corner = x2ndSectionWidth * .1

  b = turtle.Turtle()
  turtleDefaults(b, True)
  b.shape('turtle')
  b.pu()
  b.goto(offsetx2ndSection * .88, (margin + corner) * .8)
  b.fillcolor("wheat")
  b.pencolor("azure2")
  b.pd()
  b.begin_fill()
  b.rt(90)
  b.circle(60, 90)
  b.fd(x2ndSectionWidth - corner * 2 - margin)  
  b.circle(60, 90)
  b.fd(y2ndSectionHeight - corner * 2 - margin)  
  b.circle(60, 90)
  b.fd(x2ndSectionWidth - corner * 2 - margin)  
  b.circle(60, 90)
  b.fd(y2ndSectionHeight - corner * 2 - margin)  
  b.circle(60, 90)
  b.end_fill()
  b.up()
  b.goto(offsetx2ndSection, margin + corner)
  b.fillcolor("black")
  b.pencolor("yellow")
  b.down()
  b.begin_fill()
  b.rt(90)
  b.circle(60, 90)
  b.fd((x2ndSectionWidth - corner * 2 - margin) * .9)
  b.circle(60, 90)
  b.fd((y2ndSectionHeight - corner * 2 - margin)   * .8)
  b.circle(60, 90)
  b.fd((x2ndSectionWidth - corner * 2 - margin) * .9)
  b.circle(60, 90)
  b.fd((y2ndSectionHeight - corner * 2 - margin) * .8)  
  b.circle(60, 90)
  b.end_fill()
  b.up()
  b.goto(offsetx2ndSection + (corner / 2), y2ndSectionHeight -  (corner / 2))
  b.pencolor("gray")
  #b.write(b.pos(), font=("Courier New", 18, "bold")) 
  b.write("Marv quad speed", font=("Times New Roman", 18)) 

  
def drawGraph(s):
  g = turtle.Turtle()
  s.tracer(0, 0)
  turtleDefaults(g)
  g.lt(90)
  for x in range(0, 800, 10):
    g.pu()    
    g.goto(x, 0)
    g.pd()
    g.fd(600)
  g.rt(90)
  for y in range(0, 600, 10):
    g.pu()
    g.goto(0, y)
    g.pd()
    g.fd(800)
  s.update()

def playWinSound():
  # Source of sound effect: https://www.youtube.com/watch?v=dAVzcGcVecU\
  winsound.PlaySound('Ta-Da.wav', winsound.SND_FILENAME)

def row_y(row):

  counter = 1
  rowY = screenHeight * .1
  while (counter < row):
    counter += 1
    rowY += screenHeight * .05

  return rowY
  

def onClick(x, y): 
    print(x, " ", y)
    if  -350 <= x <= -265 and 250 <= y <= 270:
        draw(42)
    elif -350 <= x <= -222 and 210 <= y <= 233:
        draw("hello")
    elif -350 <= x <= -250 and 170 <= y <= 190:
        draw(3.14)

def answer1_onclick(x, y):
  answer1.write("1", font=("Courier New", 24)) 

def answer2_onclick(x, y):
  answer1.write("2", font=("Courier New", 24)) 

def answer3_onclick(x, y):
    answer3.write("3", font=("Courier New", 24))

def answer4_onclick(x, y):
    answer4.write("4", font=("Courier New", 24))

def turtleDefaults(t, hide, color="black", fill=""): 
  t.speed(0)
  t.color(color, fill)
  if hide:
    t.ht()

def show_button(t, x, y):
  t.pu()
  t.goto(x, y)
  t.st()

def show_conditional(test):
  # code takes 1 row and user input takes 2 rows
  # 1st row is the code
  # rows 2 and 3 are user input
  # next will either be:
  #   row 4 code and 5 & 6 are user input
  #   row 4 & 5 are user input (last row)
  c.clear()
  c.ht()
  c.pencolor("green")
  c.pu()
  if len(test) > 0:
    c.goto(col1, row_y(1))
    c.pd()
    ifstatement = test[0]
    c.write(if_begin.format(ifstatement.get_variable() + COMPARE.get_sigh(ifstatement.get_compare()) + str(ifstatement.get_value())), font=("Courier New", 24)) 
    show_button(answer1, col1 + indent, row_y(2 - 1)) # -1 because the shape starts at the upper left then draws down
    c.pu()

  if len(test) > 1:
    c.goto(col1, row_y(4))
    c.pd()
    ifstatement = test[1]
    c.write(if_middle.format(ifstatement.get_variable() + COMPARE.get_sigh(ifstatement.get_compare()) + str(ifstatement.get_value())), font=("Courier New", 24)) 
    show_button(answer2, col1 + indent, row_y(5 - 1)) # -1 because the shape starts at the upper left then draws down
    c.pu()

  if len(test) > 2:
    c.goto(col1, row_y(7))
    c.pd()
    ifstatement = test[2]
    c.write(if_last.format(ifstatement.get_variable() + COMPARE.get_sigh(ifstatement.get_compare()) + str(ifstatement.get_value())), font=("Courier New", 24)) 
    show_button(answer3, col1 + indent, row_y(8 - 1)) # -1 because the shape starts at the upper left then draws down
    c.pu()

  if len(test) > 3:
    c.goto(col1, row_y(10))
    c.pd()
    ifstatement = test[3]
    c.write(if_end.format(ifstatement.get_variable() + COMPARE.get_sigh(ifstatement.get_compare()) + str(ifstatement.get_value())), font=("Courier New", 24)) 
    show_button(answer4, col1, row_y(11 - 1)) # -1 because the shape starts at the upper left then draws down

def advance_variable():
  global h
  v.clear()
  Variable.draw_container(v, 35, h, "X", "5")
  h += 20
  if (h < screenHeight - bottom_margin - container_height):
    turtle.ontimer(advance_variable, 500)

turtleDefaults(answer1, True, "cyan", "blue")
answer1.onclick(answer1_onclick)
turtleDefaults(answer2, True, "cyan", "blue")
answer2.onclick(answer2_onclick)
turtleDefaults(answer3, True, "cyan", "blue")
answer3.onclick(answer3_onclick)
turtleDefaults(answer4, True, "cyan", "blue")
answer4.onclick(answer4_onclick)

ifstatement = Condition("X", COMPARE.EQUAL, 5)
test.append(ifstatement)

v = turtle.Turtle()
turtleDefaults(v, True)
c = turtle.Turtle()
turtleDefaults(c, True)

drawBackground(s)
#drawGraph(s)

s.onscreenclick(onClick)
show_conditional(test)
Variable.draw_container(v, 35, h, "X", "5")
turtle.ontimer(advance_variable, 500)

#s.onkey(nextFSMstate, "space")
#s.listen()

s.mainloop()

