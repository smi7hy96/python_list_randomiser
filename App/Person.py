class Person():

    def getName(self):
        return self.first_name

    def __init__(self, first_name):
        self.first_name = first_name


def filetest(filename):
    file = open(filename, 'r').readlines()
    names_list = [line.rstrip('\n') for line in file]

    name_dict = {i: Person(first_name) for (i, first_name) in enumerate(names_list, start=1)}
    name_dict
    return name_dict

