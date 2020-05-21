from input_methods import *
from Person import *

def main():
    print("\nRANDOMISE LIST APP \n")

    all_names = []
    people = filetest('names.txt')
    for keys, values in people.items():
        all_names.append(keys)


    final_groups = run(all_names)
    for i in range(len(final_groups)):  # loop through the parent list
        print("\n GROUP " + str(i + 1))
        for j in range(len(final_groups[i])):
         print(people.get(final_groups[i][j]).getName() + ", ", end=" ")
         # print out the child lists containing the group members

    print("\n")

if __name__ == '__main__':
    main()
