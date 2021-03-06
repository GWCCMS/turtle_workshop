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
  def get_sign(which):

    if which == COMPARE.EQUAL:
      return "=="
    if which == COMPARE.LESS:
      return "<"
    if which == COMPARE.LESSOREQUAL:
      return "<="
    if which == COMPARE.GREATER:
      return ">"
    if which == COMPARE.GREATEROREQUAL:
      return ">="
    if which == COMPARE.NOTEQUAL:
      return "!="

class Condition():

  def __init__(self):
    self.variable = chr(randint(65, 92))
    self.compare = randint(1, 6)
    self.value = randint(0, 9)

  def __init__(self, variable):
    self.variable = variable
    self.compare = randint(1, 6)
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

  def __str__(self):
    return variable + " " + compare.get_sign() + " " + str(value)

h = 50
language = LANGUAGE.CPP
test = []

bottom_margin = 20
container_height = 100
indent = 50

turn = 0  # current turn
turns = 10 # total turns
wave = 1  # current wave
waves = 5 # total waves

s = turtle.getscreen()
s.setup(820, 620) # 20 px for window sides
s.setworldcoordinates(0, 600, 800, 0)
s.mode('world') 
s.title("Conditionals Demonstration")
s.bgcolor("cyan")

screenHeight = s.screensize()[1]
screenWidth = s.screensize()[0]
col1 = screenWidth * .3

#Next button
leftNext = screenWidth - (screenWidth * .2)
bottomNext = screenHeight * .6
heightNext = screenHeight / 24
widthNext = screenWidth / 12
marginNext = screenHeight * screenWidth / 80000

font_size_small = int(round(screenWidth / 50))
font_size_medium = int(round(screenWidth * screenHeight / 24000))
font_size_large = int(round(screenWidth / 25))

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
  monitorStandLeft = screenWidth * .44
  monitorStandTop = screenHeight * .82
  monitorStandHeight = screenHeight * .1
  monitorStandWidth = screenWidth * .3
  computerLeft = screenWidth * .25
  computerTop = screenHeight * .82
  computerHeight = screenHeight * .2
  computerWidth = screenWidth * .68

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
  b.write("Marv quad speed", font=("Times New Roman", font_size_medium)) 
  b.goto(monitorStandLeft, monitorStandTop)
  b.pd
  b.fillcolor("wheat")
  b.pencolor("azure2")
  b.begin_fill()
  b.fd(monitorStandWidth)
  b.rt(90)
  b.fd(monitorStandHeight)
  b.rt(90)
  b.fd(monitorStandWidth)
  b.rt(90)
  b.fd(monitorStandHeight)
  b.end_fill()
  b.pu
  b.goto(computerLeft, computerTop)
  b.pd
  b.fillcolor("black")
  b.begin_fill()
  b.fd(computerHeight)
  b.rt(90)
  b.fd(computerWidth)
  b.rt(90)
  b.fd(computerHeight)
  b.rt(90)
  b.fd(computerWidth)
  b.end_fill()
  #computerLeft = screenWidth * .25
  #computerTop = screenHeight * .85
  #computerHeight = screenHeight * .15
  #computerWidth = screenWidth * .75

def drawGraph(s):
  g = turtle.Turtle()
  s.tracer(0, 0)
  turtleDefaults(g, True)
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

def move_turtle( t, x, y ):
    t.penup()               #don't draw when turtle moves
    t.goto( x, y)           #move the turtle to a location
    t.pendown()

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
  i = turtle.Turtle()
  turtleDefaults(i, True)
  ifstatement = test.pop()
  i.write(ifstatement, font=("Courier New", font_size_medium)) 
  ifstatement = test.pop()
  i.write(ifstatement, font=("Courier New", font_size_medium)) 
  if  -350 <= x <= -265 and 250 <= y <= 270:
      draw(42)
  elif -350 <= x <= -222 and 210 <= y <= 233:
      draw("hello")
  elif -350 <= x <= -250 and 170 <= y <= 190:
      draw(3.14)

def answer1_onclick(x, y):
  answer1.write("1", font=("Courier New", font_size_medium)) 

def answer2_onclick(x, y):
  answer1.write("2", font=("Courier New", font_size_medium)) 

def answer3_onclick(x, y):
    answer3.write("3", font=("Courier New", font_size_medium))

def answer4_onclick(x, y):
    answer4.write("4", font=("Courier New", font_size_medium))

def turtleDefaults(t, hide, color="black", fill=""): 
  t.speed(0)
  t.color(color, fill)
  if hide:
    t.ht()

def show_button(t, x, y):
  t.pu()
  t.goto(x, y)
  t.st()

def show_next():

  c.clear()
  c.pencolor("orange")

  if turn == 0:
    move_turtle(c, col1, row_y(1))
    c.write("screenWidth = " + str(screenWidth), font=("Courier New", font_size_medium))
    #c.write("Test your skill with", font=("Courier New", font_size_medium)) 
    move_turtle(c, col1, row_y(2))
    c.write("conditionals. You will".format(turns), font=("Courier New", font_size_medium)) 
    move_turtle(c, col1, row_y(3))
    c.write("get ten turns.  Each".format(turns), font=("Courier New", font_size_medium)) 
    move_turtle(c, col1, row_y(4))
    c.write("turn will have 5 waves.", font=("Courier New", font_size_medium)) 
    move_turtle(c, col1, row_y(5))
    c.write("Try to correctly choose", font=("Courier New", font_size_medium)) 
    move_turtle(c, col1, row_y(6))
    c.write("where the next line", font=("Courier New", font_size_medium)) 
    move_turtle(c, col1, row_y(7))
    c.write("will execute based", font=("Courier New", font_size_medium)) 
    move_turtle(c, col1, row_y(8))
    c.write("on the True / False.", font=("Courier New", font_size_medium)) 
  else:
    c.write("Turn completed", font=("Courier New", font_size_medium)) 

  c.pu
  c.pencolor("cyan")
  c.fillcolor('blue')
  c.goto(leftNext - marginNext, bottomNext )
  c.pd
  c.begin_fill()
  c.fd(widthNext + marginNext)
  c.rt(90)
  c.fd(heightNext + marginNext)
  c.rt(90)
  c.fd(widthNext + marginNext)
  c.rt(90)
  c.fd(heightNext + marginNext)
  c.end_fill()
  c.pu
  c.goto(leftNext, bottomNext)
  c.pencolor("white")
  c.write("NEXT", font=("Courier New", font_size_medium)) 

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
    c.write(if_begin.format(ifstatement.get_variable() + COMPARE.get_sign(ifstatement.get_compare()) + str(ifstatement.get_value())), font=("Courier New", 24)) 
    show_button(answer1, col1 + indent, row_y(2 - 1)) # -1 because the shape starts at the upper left then draws down
    c.pu()

  if len(test) > 1:
    c.goto(col1, row_y(4))
    c.pd()
    ifstatement = test[1]
    c.write(if_middle.format(ifstatement.get_variable() + COMPARE.get_sign(ifstatement.get_compare()) + str(ifstatement.get_value())), font=("Courier New", 24)) 
    show_button(answer2, col1 + indent, row_y(5 - 1)) # -1 because the shape starts at the upper left then draws down
    c.pu()

  if len(test) > 2:
    c.goto(col1, row_y(7))
    c.pd()
    ifstatement = test[2]
    c.write(if_last, font=("Courier New", font_size_medium)) 
    show_button(answer3, col1 + indent, row_y(8 - 1)) # -1 because the shape starts at the upper left then draws down
    c.pu()

  if len(test) > 3:
    c.goto(col1, row_y(10))
    c.pd()
    ifstatement = test[3]
    c.write(if_end, font=("Courier New", font_size_medium)) 
    show_button(answer4, col1, row_y(11 - 1)) # -1 because the shape starts at the upper left then draws down

def start(x, y):
  # get rid of the 'Next' button
  next_turn.ht()
  next_turn_text.clear()

  s.onscreenclick(onClick)
  show_conditional(test)
  Variable.draw_container(v, 35, h, "X", "5")
  turtle.ontimer(advance_variable, 500)

def advance_variable():
  global h
  v.clear()
  Variable.draw_container(v, 35, h, "X", "5")
  h += 20
  if (h < screenHeight - bottom_margin - container_height):
    turtle.ontimer(advance_variable, 500)
  else:
    h = 50  # reset horizontal
    show_next()


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
ifstatement = Condition("Y", COMPARE.LESS, 7)
test.append(ifstatement)
ifstatement = Condition("Z", COMPARE.NOTEQUAL, 1)
test.append(ifstatement)

v = turtle.Turtle()
turtleDefaults(v, True)
c = turtle.Turtle()
turtleDefaults(c, True)

drawBackground(s)
#drawGraph(s)

show_next()

#s.onkey(nextFSMstate, "space")
#s.listen()

s.mainloop()

