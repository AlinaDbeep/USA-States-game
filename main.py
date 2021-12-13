import turtle
import pandas as pd
import time


def game():
    game_on = True
    
    
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.bgpic(image)

    pen = turtle.Turtle()
    pen.penup()
    pen.hideturtle()

    df = pd.read_csv("50_states.csv")
    states = df.state.tolist()
    x = df.x.tolist()
    y = df.y.tolist()

    guessed = []
    score = 0

    while game_on:

        answer_state = screen.textinput(title=f"Guess the State. Score {score}/50", prompt="What's the other state?: ").title()
        print(answer_state)
        if answer_state in states and answer_state not in guessed and score !=50:
            print("True!!!!!")
            score += 1
            guessed.append(answer_state)
            print_x = x[states.index(answer_state)]
            print_y = y[states.index(answer_state)]
            pen.setposition(print_x, print_y)
            pen.write(f"{answer_state}", align = "center")
        else:
            score = score
            answer_state = screen.textinput(title=f"Guess the State. Score {score}/50", prompt="What's the other state?: ").title()
            print(answer_state)
        
        
        if score == 50:
            game_on = False
            print("congrats!")
            screen.clear()
            screen.bgpic("kitty.gif")
            again = screen.textinput(title="Wanna play again?", prompt=" Type 'y' or 'n': ").lower()
            if again == 'y':
                guessed.clear()
                game()
            else:
                screen.bye()   
                
    screen.exitonclick() 

game()


