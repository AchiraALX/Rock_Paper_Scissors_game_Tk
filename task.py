# import modules
from tkinter import *
import random

# define global variables
user_score = 0
computer_score = 0
user_choice = ""
computer_choice = ""


# define all functions
def choice():
    global computer_choice

    computer_choice = random.randrange(1, 4)

    if computer_choice == 1:
        computer_choice = "rock"

    elif computer_choice == 2:
        computer_choice = "paper"

    else:
        computer_choice = "scissors"

    return computer_choice


def rock():
    global user_choice
    global computer_score
    global user_score

    user_choice = "rock"
    choice()
    if computer_choice == "rock":
        computer_score += 0
        user_score += 0
    elif computer_choice == "paper":
        computer_score += 1
        user_score += 0
    else:
        computer_score += 0
        user_score += 1

    your_choice.config(text="rock")
    my_choice.config(text=computer_choice)
    your_score.config(text=str(user_score))
    my_score.config(text=str(computer_score))


def paper():
    global user_choice
    global computer_score
    global user_score

    user_choice = "paper"
    choice()
    if computer_choice == "rock":
        computer_score += 0
        user_score += 1
    elif computer_choice == "paper":
        computer_score += 0
        user_score += 0
    else:
        computer_score += 1
        user_score += 0

    your_choice.config(text="paper")
    my_choice.config(text=computer_choice)
    your_score.config(text=str(user_score))
    my_score.config(text=str(computer_score))


def scissor():
    global user_choice
    global computer_score
    global user_score

    user_choice = "scissors"
    choice()
    if computer_choice == "rock":
        computer_score += 1
        user_score += 0
    elif computer_choice == "paper":
        computer_score += 0
        user_score += 1
    else:
        computer_score += 0
        user_score += 0

    your_choice.config(text="scissors")
    my_choice.config(text=computer_choice)
    your_score.config(text=str(user_score))
    my_score.config(text=str(computer_score))


# create window
window = Tk()
window.title("Rock, Paper, Scissors - A Game for All!")
window.geometry("600x400")

# create widgets
score_area = Frame()
btn_area = Frame()

rock_button = Button(btn_area, text="Rock", command=rock)
paper_button = Button(btn_area, text="Paper", command=paper)
scissor_button = Button(btn_area, text="Scissors", command=scissor)
your_choice_title = Label(score_area, text="Your choice: ")
your_choice = Label(score_area)
my_choice_title = Label(score_area, text="My choice: ")
my_choice = Label(score_area)
your_score_title = Label(score_area, text="Your score: ")
your_score = Label(score_area, text="0")
my_score_title = Label(score_area, text="My Score: ")
my_score = Label(score_area, text="0")
# place widgets into window container using a layout
btn_area.pack()
score_area.pack()
rock_button.grid(row=0, column=0, padx=30, ipadx=30, pady=30)
paper_button.grid(row=0, column=1, padx=30, ipadx=30, pady=30)
scissor_button.grid(row=0, column=2, padx=30, ipadx=30, pady=30)
your_choice_title.grid(row=1, column=0, pady=30)
your_choice.grid(row=1, column=1, pady=30)
my_choice_title.grid(row=2, column=0, pady=20)
my_choice.grid(row=2, column=1, pady=20)
your_score_title.grid(row=3, column=0, pady=20)
your_score.grid(row=3, column=1, pady=20)
my_score_title.grid(row=4, column=0)
my_score.grid(row=4, column=1)

# open window
window.mainloop()
