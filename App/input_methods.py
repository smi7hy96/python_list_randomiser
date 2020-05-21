from generator import *


def choice(question_string, choice_num, all_names):
    pos_num = False
    while not pos_num:  # will keep looping until valid number is entered
        user_number = input(question_string + "\n")  # ENTER THE MAXIMUM GROUP SIZE YOU WANT.
        # BEAR IN MIND IT WILL DISTRIBUTE GROUPS OUT AS EVENLY AS POSSIBLE
        if user_number.isnumeric():  # double checks input is a number
            user_number = int(user_number)
            if user_number > 0:  # and if its greater than 0 (cant have groups with nobody!)
                pos_num = True
                groups = generate_groups(choice_num, user_number, all_names)
            else:
                print("Sorry, number entered is less than 1")
        else:
            print("You didn't enter a number")
    return groups

def generate_groups(choice_num, user_num, all_names):
    groups = create_groups(choice_num, user_num, all_names)
    return groups



def run(all_names):
    valid_input = False
    while not valid_input:
        user_choice = input("How do you want to organise groups? \n 1) By Maximum Group Size \n 2) Total Number of Groups "
              "\n Enter number of choice \n")

        if user_choice.isnumeric():
            x = int(user_choice)
            if x == 1:
                valid_input = True
                groups = choice("Enter Max Group Size", x, all_names)
            elif x == 2:
                valid_input = True
                groups = choice("Enter Total Number of Groups", x, all_names)
            else:
                print("Invalid Choice")
        else:
            print("Didn't enter a number")
    return groups
