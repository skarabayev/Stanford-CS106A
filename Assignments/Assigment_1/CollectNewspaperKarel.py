from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    turn_karel_right()
    move()
    turn_left()
    if front_is_clear():
        move()
        move()
        move()
    pick_beeper()
    turn_back()
    if front_is_clear():
        move()
        move()
        move()
    else:
        turn_left()
        """if Karel meets wall it will turn left to seek another way"""
    turn_karel_right()
    move()
    put_beeper()
    turn_karel_right()

def turn_karel_right():
    turn_left()
    turn_left()
    turn_left()

def turn_back():
    turn_left()
    turn_left()



# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
