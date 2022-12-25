import turtle
import pandas

screen = turtle.Screen()
screen.title("US States")
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)


#ovo je ako želimo s mišom dobiti kordinate
#def get_mouse_click_coor(x,y):
#    print(x, y)
#
#turtle.onscreenclick(get_mouse_click_coor)
#
#turtle.mainloop()

data = pandas.read_csv("50_states.csv")
print(data)
guessed_states = []

while len(guessed_states) <= 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What is another state name?").capitalize()

    if answer_state == "Exit":
        break

    for state in data.state:
        if state == answer_state:
            guessed_states.append(state)
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            new_x = int(data[data.state == answer_state].x)
            new_y = int(data[data.state == answer_state].y)
            t.goto(new_x, new_y)
            t.write(f"{state}", align="center", font=("Ariel", 13, "normal"))

missing_states = list(set(data.state.to_list()) - set(guessed_states))

df = pandas.DataFrame(missing_states)
df.to_csv("states_to_learn.csv")

