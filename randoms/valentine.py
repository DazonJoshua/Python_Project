import turtle
import math

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Valentine's 2026")

pointer = turtle.Turtle()
pointer.speed(0)
pointer.color("red")
pointer.hideturtle()

def heart_x(t):
    return 16 * math.sin(t)**3

def heart_y(t):
    return 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

# Draw the heart
pointer.penup()
for i in range(2550):
    t = i / 100
    x = heart_x(t) * 15
    y = heart_y(t) * 15
    pointer.goto(x, y)
    pointer.pendown()

# Add a pulse effect and message
pointer.penup()
pointer.goto(0, -30)
pointer.color("white")
pointer.write("HAPPY VALENTINE'S", align="center", font=("Courier", 24, "bold"))

pointer.goto(0, -70)
pointer.write("02 . 14 . 26", align="center", font=("Courier", 18, "italic"))

turtle.done()