import random

def create_groups(choice_num, user_num, all_names):
    if choice_num == 1:
        max_group_size = user_num
        range_num = -(len(all_names) // -max_group_size)  # generates how many groups will be created
    elif choice_num == 2:
        range_num = user_num
        max_group_size = -(len(all_names) // -range_num)  # generates how many people will be in each group

    # based on length of list and user input
    groups = [[] for i in range(range_num)]  # creates a new list that will contain more lists!
    # number of lists in parent list is determined by range_num

    for x in range(max_group_size):  # loop through set number of times (max number of people)
        for i in range(len(groups)):  # then loop through the length of the parent list
            if len(all_names) >= 1:  # double check the original class list is not empty!
                rand_num = random.randint(0, len(all_names) - 1)
                # ^^ generate random number between 0 and length of list (ie. an index)
                groups[i].append(all_names[rand_num])  # get the person from the class list (retrieved from random position)
                # and then add them to one of the lists inside the parent list.
                # (which list is determined by which iteration in loop it is in.
                all_names.pop(rand_num)  # remove the person added from the class list so they cannot be added again to
                # another group
            else:
                break  # if the class list is now empty - stop the loop process - any other iterations are redundant

    return groups

