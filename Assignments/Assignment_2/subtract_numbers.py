"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    print("This program subtracts one number from another.") #Gives to user information about the code
    num_1 = float(input("Enter first number: ")) #where user enters first value
    num_2 = float(input("Enter second number: ")) #user enters second number
    Result = num_1-num_2 #result of arithmetic subtraction
    print("The result is" + " " + str(Result)) #gives the result in module to user


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
