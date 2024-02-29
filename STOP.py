#CS175L
#Delvis Rodriguez
#STOP

import math
import turtle

#Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = 2
TEXT_Y = -25

#Size the window
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

#Calculating he diameter of the octagon
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

#Initialize the turtle

stop = turtle.Turtle()

# Move the turtle to the starting point
stop.penup()
stop.goto(-50, -116)
stop.pendown()
stop.hideturtle()

#Outer octagon
stop.begin_fill()
for x in range (0, NUM_SIDES):
    stop.color('red')
    stop.fillcolor('red')
    stop.forward(100)
    stop.left(45)
stop.end_fill()

#Inside octagons
stop.penup()
stop.goto(-46.5, -108)
stop.pendown()
stop.begin_fill()
for y in range(0, NUM_SIDES):
    stop.color('white')
    stop.fillcolor('white')
    stop.forward(93)
    stop.left(45)
stop.end_fill()

stop.penup()
stop.goto(-42, -98)
stop.pendown()
stop.begin_fill()
for z in range(0, NUM_SIDES):
    stop.color('red')
    stop.fillcolor('red')
    stop.forward(84.5)
    stop.left(45)
stop.end_fill()

#Display 'STOP'
stop.penup()
stop.goto(TEXT_X, TEXT_Y)
stop.pendown()
stop.begin_fill()
stop.color('white')
stop.fillcolor('white')
stop.write('STOP', align = 'center', font = ('Arial', 48, 'bold'))
stop.end_fill()

