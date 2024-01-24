import turtle
from turtle import Turtle,Screen
import random

timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple",
          "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen",
          "chocolate", "brown", "black", "gray", "white"]

directions = [0,90,180,270]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
      timmy.forward(100)
      timmy.right(angle)

# for sides in range(3,11):
#     timmy.color(random.choice(colors))
#     draw_shape(sides)


def random_walk():
   timmy.pensize(15)
   timmy.speed("fastest")
   for _ in range(100):
     timmy.color(random.choice(colors))
     timmy.forward(30)
     timmy.setheading(random.choice(directions))

# random_walk()


# dashes line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# turn 90 degree
# for _ in range(4):
#   timmy.forward(100)
#   timmy.right(90)

screen = Screen()
screen.exitonclick()