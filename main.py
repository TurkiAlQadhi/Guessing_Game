'''
This program is made by
Turki Al-Qadhi student
at TAFE on 18/06/2022.

All copyright goes to TAFE NSW 2022.

Program title is a Guessing Game.

It asks the use to guess the number
that has been selected randomly by the computer
in the range 1 to 10 including 1 and 10.

Program version 1.0

'''

# Constants
# Global Variable
# "guesses" is the number of guesses allowed in the program
guesses = 3
# lower_range is the lower range in the number to be guessed
lower_range = 1
# upper_range is the upper range in the numbers to be guessed
upper_range = 10
# message is going to be the variable that takes the message to the user in the program it is assigned to empty string
message = ""
# counter to count number of guesses
count = 0
# -Sub-program to request input from the user " Guess"
def RequestInput():
    print("Please Make a Guess within the range specified ")
    user_input  = input()
    return user_input
# -Sub-program to check input from the user is a number fall in the range from 1 to 10
#  Any text or number not in the range will be consider as an Error
def CheckInputInteger(user_in):
    #elements is the range of the number to be guessed from
    elements = range (lower_range,upper_range + 1, 1)
    #
    L = [str(L) for L in elements]
#   L = ["1","2","3","4","5","6","7","8","9","10"]
    A = False
    user_in = str(user_in)
    if user_in in L:
        A = True
    else:
        A = False
        print("ERROR: Please enter a valid number withen the range specified")
    return A
# -Sub-program to check input from the user
def CheckRequest():
    input_check  = 1
    while input_check == 1:
        user_input = RequestInput()
        if CheckInputInteger(user_input) == True:
            input_check = 0
        else:
            input_check = 1
    return int(user_input)

# Import libraries
# ____random library helps the computer to select a random number 
import random

#_____ Main program start here _____
# The following line pick a random number between the range specify
computer_guess = random.randint(lower_range, upper_range)
print("guess the number within the range of " , lower_range," " , upper_range )
#this has been used for testing purposes
print(computer_guess)


# loop to check wither the guess is matching computer guess
while guesses > 0:
    user_input = CheckRequest()
    if computer_guess > user_input  :
        message = "Your guess is smaller than the number."
        print(message)
        guesses = guesses - 1
        count =+1 
    if computer_guess < user_input  :
        message = "Your guess is greater than the number."
        print(message)
        guesses = guesses - 1
        count =+1 
    if computer_guess == user_input  :
        message = "Congratulation you guessed it right!!"
        guesses = 0
        count +=1 
        break
    
if message == "Congratulation you guessed it right!!" :
    print ("Congratulation you guessed it right the number is ", computer_guess)
    print ("Number of guesses made = ", count)
    print ("Thanks for playing")

else :
    print("You run out of guesses the number you should have guessed is ", computer_guess)

# End of you main program - nothing after this.
