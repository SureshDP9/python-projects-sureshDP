import random
import turtle as t


tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim.speed("fastest")
for _ in range(200):
   tim.color(random_color())
   tim.circle(100)
   tim.setheading(tim.heading() + 10)

screen = t.Screen()
screen.exitonclick()