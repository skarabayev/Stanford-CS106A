from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
-----------------------------------------------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
Karel moves through the wall and repair buildings.
There are only 4 buildings on 1,5,9,13 columns
"""


def main():
    turn_left()
    for i in range(3):
        build_arche()
        move_to_next_wall()
    build_arche()


def move_to_next_wall():
    """
    Karel goes to next wall 4 points away
    -------------------------------------------------------
    pre: Karel facing east at the bottom of the arche
    post: Karel facing east at the bottom of the next arche	
    """
    for i in range(4):
        if front_is_clear():
            step_down()
        else:
            step_up()
    turn_right()


def step_up():
    """
    Karel makes one step to south
    ---------------------------------------
    pre: Karel facing east front is blocked
    post: Karel facing east front is clear
    """
    turn_right()
    move()
    turn_left()
    move()


def step_down():
    """
    Karel makes one step to north
    ----------------------------------------
    pre: Karel facing east front is clear
    post: Karel facing east front is blocked
    """
    move()
    turn_left()
    move()
    turn_right()


def build_arche():
    """
    Karel repairs entire column
    -----------------------------------------------------------
    pre: Karel stands the beginning of the arche to be repaired
    post: Karel stands at the end of recently repaired arche 
    """
    while front_is_clear():
        repair_arche()
    if front_is_blocked():
        if no_beepers_present():
            put_beeper()
    move_to_base()


def move_to_base():
    """
    Karel moves to base of the arche
    --------------------------------------------------
    pre: Karel at the top of the column
    post: Karel at the bottom of the column facing east
    """
    if left_is_blocked():
        turn_right()
    else:
        turn_around()
        while front_is_clear():
            move()
        turn_right()


def repair_arche():
    """
    Karel checks and put stones into empty spaces
    ---------------------------------------------
    pre: no
    post: repaired cell
    """
    if no_beepers_present():
        put_beeper()
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


if __name__=="__main__":
    run_karel_program()
