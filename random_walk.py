from turtle import Turtle, Screen
import random

scooby_the_turtle = Turtle()
scooby_the_turtle.shape('turtle')
scooby_the_turtle.color('hot pink')


colors = ['yellow', 'light green', 'dodger blue', 'dark orchid', 'coral', 'dim gray', 'medium violet red',
              'dark green', 'slate blue', 'gold', 'light sea green']

sides = [0, 90, 180, 270]

scooby_the_turtle.pensize(15)
scooby_the_turtle.speed("fastest")

for n in range(1, 200):
    scooby_the_turtle.color(random.choice(colors))
    scooby_the_turtle.forward(30)
    scooby_the_turtle.setheading(random.choice(sides))


screen = Screen()
screen.exitonclick()