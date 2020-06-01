class Person:

    def __init__(self, first_name):  # initialise instance of object Person
        self.first_name = first_name  # set first name (only attribute available at the moment)


def file_test(filename):  # reading a txt file and adding instances of Class
    file = open(filename, 'r').readlines()  # open a .txt file - read each individual line
    names_list = [line.rstrip('\n') for line in file]  # create a list and loop through file, making each new line (rstrip(\n)) a separate index in the list. This means each name has its own position in the list

    name_dict = {i: Person(first_name) for (i, first_name) in enumerate(names_list, start=1)}
    #  new dictionary - because we will be randomising using numbers instead of direct names, storing a permanent number as the key in the dictionary will make following the data easier. the value will be the Person object
    return name_dict  # return dictionary

