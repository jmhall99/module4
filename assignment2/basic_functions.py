"""
Program: basic_functions.py
Author: Jeremy Hall
Last date modified: 09/19/2021
The purpose of this program is to house a function built to take input (name, hours, rate)
from the user and print it.
"""

#Open the editor of your choice. Write a function called hourly_employee_input that asks the
# user for a name (string), hours worked (int) and an hourly pay rate (float) and prints a string
# including the information. Include a docstring as your first line declaring what the function does.
#Run the script in a shell.
#Call the function, entering expected values, numbers in appropriate range
#Call the function, entering negative numbers
#Call the function, entering bad input (letters, symbols)
#What do you need to add to your function for bad input? Handle the bad input
#Submit your screen shot and .py file.

def hourly_employee_input():
    """
    This function take 3 pieces of input and returns a message.
    """
    name = str(input("What is your name?"))
    hours = int(input("how many hours did you work?"))
    rate = float(input("What is your hourly rate?"))

    txt = "{} worked {} hours at a rate of {} per hour."
    print(txt.format(name,hours,rate))

if __name__ == '__main__':
    try:
        hourly_employee_input()  # function call
    except:
        print("uh oh, Trouble!")

