# This is an example comment in python

# Video for refference: https://www.youtube.com/watch?v=-nh9rCzPJ20

# To run in VS Code, right click and select 'Run Python in Terminal'

# To run a virtual module in Python: python -m venv venv
# This creates a virtual environemtn you can work off of...the second venv is the virtual enviornment name after the command
# It creates that venv folder in your project directory. In VS Code, you can then select that virtual enviornment in the
# Same section to change interpreter below

# To change interpreter in VS Code, go to the bottom left hand corner of the screen and
# Click the version on the bottom. It should show in the menu bar what versions you have installed.

# To 'autoformat' code, you'll need to install something on VS COde
# Use the following in VS Code: Shift + Alt + f
# This dude used 'Black'
# I think VS Code automatically formats this code whenever it saves...

# Recoomend getting 'Code Runner' as an extension...makes this easier to run

# To install a certain package:
# pip install requests --user
# We need to use that --user section because windows gets fussy with permissions

# This is for telling versioning of Python installed
import sys
import os
import math

# See above to install this package beforehand
import requests

# print(sys.version)  # prints version
# print(sys.executable)  # prints location where Python is installed
# print(os.getcwd())  # get the working directory

# import a class from a directory we are running main in
import classtest

# from classtest import myClass

# import our class from a different directory; this is used in the example below
print(sys.path)
from classfolder.mymodule import myModuleGreeting as myGreeting

# These are all the directories python will look in to import directories
# print()
# print(sys.path)
# print()
# This is one way to add a module to your syspath...but it's not the BEST way
# sys.path.append('D:\Python Programming\Python Programming\example_all_project\otherclasses')

# from otherclasses import greetingcool, myCoolClass
# insert at position 1 in the path, as 0 is the path of this file.
# classesfolder = os.getcwd() + "\otherclasses"
# sys.path.insert(1, classesfolder)
# from car import Car as Car #import this file

# define a function
# def greet(who_to_greet):
#     greeting = "Hello, {}".format(who_to_greet)
#     return greeting


# print(greet("World"))
# print(greet("Joe"))
# print("")

# This is an example package from the 'requests' package.
# To learn more about this, right click on any section,('get', for example)
# , then go to 'Peek Definition' or 'Go To Definitiion'
# Make sure you have no issues with VPN or whatever as well!
# python command in terminal:
# try: pip install requests
# try:
#     r = requests.get("http://josephkeller.me/")
#     print(r.status_code)
# except Exception as e:
#     print("Could not reach your resume site! {}", format(e))

# # Read from file example
# f = open(
#     "guru99.txt", "a+"
# )  # 'a+' means append, and the plus creates the file if it dosen't exist
# # append 2 lines
# for i in range(2):
#     f.write("Appended line %d\r\n" % (i + 1))
# # close file
# f.close()
# # open file again and read from it
# g = open("guru99.txt", "r")
# for x in g:
#     print(x)

# # close the file when finished reading/writing
# f.close()

# This allows you to exit the program; it will not run anytghing beneth it
# you must import sys
# sys.exit()

# This is a sure fire way to test if the file you are running is the MAIN file
if __name__ == "__main__":
    print("This is the main")

# Test with classes
# classtest.greeting("Michael")
# testMyClass = classtest.myClass("Example string")
# print(testMyClass.getVal() + " is the value here")

# nicholas = classtest.Student("Nicholas", "Computer Science")
# nicholas.get_student_details()

# Test with classes in another directory
# This was defined way up top!
# Example: https://www.youtube.com/watch?v=X1cwEKfRZJEThan
myGreeting()