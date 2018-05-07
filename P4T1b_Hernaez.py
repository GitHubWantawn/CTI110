# CTI-110
# P4T1b - Initials
# Juan Hernaez
# 03/20/2018

# Set up the window and its attributes.

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Juan Hernaez' Initials")

# Create the initial "j" and set some attributes.

j = turtle.Turtle()
j.color("red")
j.pensize(9)

# Create the initial "h" and set some attributes.

h = turtle.Turtle()
h.color("red")
h.pensize(9)

# Make j draw a j.

j.forward(30)
j.left(90)
j.forward(60)
j.left(180)
j.forward(60)
j.right(90)
j.forward(30)
j.right(90)
j.forward(20)

# Pick up Turtle and move to a new location.

j.penup()
j.goto(100, 0)
j.pendown()


# Make j draw a h.
j.forward(60)
j.backward(30)
j.left(90)
j.forward(20)
j.right(90)
j.forward(30)
j.left(180)
j.forward(60)

h.left(90)

wn.mainloop()
