"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():

    for i in range(10,0,-1): #call of beginns from 10 till 0 with -1 step backward count
        print(i) #print in module i values
    print("Liftoff!") #after completion of the count down prints command to LIFT OFF

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
