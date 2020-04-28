"""
File: khansole_academy.py
-------------------------
This program randomly generates simple addition problems for the user, 
reads in the answer from the user, and then checks to see if they got it right or wrong, 
until the user appears to have mastered the material.
"""

import random

TOTAL_CORRECT = 3  # Assign constant number to total correct answers


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """

    correct_row = int(0)  # assign variable for correct answers

    while correct_row < TOTAL_CORRECT:  # loop until the correct row is lower than total corrects given

        if correct_row == TOTAL_CORRECT:  # loop will stop when the correct answer number will reach constant value
            print("Congratulations! You mastered addition.")
        else:
            num_1 = int(random.randint(10, 99))  # random number 1 between range 10 and 99
            num_2 = int(random.randint(10, 99))  # random number 2 between range 10 and 99
            total = num_1 + num_2  # sum of two numbers

            print("What is " + str(num_1) + "+" + str(num_2) + "?")  # asks user to input correct answer
            answer = int(input("Your answer: "))  # assign answer and prints input for user answer

            if total != answer:  # loop if the answer is incorrect gives right answer
                print("Incorrect. The expected answer is " + str(total))
                correct_row = int(0)
            else:
                correct_row = correct_row + 1
                print("Correct! You`ve gotten " + str(correct_row) + " correct in a row.")

    print("Congratulations! You mastered addition.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__=='__main__':
    main()
