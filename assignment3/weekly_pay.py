"""
Program: weekly_pay.py
Author: Jeremy Hall
Last date modified: 09/21/2021
The purpose of this file is to house my 2 functions)
"""

#Open the editor of your choice. Make a copy of your .py file containing the function
# called hourly_employee_input that asks the user for a name (string), hours worked (int)
# and an hourly pay rate (float) and prints a string including the information.
#Write a function weekly_pay that accepts in the parameter list the hours_worked and hourly_pay_rate
# and returns the calculated weekly pay.
#Make a function call in hourly_employee_input
#Change the string in hourly_employee_input  to print name and weekly pay
#Change the hourly_employee_input instead of printing, return a statement and print the result in the main
#Include a docstring as your first line declaring what the function does.
#Submit your .py file

def weekly_pay(hours_worked, hourly_pay_rate):
    calculated_weekly_pay = 0
    calculated_weekly_pay = hours_worked * hourly_pay_rate
    return calculated_weekly_pay


def hourly_employee_input():
    """
    This function take 3 pieces of input and returns a message.
    """
    name = ""
    hours = 0
    rate = 0.00
    #weekly_pay = 0.00

    try:
        name = str(input("What is your name?"))
        if (name == ""):
            raise ValueError()
    except ValueError as err:
        print("Sorry, your name is not blank. Try again.")

    try:
        hours = int(input("how many hours did you work? (whole numbers only please)"))
        if (hours == 0):
            raise ValueError()
    except ValueError as err:
        print("Why are you bothering people?")

    try:
        rate = float(input("What is your hourly rate?"))
        if (rate == 0):
            raise ValueError()
    except ValueError as err:
        print("please stop...")

    pay = weekly_pay(hours, rate)

    txt = "{}'s weekly pay is ${}."
    return txt.format(name, pay)

if __name__ == '__main__':
    try:
        print(hourly_employee_input())  # function call
    except:
        print("uh oh, Trouble!")

