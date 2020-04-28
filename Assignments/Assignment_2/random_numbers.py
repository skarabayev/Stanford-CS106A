"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random #imports random library from Python

NUM_RANDOM = 10 #constant which determines the number of random numbers to print
MIN_RANDOM = 0 #determine the minimal values of the random numbers generated
MAX_RANDOM = 100 ##determine the maximal values of the random numbers generated

def main():

    for i in range(NUM_RANDOM):
        print(random.randint(MIN_RANDOM,MAX_RANDOM)) #prints generated randomly 10 number between MIN and MAX range

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
