import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


scooby_the_turtle = Turtle()
scooby_the_turtle.shape('turtle')
scooby_the_turtle.speed('fastest')


def drawing_spirograph(size_of_heading):
    for num in range(int(360 / size_of_heading)):
        scooby_the_turtle.color(random_color())
        scooby_the_turtle.circle(100)
        scooby_the_turtle.setheading(scooby_the_turtle.heading() + size_of_heading)


drawing_spirograph(10)



screen = Screen()
screen.exitonclick()
