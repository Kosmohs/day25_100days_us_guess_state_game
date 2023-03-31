import turtle
import pandas

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
states_list = states["state"].to_list()

score = 0
guessed = []

while len(guessed) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States correct", prompt="What's another state's name ?").title()

    if answer_state in states_list:
        ans_row = states[states.state == answer_state]
        guessed.append(answer_state)
        score += 1
        x_cor = int(ans_row.x)
        y_cor = int(ans_row.y)
        t.color("red")
        t.penup()
        t.hideturtle()
        t.speed(0)
        t.setposition(x_cor, y_cor)
        t.write(answer_state)#, font=('Arial', 10, 'bold'))
    elif answer_state == "Quit" or answer_state == "Q":
        states_to_learn = [state for state in states_list if state not in guessed]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break   

print(guessed)
# screen.exitonclick()