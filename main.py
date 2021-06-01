import turtle  # TURTLE IS A LIBRARY FOM PYTHON
from turtle import Turtle, Screen  # TURTLE IS A LIBRARY FOM PYTHON
import random  # RANDOMIZE NUMBERS, COLORS

chuy = Turtle()  # NAME OF MY VARIABLE
turtle.colormode(255)  # TRANSFORM COLOR TO RGB 255 MODE
chuy.width(2)  # WIDTH OF THE LINES


def random_color():  # RANDOM COLOR WHEEL AND FUNCTION
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


chuy.speed("fastest")  # HOW FAST THE DRAWING MOVES


def draw_spirograph(size_of_gap):   # MATH OF THE WHEEL
    for _ in range(int(360 / size_of_gap)):
        chuy.color(random_color())
        chuy.circle(150)
        chuy.setheading(chuy.heading() + size_of_gap)


draw_spirograph(10)
screen = turtle.Screen()
screen.exitonclick()
