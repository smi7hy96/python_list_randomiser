# Group Randomiser Application

## Intro

The main method to run the application from is under the CONTROL.PY file.

This app reads a .txt file ('names.txt') which contains a list of names (keep format of .txt the same but change the 
names if necessary).

It takes the list and makes each line the first name of a new Object in the Class Person. (Only one attribute - 
'first_name' at the moment)

It stores these Objects in a dictionary where the keys are the row number of the name from the .txt file.

From there it will use the list of keys of the dictionary and move the list throughout the app, eventually randomising 
them.

## User Options

As a user, there are two main routes you can go. Either organise into random groups by Maximum Group Size or by Total 
Number of Groups.

These options are chosen by entering either 1 or 2. Not entering those numbers will result in an error and ask for
input again.

The following choice will be the amount of groups (or group size) which can be any number greater than 0.

The program will organise into groups as evenly as possible.

The groups will be printed out at the end with the names displayed.
