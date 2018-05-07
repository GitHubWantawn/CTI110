# CTI-110
# P4T1a - Shapes - Triangle and Square
# Juan Hernaez
# 03/20/2018

# Set up the window and its attributes.

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Stephanie & Juan")

# Create stephanie and set some attributes.

stephanie = turtle.Turtle()
stephanie.color("hotpink")
stephanie.pensize(5)

# Create juan and set some attributes.

juan = turtle.Turtle()
juan.color("darkblue")
juan.pensize(5)

# Make stephanie draw an equilateral triangle.

for i in range(3):
    stephanie.forward(80)
    stephanie.left(120)

# Complete the triangle.


# Turn stephanie around.

stephanie.right(180)

# Move stephanie away from the origin.

stephanie.forward(80)

# Make juan draw a square.

for i in range(4):
    juan.forward(50)
    juan.left(90)

wn.mainloop()




