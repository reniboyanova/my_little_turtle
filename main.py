from turtle import Turtle, Screen
import random

# # Make a square
# def make_left_move(left_move, forward_move):
#     scooby_the_turtle.left(left_move)
#     scooby_the_turtle.forward(forward_move)
#
#
# def make_a_square(forward_move, left_move_angle):
#     scooby_the_turtle.forward(forward_move)
#     for _ in range(3):
#         make_left_move(left_move_angle, forward_move)


scooby_the_turtle = Turtle()
scooby_the_turtle.shape('turtle')
scooby_the_turtle.color('hot pink')


# # Make a square
# make_a_square(150, 90)

# # Make a dashed line
# def draw_a_dashed_line(range_of_lines, forward_move):
#     for i in range(range_of_lines):
#         scooby_the_turtle.forward(forward_move)
#         scooby_the_turtle.penup()
#         scooby_the_turtle.forward(forward_move)
#         scooby_the_turtle.pendown()
#
#
# draw_a_dashed_line(10, 8)

# # with functions:

# def choose_a_color(colors):
#     scooby_the_turtle.color(random.choice(colors))
#
#
# def first_move(forward_move, colors):
#     choose_a_color(colors)
#     scooby_the_turtle.forward(forward_move)
#
#
# def drawing_shape_function(number_of_angles, angle_size, forward_move):
#     for _ in range(number_of_angles- 1):
#         scooby_the_turtle.right(angle_size)
#         scooby_the_turtle.forward(forward_move)
#     scooby_the_turtle.right(angle_size)
#
#
# # Draw shapes:
#
# list_of_colors = ['yellow', 'light green', 'dodger blue', 'dark orchid', 'coral', 'dim gray', 'medium violet red',
#                   'dark green', 'slate blue', 'gold', 'light sea green']
#
# forward_step = 100
#
# triangle_angle = 120
# square_angle = 90
# pentagon_angle = 72
# hexagon_angle = 60
# heptagon_angle = 180 - 128.571
# octagon_angle = 180 - 135
# nonagon_angle = 180 - 140
# decagon_angle = 180 - 144
#
# # triangle shape
# first_move(forward_step, list_of_colors)
# drawing_shape_function(number_of_angles=3, angle_size=triangle_angle,forward_move=forward_step)
# # without function, you can just loop like that:
#
# # for _ in range(2):
# #     scooby_the_turtle.right(triangle_angle)
# #     scooby_the_turtle.forward(100)
# # scooby_the_turtle.right(triangle_angle)
#
# # square shape
# first_move(forward_step, list_of_colors)
# drawing_shape_function(number_of_angles=4, angle_size=square_angle,forward_move=forward_step)
#
# # pentagon shape
# first_move(forward_step, list_of_colors)
# drawing_shape_function(number_of_angles=5, angle_size=pentagon_angle, forward_move=forward_step)
#
# # hexagon shape
# first_move(forward_step, list_of_colors)
# drawing_shape_function(number_of_angles=6, angle_size=hexagon_angle, forward_move=forward_step)
#
#
# # heptagon shape
# first_move(forward_step, list_of_colors)
# drawing_shape_function(number_of_angles=7, angle_size=heptagon_angle, forward_move=forward_step)
#
# # octagon shape
# first_move(forward_step, list_of_colors)
# drawing_shape_function(number_of_angles=8, angle_size=octagon_angle, forward_move=forward_step)
#
# # nonagon shape
# first_move(forward_step, list_of_colors)
# drawing_shape_function(number_of_angles=9, angle_size=nonagon_angle, forward_move=forward_step)
#
# # decagon shape
# first_move(forward_move=forward_step, colors=list_of_colors)
# drawing_shape_function(number_of_angles=10, angle_size=decagon_angle, forward_move=forward_step)

# # with Classes


class Shape:
    FORWARD_MOVE = 100
    COLORS = ['yellow', 'light green', 'dodger blue', 'dark orchid', 'coral', 'dim gray', 'medium violet red',
              'dark green', 'slate blue', 'gold', 'light sea green']

    def __init__(self, angle_degree, number_of_sides):
        self.angle_degree = angle_degree
        self.number_of_sides = number_of_sides

    def choose_a_color(self, t: Turtle):
        t.color(random.choice(self.COLORS))

    def first_move(self,t: Turtle):
        self.choose_a_color(t)
        t.forward(self.FORWARD_MOVE)

    def drawing_shape_function(self, t: Turtle):
        for _ in range(self.number_of_sides - 1):
            t.right(self.angle_degree)
            t.forward(self.FORWARD_MOVE)
        t.right(self.angle_degree)

# or you can just divide 360 / number_of_shapes
# triangle_angle = 120
# square_angle = 90
# pentagon_angle = 72
# hexagon_angle = 60
# heptagon_angle = 180 - 128.571
# octagon_angle = 180 - 135
# nonagon_angle = 180 - 140
# decagon_angle = 180 - 144

# triangle shape
triangle = Shape(120, 3)
triangle.first_move(scooby_the_turtle)
triangle.drawing_shape_function(scooby_the_turtle)

# square shape
square = Shape(90, 4)
square.first_move(scooby_the_turtle)
square.drawing_shape_function(scooby_the_turtle)

# pentagram shape
pentagram = Shape(72, 5)
pentagram.first_move(scooby_the_turtle)
pentagram.drawing_shape_function(scooby_the_turtle)

# hexagon shape
hexagon = Shape(60, 6)
hexagon.first_move(scooby_the_turtle)
hexagon.drawing_shape_function(scooby_the_turtle)

# heptagon shape
heptagon = Shape(180 - 128.571, 7)
heptagon.first_move(scooby_the_turtle)
heptagon.drawing_shape_function(scooby_the_turtle)


# octagon shape
octagon = Shape(45, 8)
octagon.first_move(scooby_the_turtle)
octagon.drawing_shape_function(scooby_the_turtle)


# Use this way ---- make your Objects, append them to a list in the order that you want and make a simple for loop

list_with_shapes = [triangle, square, pentagram, hexagon, heptagon, octagon]

for some_shape in list_with_shapes:
    some_shape.first_move(scooby_the_turtle)
    some_shape.drawing_shape_function(scooby_the_turtle)


# last easiest way :)

colors = ['yellow', 'light green', 'dodger blue', 'dark orchid', 'coral', 'dim gray', 'medium violet red',
              'dark green', 'slate blue', 'gold', 'light sea green']

def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        scooby_the_turtle.forward(100)
        scooby_the_turtle.right(angle)

for shape_side_n in range(3, 11):
    scooby_the_turtle.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
