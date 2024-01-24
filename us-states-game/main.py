import turtle
import pandas

IMG = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. State Game")
screen.addshape(IMG)

turtle.shape(IMG)

guessed_states = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

score = 0
while len(guessed_states) < 10:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/10 \nGuess State", prompt="What's another state name?")
    if answer_state == "exit":
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(answer_state)
data_dict = {
    "states" : guessed_states
}
df = pandas.DataFrame(data_dict)
df.to_csv("save_data.csv")



screen.exitonclick()
