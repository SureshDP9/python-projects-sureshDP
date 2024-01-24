from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("make a bet", "which turtle will win the race? Enter a color : ")
all_turtles = []
def move_forwards():
    new_tim.forward(10)

colors = ["red", "green", "yellow", "orange", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

is_race_on = False

for turtle_index in range(0, 6):
    new_tim = Turtle("turtle")
    new_tim.penup()
    new_tim.color(colors[turtle_index])
    new_tim.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! The {winning_color} turtle is the winner!")
            else:
                print(f"you've lost! The {winning_color} turtle is the winner!")
        turtle.forward(random.randint(0,10))

screen.exitonclick()
