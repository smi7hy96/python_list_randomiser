from generator import *


def choice(question_string, choice_num, all_names):  # this method now asks for the limit number for the choice which will then push the data to the final method that will create the groups
    pos_num = False
    while not pos_num:  # will keep looping until valid number is entered
        user_number = input(question_string + "\n")  # ENTER THE MAXIMUM GROUP SIZE YOU WANT.
        # BEAR IN MIND IT WILL DISTRIBUTE GROUPS OUT AS EVENLY AS POSSIBLE
        if user_number.isnumeric():  # double checks input is a number
            user_number = int(user_number)
            if user_number > 0:  # and if its greater than 0 (cant have groups with nobody!)
                pos_num = True
                groups = create_groups(choice_num, user_number, all_names)  # perform create groups method with parameters being the choice number, limit number and the list of names - which remember are actually just numbers (keys in dictionary)
            else:
                print("Sorry, number entered is less than 1")
        else:
            print("You didn't enter a number")
    return groups  # Create groups returned the list of lists, which we will again return


def run(all_names):  # functions that ask the user to make a choice for how to separate groups.
    valid_input = False
    while not valid_input:  # loop until valid input entered
        user_choice = input("How do you want to organise groups? \n 1) By Maximum Group Size \n 2) Total Number of Groups "
              "\n Enter number of choice \n")

        if user_choice.isnumeric():  # check input is number
            x = int(user_choice)  # convert input into int
            if x == 1:  # if x is 1, perform the method using max groups size
                valid_input = True  # break loop
                groups = choice("Enter Max Group Size", x, all_names)
            elif x == 2: # if x is 2, perform the method using total number of groups
                valid_input = True  # break loop
                groups = choice("Enter Total Number of Groups", x, all_names)
            else:
                print("Invalid Choice")  # error message
        else:
            print("Didn't enter a number")  # error message
    return groups  # same list of lists from choice() is returned again so it can get back to control.py
