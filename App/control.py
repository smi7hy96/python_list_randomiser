from input_methods import *
from Person import *

def main():
    print("\nRANDOMISE LIST APP \n")

    all_names = []  # empty list
    people = file_test('names.txt')  # filetest method (in Person) returns dictionary which is stored in variable people
    for keys, values in people.items():  # loop through dictionary
        all_names.append(keys)  # add the keys (which are just numbers for now) to the list created previously

    final_groups = run(all_names)  # new list which is a list of lists (each index is a list of names)
    for i in range(len(final_groups)):  # loop through the parent list
        print("\n GROUP " + str(i + 1))  # print out group names
        for j in range(len(final_groups[i])):
         print(people.get(final_groups[i][j]).first_name + ", ", end=" ")
         # print out the child lists containing the group member; separate each name with a comma

    print("\n")

if __name__ == '__main__':
    main()