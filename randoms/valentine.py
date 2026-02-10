import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Tangina Valentine's Day na naman")

pointer = turtle.Turtle()
pointer.color("red")
pointer.width(2)
pointer.hideturtle()
pointer.speed(0) 


def heart_x(t):
    return 16 * math.sin(t)**3

def heart_y(t):
    return 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

# Draw the heart
pointer.penup()

for i in range(0, 628, 1): 
    t = i / 100
    x = heart_x(t) * 15
    y = heart_y(t) * 15
    pointer.goto(x, y)
    pointer.pendown()

# Add message
pointer.penup()
pointer.goto(0, -30)
pointer.color("white")
pointer.write("HAPPY VALENTINE'S DAY!", align="center", font=("Courier", 22, "bold"))

pointer.goto(0, -70)
pointer.write("02 . 14 . 26", align="center", font=("Courier", 18, "italic"))

turtle.done()