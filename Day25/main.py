import turtle
import pandas


#setting up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


def display_state(state_name, x_axis, y_axis):
    """This function takes the name, and coordinates of the state and shows on the map"""
    display = turtle.Turtle()
    display.penup()
    display.speed("slowest")
    display.goto(x_axis, y_axis)
    display.hideturtle()
    display.write(state_name)

data = pandas.read_csv("50_states.csv") #Getting the data from the file
all_states = data.state.to_list() #Saving the states from the file in a list
guessed_states = []


while len(guessed_states) < 50:

    #Getting the user input
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another state name?").title()


    if user_answer == "Exit":
        break

    if user_answer not in guessed_states: #checking if the user has entered this answer before
        if user_answer in all_states: #checking if the answer is in the list of states from the file
            row = data[data.state == user_answer] #Getting the full row of the user's answer
            x = row.x.item() #The item() method gets the value from the series format
            y = row.y.item()
            display_state(state_name=user_answer, x_axis=x, y_axis=y)
            guessed_states.append(user_answer)



missed_states = []

for state in all_states:
    if state not in guessed_states:
        missed_states.append(state)

missed_list = pandas.DataFrame(missed_states)
missed_list.to_csv("missed_states.csv")


screen.mainloop() #Allows the screen to be on even after click