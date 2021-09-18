"""
Program: cast_to_integer.py
Author: Jeremy Hall
Last date modified: 09/18/2021
The purpose of this is to take user input of 3 scores and then output the average of those scores.
With some elementary input validation added.
"""

#constant "NUMOFSCORES" is set in the constants.py file
import constants

#get input from user
first_name = str(input("What is your first name?"))
last_name = str(input("What is your last name?"))
age = int(input("How old are you? (in whole years) "))
print("You will now be asked to enter " + str(constants.NUMOFSCORES) + " scores")
score1 = float(input("Enter a score:"))
score2 = float(input("Enter a score:"))
score3 = float(input("Enter a score:"))

#process data to determine average_score
average_score = float((score1 + score2 + score3) / constants.NUMOFSCORES)

#format output for average_score
format_average_score = "{:.2f}".format(average_score)
txt = "{}, {} age: {} average score: {}"

#output average_score
print(txt.format(last_name, first_name, age, format_average_score))

#comments from observed output
#none really. Working as planned